from .models import LinkSocial

def get_links(request):
    context = {}
    links = LinkSocial.objects.filter(status = True)
    for link in links:
        context[link.key] = link.url
    return context
