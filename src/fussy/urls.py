from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView,PasswordResetView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'),name="home"),
    url(r'^contact/$',TemplateView.as_view(template_name='contact.html'),name="contact"),
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^password/$',PasswordResetView.as_view(),name='password_reset'),
    url(r'^about/$',TemplateView.as_view(template_name='about.html'),name="about"),
    url(r'^restaurants/', include('restaurants.urls',namespace="restaurants")),
    url(r'^items/', include('menus.urls',namespace="menus")),

]
