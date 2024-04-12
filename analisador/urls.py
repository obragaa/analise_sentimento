from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('analise/', views.home, name='analise_sentimento'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('other-admin-action/', views.other_admin_action, name='other_admin_action'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
