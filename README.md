# Django Online Course Exam Project

A Django Online Course application implementing the final-project requirements:
- Question, Choice, Submission models
- Django Admin course/exam management
- Bootstrap course details page
- Exam submission and evaluation
- Exam result page with score and detailed results

## Run
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/

Create a Course, Lessons, Questions and Choices in the admin site, then take the exam.
