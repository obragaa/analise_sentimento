from django.contrib import admin
from .models import Frases
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class ListandoFrases(admin.ModelAdmin):
    list_filter = ("categoria",)
    list_display = ("texto", "resposta", "data_e_hora", "publicada")
    search_fields = ("resposta",)
    list_display_links = ("texto", "resposta")
    list_editable = ("publicada",)
    list_per_page = 10

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff']  # Adicione 'is_admin' para exibição na lista de usuários
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'groups']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active')}
        ),
    )
    search_fields = ['username', 'email']
    ordering = ['username']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Frases, ListandoFrases)
