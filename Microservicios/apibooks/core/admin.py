from django.contrib import admin
from .models import Student,Teacher,Course,Grade,Profile

admin.site.register([Student,Teacher,Course,Profile,Grade])
