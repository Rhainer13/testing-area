from django.db import models

# Create your models here.
class Model1(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Model2(models.Model):
    model1 = models.ForeignKey(Model1, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Model3(models.Model):
    model1 = models.ForeignKey(Model1, on_delete=models.CASCADE)
    additional_info = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.model1.name} - {self.model2.title}"