from django.db import models

# Create your models here.

class Team (models.Model):
    name = models.CharField(unique=False,max_length=50)
    
    def _unicode_(self):
        return U'%s %s' %(self.name)

class Player (models. Model):
    name = models.CharField(unique=True, max_length=50)
    number = models.CharField(unique=False, max_length=4)
    year = models.CharField(max_length=50)
    position = models.CharField(max_length=200)
    height = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    PPG = models.CharField(max_length=50)
    SPG = models.CharField(max_length=50)
    FTP = models.CharField(max_length=50);
    
    class Meta(object):
        verbose_name_plural = "Players"
        
    def __unicode__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Course, self).save(*args, **kwargs)