from django.contrib import admin
from courses.models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','code','credits','department']
    search_fields = ['name','code']
    list_filter = ['department']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','department','enrollment_year']
    search_fields = ['first_name','last_name']
    list_filter = ['department','enrollment_year']

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student','course','enrollment_date','grade']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','head_of_dept','budget']

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Enrollment,EnrollmentAdmin)
admin.site.register(Student,StudentAdmin)














