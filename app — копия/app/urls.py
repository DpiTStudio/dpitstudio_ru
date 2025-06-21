# from django.contrib import admin
# from django.urls import path

from main import views

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", views.index, name="index"),
#     path("about/", views.about, name="about"),
# ]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('', views.home, name='home'),
                  path('services/', views.service_list, name='service_list'),
                  path('services/<slug:slug>/', views.service_detail, name='service_detail'),
                  path('portfolio/', views.project_list, name='project_list'),
                  path('portfolio/<slug:slug>/', views.project_detail, name='project_detail'),
                  path('testimonials/', views.testimonial_list, name='testimonial_list'),
                  path('pages/<slug:slug>/', views.page_detail, name='page_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
