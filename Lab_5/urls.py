from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import include, re_path
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path('i18n/', include('django.conf.urls.i18n')),
    re_path(r'^', include('polls.urls')),

]
