from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from .managers import *

# ----------------------------------------------------------------------------------------------------------------------------
class User(AbstractBaseUser):
    phoneNumber = models.CharField(unique=True, max_length=11)
    firstName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    Avatar = models.ImageField(upload_to="images/Avatar",blank=True,null=True)

    code = models.IntegerField(blank=True,null=True)



    USERNAME_FIELD = 'phoneNumber'
    objects = MyUserManager()

    def __str__(self):
        return str(self.phoneNumber) + " - " + str(self.firstName) + " " + str(self.lastName)

    def full_name(self):
        return str(self.firstName) + " " + str(self.lastName)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.is_admin
# ----------------------------------------------------------------------------------------------------------------------------
