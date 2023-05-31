from .models import Employee, User, Shift
from faker import Faker
import random
from django.db import IntegrityError

fake = Faker()

for _ in range(100):
    full_name = fake.name()

    user = User.objects.create_user(name=full_name)
    
    employee = Employee.objects.create(user=user)

    
    shift_start = random.choice([0,8,16])
    try:

        shift = Shift.objects.create(employee=employee, shift_start=shift_start)
    except IntegrityError:
        pass