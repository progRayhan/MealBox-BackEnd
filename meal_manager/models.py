from django.db import models
from meal_user.models import Staff
from _applibs.validators import PHONE_REGEX
from _applibs.choice_fields import PaymentStatus, DeliverStatus
from meal_user.models import Employee


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


class MealTracker(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, related_name="meal_tracker_staff")
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name="meal_tracker_employee")
    order_datetime = models.DateTimeField()
    payment_status = models.CharField(
        max_length=10, choices=PaymentStatus.choices, default=PaymentStatus.PENDING
    )
    meal_rate = models.ForeignKey(MealRate, on_delete=models.DO_NOTHING, related_name="meal_tracker_meal_rate")
    deliver_status = models.CharField(
        max_length=10, choices=DeliverStatus.choices, default=DeliverStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.deliver_status

    class Meta:
        verbose_name = "Meal Tracker"
        verbose_name_plural = "Meal Trackers"
        db_table = "meal_tracker"
