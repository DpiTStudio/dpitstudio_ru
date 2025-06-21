from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggitManager

class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    services = models.ManyToManyField(Service)
    client_name = models.CharField(max_length=200)
    project_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    tags = TaggitManager()

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = ProcessedImageField(
        upload_to='projects',
        processors=[ResizeToFill(1200, 800)],
        format='JPEG',
        options={'quality': 90}
    )
    caption = models.CharField(max_length=200, blank=True)
    is_main = models.BooleanField(default=False)

class Testimonial(models.Model):
    author = models.CharField(max_length=200)
    position = models.CharField(max_length=200, blank=True)
    content = RichTextField()
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.author}"

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextUploadingField()
    is_active = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title
