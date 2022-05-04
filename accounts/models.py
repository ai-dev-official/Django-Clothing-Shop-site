from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone


class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
    ]
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE,  related_name="profile")
    image = models.ImageField(
        upload_to="accounts/profiles/", null=True, blank=True)
    first_name = models.CharField(
        max_length=15, default='', null=False, blank=False)
    last_name = models.CharField(
        max_length=15, default='', null=False, blank=False)
    email = models.EmailField(max_length=65, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=75, null=True, blank=True)
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    eircode = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=25, null=True, blank=True)
    county = models.CharField(max_length=25, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s' % self.user.username


User.accounts = property(lambda u: Profile.objects.get_or_create(user=u)[0])
