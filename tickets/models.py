from django.db import models

# Create your models here.
class Ticket(models.Model):
    TYPE_CHOICES = [
        ('BUG', 'Bug'),
        ('FEATURE', 'Feature')
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='BUG',)
    name = models.CharField(max_length=254, default='')
    author = models.CharField(max_length=50, default='')
    description = models.TextField()
    date = models.DateField()
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('INPROGRESS', 'In Progress'),
        ('TESTING', 'Testing'),
        ('COMPLETED', 'Completed')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW',)
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('NORMAL', 'Normal'),
        ('HIGH', 'High')
    ]
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='LOW',)
    upvotes = models.IntegerField(blank=False, default=0)
    views = models.IntegerField(blank=False, default=0)
    points = models.IntegerField(blank=False, default=0)
    

    def __str__(self):
        return '{0} - Type: {1} | Priority: {2} | Status: {3}'.format(self.name, self.type, self.priority, self.status)