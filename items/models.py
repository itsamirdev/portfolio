from django.db import models


# Create your models here.


class BaseModel(models.Model):
    is_main_setting = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ItemBox(BaseModel, models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.title


class About(BaseModel, models.Model):
    main_text = models.TextField()


class Project(BaseModel, models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to="media/")
    url = models.URLField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    is_read_by_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
