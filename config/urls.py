
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from tracker import views

urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.SignUpView.as_view(template_name="signup.html"), name='signup'),
    path('users/', include('django.contrib.auth.urls')),
    path('create_habit/', views.create_habit, name='create_habit'),
    path('habit/<slug:slug>/log/<int:pk>', views.log_entry, name='log_entry'), 
    path('habit/<slug:slug>', views.habit_detail, name='habit_detail'),
    path('api/log/<int:pk>', views.logapi),
    path('log_edit/<int:pk>', views.LogEdit.as_view(template_name="log_edit.html"), name='log_edit'),      
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
    SHOW_TOOLBAR_CALLBACK = True
