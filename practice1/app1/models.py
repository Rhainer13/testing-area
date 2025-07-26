from django.db import models

# Create your models here.
# class Model1(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return self.name
    
# class Model2(models.Model):
#     model1 = models.ForeignKey(Model1, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     content = models.TextField()

#     def __str__(self):
#         return self.title

# class Model3(models.Model):
#     model1 = models.ForeignKey(Model1, on_delete=models.CASCADE)
#     additional_info = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.model1.name} - {self.model2.title}"
    
class IncidentReport(models.Model):
    # Victim
    victim_name = models.CharField(max_length=100)
    victim_age = models.IntegerField()
    contact_number = models.CharField(max_length=20)

    # Incident
    incident_date = models.DateField()
    location = models.CharField(max_length=100)
    is_electronic = models.BooleanField(default=False)
    electronic_medium = models.CharField(max_length=255, blank=True, null=True)

    # Perpetrator
    perpetrator_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    description = models.TextField()