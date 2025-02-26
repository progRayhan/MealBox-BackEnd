from django.db import models
from _applibs.validators import PHONE_REGEX
from _applibs.choice_fields import Gender, EmployeeStatus

from django.contrib.auth.models import AbstractBaseUser, AbstractUser


from django.contrib.auth.models import BaseUserManager



class StaffBaseUserManager(BaseUserManager):

    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Username field is required")
        if email:
            email = self.normalize_email(email)
        user = self.model(phone_number=phone_number,email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(phone_number, email, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})


class Staff(AbstractBaseUser):
    phone_number = models.CharField(max_length=11, validators=[PHONE_REGEX], unique=True)
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    office = models.CharField(max_length=200)
    office_address = models.TextField()
    total_sales = models.PositiveIntegerField(default=0)
    order_completed = models.PositiveIntegerField(default=0)
    total_employee = models.PositiveIntegerField(default=0)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    def __str__(self):
        return self.phone_number

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["email"]

    objects = StaffBaseUserManager()

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staffs"
        db_table = "staff"

    def has_perm(self, perm, obj=None):
        if self.is_staff and self.is_active and not self.is_superuser:
            return super().has_perm(perm, obj)
        return True

    def has_module_perms(self, app_label):
        if self.is_staff and self.is_active and not self.is_superuser:
            return super().has_module_perms(app_label)
        return True




class EmployeeBaseUserManager(models.Manager):

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})



class Employee(AbstractBaseUser):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, validators=[PHONE_REGEX], unique=True)
    email = models.EmailField(max_length=100, unique=True)
    gender = models.CharField(
        max_length=10, choices=Gender.choices, default=Gender.MALE, null=True, blank=True
    )
    office = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(
        max_length=10, choices=EmployeeStatus.choices, default=EmployeeStatus.ACTIVE
    )
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, related_name="staff")

    def __str__(self):
        return self.phone_number

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = EmployeeBaseUserManager()
    
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employes"
        db_table = "employee"

