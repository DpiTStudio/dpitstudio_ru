# from django.contrib import admin
#
# # Register your models here.
from django.contrib import admin
from .models import Service, Project, ProjectImage, Testimonial, Page
from django.utils.html import format_html
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class ServiceAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Service
        fields = '__all__'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    list_display = ('title', 'price', 'is_active', 'order')
    list_editable = ('price', 'is_active', 'order')
    prepopulated_fields = {'slug': ('title',)}

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return format_html('<img src="{}" height="100" />', obj.image.url) if obj.image else "-"
    image_preview.short_description = "Превью"

class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Project
        fields = '__all__'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    inlines = [ProjectImageInline]
    list_display = ('title', 'client_name', 'project_date', 'is_featured')
    list_filter = ('services', 'is_featured')
    filter_horizontal = ('services',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'position', 'project', 'service', 'is_active')
    list_filter = ('is_active', 'project', 'service')
    search_fields = ('author', 'content')

class PageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Page
        fields = '__all__'

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm
    list_display = ('title', 'slug', 'is_active')
    list_editable = ('is_active',)
    prepopulated_fields = {'slug': ('title',)}
