from django.db import models

class Incident(models.Model):

    PRIORITY_CHOICES = [
        ('Critical', 'P1 - Critical'),
        ('High', 'P2 - High'),
        ('Medium', 'P3 - Medium'),
        ('Low', 'P4 - Low'),
    ]

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('On Hold', 'On Hold'),
        ('Resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES
        # ❌ REMOVE default='Low'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Open'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title