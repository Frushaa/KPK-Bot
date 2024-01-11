from django.contrib import admin
from Roleplay.models import Person, Course, Grade
from .models import Profile 
from .forms import ProfileForm
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    form = ProfileForm