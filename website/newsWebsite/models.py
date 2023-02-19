import uuid
from django.db import models
from ckeditor.fields import RichTextField
# from multiselectfield import MultiSelectField


# Create your models here.


class Newsweb(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, blank=False, editable=False)
    temeHome = models.CharField(max_length=25555, null=False)
    temasport = models.CharField(max_length=25555, null=False)
    tematecnology = models.CharField(max_length=25555, null=False)
    temabusines = models.CharField(max_length=25555, null=False)
    temapolitic = models.CharField(max_length=25555, null=False)
    temahealth = models.CharField(max_length=25555, null=False)
    link = models.CharField(max_length=255, null=False)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', null=True)
    home = RichTextField()
    sportnNew = RichTextField()
    tecnologyNews = RichTextField()
    businessnews = RichTextField()
    politikNews = RichTextField()
    healthNews = RichTextField()
    newNews = RichTextField()

    def __str__(self):
        return self.temeHome
