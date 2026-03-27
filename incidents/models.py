from django.db import models

class Incident(models.Model):

    PRIORITY_CHOICES = [
        ('P1', 'Critical'),
        ('P2', 'High'),
        ('P3', 'Medium'),
        ('P4', 'Low'),
    ]

    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('RESOLVED', 'Resolved'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    reported_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default='P3')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')

    def __str__(self):
        return self.title