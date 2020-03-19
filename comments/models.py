from django.db import models
from datetime import datetime 

# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    date = models.DateField(default=datetime.now, blank=True)
    author = models.CharField(max_length=50, default='')
    ticketID = models.IntegerField(default=0)

    def __str__(self):
        return 'Author: {0} | Date: {1} | Content: {2}'.format(self.author, self.date, self.content)