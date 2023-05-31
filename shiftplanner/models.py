from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    

class Shift(models.Model):
    shift_choices = (
        (0, '0-8'),
        (8, '8-16'),
        (16, '16-24'),
    )

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    shift_start = models.IntegerField(choices=shift_choices)

    def save(self, *args, **kwargs):
        """checks if the employee already has a shift. """
        if Shift.objects.filter(shift_start=self.shift_start, employee__user=self.employee.user).exists():
            raise ValueError("An employee can have only one shift per day.")
        
        super().save(*args, **kwargs) #saves the instance to ensure that an employee can only have one shift