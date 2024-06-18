from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from shop.models import Products

admin.site.register(Application)


class ProductsAdminForm(forms.ModelForm):
    content = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Products
        fields = '__all__'


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at', 'content')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    prepopulated_fields = {"slug": ("title",)}
    form = ProductsAdminForm


admin.site.register(Products, ProductsAdmin)


