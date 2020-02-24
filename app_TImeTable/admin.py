from django.contrib import admin
from app_TImeTable.models import TimeTable
# Register your models here.


class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['time', 'subject', 'topics']


admin.site.register(TimeTable, TimeTableAdmin)