from django.db import models

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    param = (
        ('false', u'物語は続く'),
        ('true', u'物語の終了')
    )
    is_finish = models.CharField(max_length=5, choices=param)
    def __str__(self):
        return self.title

class Storybone(models.Model):
    starttext = models.TextField(max_length=100)
    lasttext = models.TextField(max_length=100)

    def __str__(self):
        return self.starttext