from django.contrib import admin
from django.contrib.admin import ModelAdmin

from pypro.turmas.models import Turma


@admin.register(Turma)
class TurmaAdmin(ModelAdmin):
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('-inicio',)
