from django.db import models
from _applibs.validators import PHONE_REGEX
from _applibs.choice_fields import Gender, EmployeeStatus


class Employee(models.Model):
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

    def __str__(self):
        return self.phone_number
    
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employes"
        db_table = "employee"
