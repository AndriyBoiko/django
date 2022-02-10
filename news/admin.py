from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import News, Category


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    
    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id','title', 'category', 'created_at', 'upload_at', 'in_publisher', 'get_photo')
    list_display_links=('id','title')
    search_fields = ('title', 'content')
    list_editable = ('in_publisher',)
    list_filter = ('in_publisher', 'category')
    fields = ('title', 'category', 'content', 'photo', 'get_photo',  'in_publisher', 'views', 'created_at', 'upload_at'  )
    readonly_fields = ( 'get_photo', 'views', 'in_publisher','created_at', 'upload_at')
    save_on_top = True
    
    
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width = "50px">')
        else:
            return '-'
    get_photo.short_description = 'Фото'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links=('id','title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.site_title = 'Раз два'
admin.site.site_header = 'Adminka'
# Register your models here.
