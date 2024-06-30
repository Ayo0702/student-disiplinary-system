from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Student(models.Model):
    name = models.CharField(max_length=100, null=False)
    matric_no = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.matric_no})"

class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes', null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return f"Note {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

class Offense(models.Model):
    class Status(models.TextChoices):
        PENDING_STATEMENT = 'PENDING_STATEMENT', 'Pending Statement'
        REPORT_WRITTEN = 'REPORT_WRITTEN', 'Report Written'
        UNDER_INVESTIGATION = 'UNDER_INVESTIGATION', 'Under Investigation'
        RESOLVED = 'RESOLVED', 'Resolved'
        RECOMMENDATION = 'RECOMMENDATION', 'Recommendation'

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='offenses', null=False)
    statement = models.TextField()
    conclusion = models.TextField(blank=True)
    notes = models.ManyToManyField(Note, related_name='offenses', blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING_STATEMENT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Offense {self.id} - {self.student.matric_no}"
