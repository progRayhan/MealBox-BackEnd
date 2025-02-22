from django.db import models
from meal_user.models import Staff
from _applibs.validators import PHONE_REGEX


class MealRate(models.Model):
    vendor_name = models.CharField(max_length=100)
    vendor_phone = models.CharField(max_length=11, validators=[PHONE_REGEX], unique=True, null=True, blank=True)
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, related_name="staff")
    meal_rate = models.PositiveIntegerField()

    def __str__(self):
        return self.vendor_name
    
    class Meta:
        verbose_name = "Meal Rate"
        verbose_name_plural = "Meal Rates"
        db_table = "meal_rate"
