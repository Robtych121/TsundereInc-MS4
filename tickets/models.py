from django.db import models

# Create your models here.
class Ticket(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    date = models.DateField()
    status = models.CharField(max_length=50, default='')
    priority = models.CharField(max_length=50, default='')
    upvotes = models.IntegerField(blank=False)
    views = models.IntegerField(blank=False)

    def __str__(self):
        return '{0} - Priority: {1} | Status: {2}'.format(self.name, self.priority, self.status)