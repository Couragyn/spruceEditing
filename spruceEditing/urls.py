"""spruceEditing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.views.generic import TemplateView
from main.views import(
   contact_page,
   send_contact,
)

sitemaps = {
    "posts": PostSitemap,

}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='../templates/index.html'), name='index'),
    path('', include('blog.urls')),
    path('services/', TemplateView.as_view(template_name='../templates/services.html'), name='services'),
    path('testimonials/', TemplateView.as_view(template_name='../templates/testimonials.html'), name='testimonials'),
    path('editors/', TemplateView.as_view(template_name='../templates/editors.html'), name='editors'),
    path('summernote/', include('django_summernote.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    url(r'^contact/$', contact_page),
    url(r'^send-contact/$', send_contact),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
