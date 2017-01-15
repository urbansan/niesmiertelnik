from django.db import models
from django.utils import timezone

class BlogManager(models.Manager):
    def get_next_blog_post(self, blog_post):
        try:
            return self.get_queryset().filter(blog=blog_post.blog, date__gt=blog_post.date).order_by('date').first()
        except blogPost.DoesNotExist:
            return None

    def get_previous_blog_post(self, blog_post):
        try:
            return self.get_queryset().filter(blog=blog_post.blog, date__lt=blog_post.date).order_by('date').last()
        except blogPost.DoesNotExist:
            return None

class blogPost(models.Model):
    blog_types = (
        ('it', 'it'),
        ('moto', 'moto'),
        ('climbing', 'climbing'),
        ('guitar', 'guitar'),
        ('blob', 'blob'),
    )
    blog = models.CharField(max_length=8, choices=blog_types, default='blob')
    title = models.CharField(max_length = 140)
    article_link = models.CharField(unique = True, max_length = 40, default = '#')
    author = models.CharField(max_length = 40)
    author_link = models.TextField(default = '#')
    body = models.TextField()
    date = models.DateTimeField(default = timezone.now)
    views_count = models.IntegerField(default = 0)

    objects = BlogManager()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Wpis"
        verbose_name_plural = "Wpisy"


