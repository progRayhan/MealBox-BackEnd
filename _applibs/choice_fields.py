from django.db import models


class Gender(models.TextChoices):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"


class EmployeeStatus(models.TextChoices):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"


class PaymentStatus(models.TextChoices):
    PAID = "PAID"
    PENDING = "PENDING"
    REFUND = "REFUND"


class DeliverStatus(models.TextChoices):
    PENDING = "PENDING"
    DELIVERED = "DELIVERED"
    CANCEL = "CANCEL"
    