from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .models import Course, Submission

def course_list(request):
    courses = Course.objects.all()
    return render(request, "course_list.html", {"courses": courses})

def course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, "course_details_bootstrap.html", {"course": course})

def submit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method != "POST":
        return redirect("course_details", course_id=course.id)

    questions = course.questions.prefetch_related("choices").all()
    total_points = sum(q.points for q in questions)
    score = 0

    for question in questions:
        selected_id = request.POST.get(f"question_{question.id}")
        if selected_id:
            choice = question.choices.filter(id=selected_id).first()
            if choice and choice.is_correct:
                score += question.points

    user = request.user if request.user.is_authenticated else None
    submission = Submission.objects.create(
        user=user, course=course, score=score, total_points=total_points
    )
    return redirect("show_exam_result", submission_id=submission.id)

def show_exam_result(request, submission_id):
    submission = get_object_or_404(
        Submission.objects.select_related("course"), id=submission_id
    )
    questions = submission.course.questions.prefetch_related("choices").all()
    results = []
    for question in questions:
        selected_id = request.GET.get(f"q{question.id}")
        correct = question.choices.filter(is_correct=True).first()
        results.append({
            "question": question,
            "correct": correct,
            "selected_id": selected_id,
        })
    return render(request, "exam_result.html", {
        "submission": submission,
        "results": results,
    })
