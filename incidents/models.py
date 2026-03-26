from django.db import models


class Incident(models.Model):
    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES,
        default='Low'
    )
    location = models.CharField(max_length=200)
    reported_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.severity})"