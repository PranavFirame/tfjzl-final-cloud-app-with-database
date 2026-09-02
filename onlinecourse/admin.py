from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from .models import (
    Course,
    Lesson,
    Question,
    Choice,
    Submission,
    Instructor,
    Learner,
)


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


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("text", "question", "is_correct")
    list_filter = ("is_correct",)


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "course",
        "score",
        "total_points",
        "submitted_at",
    )
    readonly_fields = ("submitted_at",)


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("user",)


@admin.register(Learner)
class LearnerAdmin(admin.ModelAdmin):
    list_display = ("user",)


# Customize User administration
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Group is already registered by Django.
# Do NOT use admin.site.register(Group)
