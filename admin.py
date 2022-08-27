from django.contrib.admin import AdminSite


class PyBookAdminSite(AdminSite):
    title_header = 'PyBook Admin'
    site_header = 'PyBook Administration'
    index_title = 'PyBook Site Admin'
