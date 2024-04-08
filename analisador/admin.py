from django.contrib import admin
from .models import Frases

class ListandoFrases(admin.ModelAdmin):
    list_filter = ("categoria",)
    list_display = ("texto", "resposta", "data_e_hora", "publicada")
    search_fields = ("resposta",)
    list_display_links = ("texto", "resposta")
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Frases, ListandoFrases)
