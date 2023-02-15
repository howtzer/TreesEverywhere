from django.contrib import admin
from app.models import User, Account, PlantedTree

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = []


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('created', 'name', 'activate')
    search_fields = ['created', 'name', 'activate']


@admin.register(PlantedTree)
class PlantedTreeAdmin(admin.ModelAdmin):
    list_display = ('planted_at', 'user', 'account', 'tree')
    search_fields = ['planted_at', 'user', 'account', 'tree']

