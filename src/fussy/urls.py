from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView,PasswordResetView,LogoutView

from menus.views import HomeFeedView

from profiles.views import activateProfileView,ProfileFollowToggle,AnotherProfileToToggle,RegisterView
# from Profils.views import UserFollowToggle

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', TemplateView.as_view(template_name='home.html'),name="home"),
    url(r'^$', HomeFeedView.as_view(),name="home"),
    url(r'^contact/$',TemplateView.as_view(template_name='contact.html'),name="contact"),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^activation/(?P<code>[\w-]+)/$',activateProfileView,name='activate'),
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^logout/$',LogoutView.as_view(),name='logout'),
    url(r'^profile-follow/$',ProfileFollowToggle.as_view(),name='follow'),
    # url(r'^profile-folgen/$',AnotherProfileToToggle.as_view(),name='folgen'),
    # url(r'^profile-folgen/$',UserFollowToggle.as_view(),name='folgen'),
    url(r'^password/$',PasswordResetView.as_view(),name='password_reset'),
    url(r'^about/$',TemplateView.as_view(template_name='about.html'),name="about"),
    url(r'^restaurants/', include('restaurants.urls',namespace="restaurants")),
    url(r'^items/', include('menus.urls',namespace="menus")),
    url(r'^profile/', include('profiles.urls',namespace="profile")),

]
