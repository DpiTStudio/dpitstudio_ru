# from django.http import HttpResponse
# from django.shortcuts import render
#
#
# def index(request):
#     con_text = {
#         "title": "Главная страница сайта DPITSTUDIO",
#         "content": "Добро пожаловать на главную страницу нашего сайта. Здесь вы можете найти информацию о нашем проекте и наших услугах. Если у вас есть какие-либо вопросы или пожелания, пожалуйста, свяжитесь с нами. Мы будем рады помочь вам.",
#         "is_aut": True,
#     }
#     return render(request, "main/index.html", context=con_text)
#
#
# def about(request):
#     con_text = {
#         "title": "Страница о нас DPITSTUDIO",
#         "content": "Истоия нас и наши услуги",
#         "is_aut": True,
#     }
#     return render(request, "main/about.html", context=con_text)


from django.shortcuts import render, get_object_or_404
from .models import Page, Service, Project, Testimonial

def home(request):
    services = Service.objects.filter(is_active=True).order_by('order')[:6]
    featured_projects = Project.objects.filter(is_featured=True)
    testimonials = Testimonial.objects.filter(is_active=True)

    context = {
        'services': services,
        'featured_projects': featured_projects,
        'testimonials': testimonials,
    }
    return render(request, 'portfolio/home.html', context)

def service_list(request):
    services = Service.objects.filter(is_active=True).order_by('order')
    return render(request, 'portfolio/service_list.html', {'services': services})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    related_projects = Project.objects.filter(services=service)
    testimonials = Testimonial.objects.filter(service=service, is_active=True)

    context = {
        'service': service,
        'related_projects': related_projects,
        'testimonials': testimonials,
    }
    return render(request, 'portfolio/service_detail.html', context)

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def testimonial_list(request):
    testimonials = Testimonial.objects.filter(is_active=True)
    return render(request, 'portfolio/testimonial_list.html', {'testimonials': testimonials})

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'portfolio/page.html', {'page': page})
