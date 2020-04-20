from django.db import models
from datetime import datetime 

# Create your models here.
class Forum(models.Model):
    name = models.CharField(max_length=254, default='')
    author = models.CharField(max_length=50, default='')
    description = models.TextField()
    date = models.DateField(default=datetime.now, blank=True)
    upvotes = models.IntegerField(blank=False, default=0)
    views = models.IntegerField(blank=False, default=0)
    points = models.IntegerField(blank=False, default=0)
    

    def __str__(self):
        return '{0} - Author: {1} | Date: {2}'.format(self.name, self.author, self.date)

class Comment(models.Model):
    content = models.TextField()
    date = models.DateField(default=datetime.now, blank=True)
    author = models.CharField(max_length=50, default='')
    ticketID = models.IntegerField(default=0)

    def __str__(self):
        return 'Author: {0} | Date: {1} | Content: {2}'.format(self.author, self.date, self.content)