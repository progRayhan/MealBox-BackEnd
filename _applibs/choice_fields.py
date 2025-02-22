from django.db import models


class Gender(models.TextChoices):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"


class EmployeeStatus(models.TextChoices):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"
