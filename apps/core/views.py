from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)
from apps.members.models import Member
from apps.partnerships.models import Partnership
from apps.publications.models import Paper
from apps.about.models import About
from apps.links.models import Link
from apps.news.models import News
from django.db.models import Count
from django.db.models import Q
from django.db.models.functions import ExtractYear
from django.utils.translation import ugettext_lazy as _

class HomeView(ListView):
    template_name = "core/home.html"
    context_object_name = 'context_members'

    # Two conditions:
    # AND: ~Q(...) & ~Q(...)
    # OR:  ~Q(...) | ~Q(...)
    def get_queryset(self):
        _members_all = Member.objects.all().filter(~Q(role_id = 1) & ~Q(role_id = 7), status = True).order_by('role__order', 'first_name')
        # _members_postdoc = _members_all.filter(role_id = 2) # Postdoctoral fellows
        # _members_phd_stu = _members_all.filter(role_id = 3) # Ph.D Student
        # _members_msc_stu = _members_all.filter(role_id = 4) # M.Sc. Student
        # _members_sci = _members_all.filter(role_id = 5) # Scientific Initiation
        # _members_vis = _members_all.filter(role_id = 6) # Visiting Researchers and Students
        # _members = _members_postdoc.order_by('first_name') | _members_phd_stu.order_by('first_name')
        return _members_all

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        # Members context
        query_coordinator = Member.objects.all().filter(status = True, role_id = 1)
        context['context_members_coordinator'] = query_coordinator

        # About context
        query_about = About.objects.get(status = True, pk = 1)
        context['context_about'] = query_about

        # Links context
        query_links = Link.objects.all().filter(status = True)

        hash_links = {}
        pending = len(query_links)
        link_for_row = 6 # 6 links por fila
        remaining = pending % link_for_row
        weight = link_for_row - remaining
        weight_insert = False
        count = 1
        for link in query_links:
            hash_current = {}
            hash_current['name'] = link.name
            hash_current['link'] = link.link
            hash_current['logo'] = link.logo
            hash_current['weight'] = 0

            if pending <= remaining and not weight_insert:
                hash_current_alt = {}
                hash_current_alt['weight'] = weight
                hash_links.update({count: hash_current_alt})
                count += 1
                weight_insert = True

            hash_links.update({count: hash_current})

            pending -= 1
            count += 1

        if weight_insert:
            hash_current_alt = {}
            hash_current_alt['weight'] = weight
            hash_links.update({count: hash_current_alt})

        context['context_links'] = hash_links

        # Papers context
        query_papers = Paper.objects.filter(status = True).order_by('-published')
        hash_papers_year = {}
        hash_years = {}
        hash_years_all = {}
        year_group = 0
        count = 0
        group = 0
        for paper in query_papers:
            if count == 0:
                hash_years.update({_('ALL'): len(query_papers)})

            _year = paper.published.year

            if _year != year_group and len(hash_years) == 4: # 4: debido que son 4 slides concurrentes
                hash_papers_year.update({group: hash_years})
                hash_years = {}
                group += 1

            if _year in hash_years:
                hash_years.update({_year: hash_years[_year] + 1})
            else:
                hash_years.update({_year: 1})
            year_group = _year
            count += 1

            if _year in hash_years_all:
                hash_years_all.update({_year: hash_years_all[_year] + 1})
            else:
                hash_years_all.update({_year: 1})

        if len(hash_years) > 0:
            hash_papers_year.update({group: hash_years})

        _hash_keys = list(reversed(list(hash_years_all.keys())))
        _hash_values = list(reversed(list(hash_years_all.values())))

        hash_papers_list = {'year': '|'.join(str(i) for i in _hash_keys),
                            'count': '|'.join(str(i) for i in _hash_values)}

        context['context_papers_year'] = hash_papers_year
        context['context_papers_list'] = hash_papers_list

        # Partnerships context
        query_partnerships_national = Partnership.objects\
                                                 .filter(status = True, institution__state__name__isnull = False)\
                                                 .distinct()\
                                                 .values('institution__state__id',
                                                         'institution__state__name',
                                                         'institution__state__code',
                                                         'institution__state__image',
                                                         'institution__country__id',
                                                         'institution__country__name',
                                                         'institution__country__code')\
                                                 .annotate(count=Count('institution__state__name'))\
                                                 .order_by('institution__state__name')

        query_partnerships_international = Partnership.objects\
                                                      .filter(~Q(institution__country__name = 'Brazil'), status = True)\
                                                      .distinct()\
                                                      .values('institution__country__id',
                                                              'institution__country__name',
                                                              'institution__country__code')\
                                                      .annotate(count=Count('institution__country__name'))\
                                                      .order_by('institution__country__name')

        hash_partnerships_detail = {}
        for item in query_partnerships_national:
            state_id = item['institution__state__id']
            hash_current = {}
            hash_current['state_id'] = state_id
            hash_current['state_name'] = item['institution__state__name']
            hash_current['state_code'] = item['institution__state__code']
            hash_current['state_image'] = item['institution__state__image']
            hash_current['country_id'] = item['institution__country__id']
            hash_current['country_name'] = item['institution__country__name']
            hash_current['country_code'] = item['institution__country__code']
            hash_current['partnerships_count'] = item['count']
            hash_partnerships_detail.update({state_id: hash_current})

        hash_partnerships_international = {}
        for item in query_partnerships_international:
            state_id = item['institution__country__id']
            hash_current = {}
            hash_current['country_id'] = state_id
            hash_current['country_name'] = item['institution__country__name']
            hash_current['country_code'] = item['institution__country__code']
            # hash_current['country_code'] = "img/flags/countries/%s.png" % (str(item['institution__country__code']).lower())
            hash_current['partnerships_count'] = item['count']
            hash_partnerships_international.update({state_id: hash_current})

        if len(hash_partnerships_international) > 0:
            hash_partnerships_detail.update({0: hash_partnerships_international})

        query_partnerships = Partnership.objects.filter(status = True) 
        hash_partnerships = {}
        hash_partnerships_inter = {}
        for partner in query_partnerships:
            hash_partnerships_current = {}
            hash_partnerships_current['partner_id'] = partner.id
            hash_partnerships_current['partner'] = "{first_name} {last_name}".format(first_name = partner.first_name, last_name = partner.last_name)
            hash_partnerships_current['degree'] = partner.degree.name
            hash_partnerships_current['link'] = partner.link
            hash_partnerships_current['country_id'] = partner.country.id
            hash_partnerships_current['country'] = partner.country.name
            hash_partnerships_current['country_code'] = partner.country.code
            # hash_partnerships_current['country_code'] = "img/flags/countries/%s.png" % (str(partner.country.code).lower())

            institution_id = partner.institution.id
            country_id = partner.institution.country.id
            hash_institution_current = {}
            hash_institution_current['institution_id'] = institution_id
            hash_institution_current['institution'] = partner.institution.full_name
            hash_institution_current['institution_name'] = partner.institution.name
            # hash_institution_current['institution_country_id'] = country_id
            # hash_institution_current['institution_country'] = partner.institution.country.name
            # hash_institution_current['institution_country_code'] = partner.institution.country.code

            if country_id == 30:
                # Brazil
                state_id = partner.institution.state.id
                #hash_institution_current['institution_state_id'] = state_id
                #hash_institution_current['institution_state'] = partner.institution.state.name
                #hash_institution_current['institution_state_code'] = partner.institution.state.code

                index = 0
                if state_id not in hash_partnerships:
                    hash_partnerships.update({state_id: {}})

                if institution_id in hash_partnerships[state_id]:
                    index = len(hash_partnerships[state_id][institution_id]['data'])
                else:
                    hash_partnerships[state_id].update({institution_id: hash_institution_current})
                    hash_partnerships[state_id][institution_id].update({'data': {}})

                hash_partnerships[state_id][institution_id]['data'].update({index: hash_partnerships_current})
            else:
                # International
                index = 0
                if country_id not in hash_partnerships_inter:
                    hash_partnerships_inter.update({country_id: {}})

                if institution_id in hash_partnerships_inter[country_id]:
                    index = len(hash_partnerships_inter[country_id][institution_id]['data'])
                else:
                    hash_partnerships_inter[country_id].update({institution_id: hash_institution_current})
                    hash_partnerships_inter[country_id][institution_id].update({'data': {}})

                hash_partnerships_inter[country_id][institution_id]['data'].update({index: hash_partnerships_current})

        if len(hash_partnerships_inter) > 0:
            hash_partnerships.update({0: hash_partnerships_inter})

        hash_partnerships_tmp = hash_partnerships_detail.copy()

        for item in hash_partnerships_tmp:
            if item == 0:
                partner_inter = hash_partnerships[item].copy()
                for key in partner_inter:
                    hash_partnerships_detail[item][key].update({'data': hash_partnerships[item][key]})
            else:
                hash_partnerships_detail[item].update({'data': hash_partnerships[item]})

        context['context_partnerships_national'] = query_partnerships_national
        context['context_partnerships_international'] = query_partnerships_international
        context['context_partnerships_detail'] = hash_partnerships_detail

        # News context
        query_news = News.objects.all().filter(status = True)[:4]
        context['context_news'] = query_news

        return context
