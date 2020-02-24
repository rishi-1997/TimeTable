import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','TimeTable.settings')
import django
django.setup()

from app_TImeTable.models import *
from faker import Faker
from random import *
faker = Faker()

def populate(n):
    for i in range(n):
        time = faker.time()
        subject = faker.name()
        topics = faker.name()
        timetable_record = TimeTable.objects.get_or_create(time=time, subject=subject, topics=topics)

populate(10)