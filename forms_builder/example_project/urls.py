from __future__ import unicode_literals

try:
    from django.urls import re_path, include
except ImportError:
    # For Django 1.11 compatibility
    from django.conf.urls import url as re_path, include
from django.contrib import admin
from django.views.generic.list import ListView

from forms_builder.forms.models import Form
from forms_builder.forms import urls as form_urls


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^forms/', include(form_urls)),
    re_path(r'^$', ListView.as_view(model=Form,
        template_name='index.html')),
]
