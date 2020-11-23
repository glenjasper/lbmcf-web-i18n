from django.conf import settings

def global_settings(request):
    return {'VG_GROUP_REGULAR': settings.GROUP_REGULAR}
