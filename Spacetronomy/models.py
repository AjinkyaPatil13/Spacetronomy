from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content_1 = models.TextField()
    image_1 = models.ImageField(null=True, blank=True, upload_to="images/")
    content_2 = models.TextField(null = True, blank= True)
    image_2 = models.ImageField(null=True, blank=True, upload_to="images/")
    content_3= models.TextField(null=True, blank=True)
    image_3 = models.ImageField(null=True, blank=True, upload_to="images/")
    content_4=models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
   

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Contact(models.Model):
    name    = models.CharField(max_length=100, null="True")
    email   = models.EmailField(max_length=213, default="name@example.com", null="True")
    phone   = models.CharField(max_length=12, null="True")
    message = models.TextField(null="True")

    def __str__(self):
        return self.name
