from django.db import models
from django.contrib.auth.models import User, UserManager
from django.utils.translation import gettext_lazy as _


BATCH = [
    ("1", "1st Year"),
    ("2", "2nd Year"),
    ("3", "3rd Year"),
    ("4", "4th Year"),
    ("5", "5th Year"),
]

class College(models.Model):
    name = models.CharField(_("College Name"), max_length=256, unique=True)
    ar_name = models.CharField(_("College Name"), max_length=256, unique=True)
    contact = models.CharField(_("College Registeration Office Contact Number"), max_length=16)
    location = models.TextField(_("College Location"))
    description = models.TextField(_("College Description"))
    ar_description = models.TextField(_("College Description"))
    batch = models.CharField(max_length=1, choices=BATCH)

    def __str__(self):
        return self.name + " | "+ self.ar_name
    

class Anouncement(models.Model):
    title = models.CharField(max_length=256)
    ar_title = models.CharField(max_length=256)
    body = models.TextField()
    ar_body = models.TextField()
    created = models.DateTimeField(_("Added at"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated at"), auto_now=True)
    date = models.DateTimeField(_("Announcement Date"), null=True)
    college = models.ForeignKey('college.College', verbose_name=_("College"), on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " | " + self.ar_title

