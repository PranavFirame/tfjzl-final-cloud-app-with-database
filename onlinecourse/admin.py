from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Course, Lesson, Question, Choice, Submission

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    show_change_link = True

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "course", "points", "order")
    list_filter = ("course",)
    inlines = [ChoiceInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order")
    list_filter = ("course",)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [QuestionInline]

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "score", "total_points", "submitted_at")
    readonly_fields = ("submitted_at",)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
