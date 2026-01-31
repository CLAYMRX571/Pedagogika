from django.db import models

class Home(models.Model):
    research_name = models.CharField(max_length=255)
    pedagogical_name = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)
    student_name = models.CharField(max_length=255)
    monitor_name = models.CharField(max_length=255)
    multimedia_name = models.CharField(max_length=255)
  
    def __str__(self):
        return self.research_name