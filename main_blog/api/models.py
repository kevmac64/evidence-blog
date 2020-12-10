from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(null=False, max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(null=False, default=True)

    def __str__(self):
        return f"{self.title} - {self.author} -> ({self.last_update})"


class Person(models.Model):
    name = models.CharField(null=False, max_length=255)
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.title})"

"""
class Evidence(models.Model):
    title = models.CharField(null=False, max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    disproved = models.BooleanField(default=False)
    sworn = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} Sworn({self.sworn})"


class Strand(models.Model):
    title = models.CharField(null=False, max_length=255)
    remarks = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class Tag(models.Model):
    title = models.CharField(null=False, max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

"""
