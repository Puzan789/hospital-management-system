
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class doctor(models.Model):
    name = models.CharField(max_length=100)
    mobile = PhoneNumberField(blank=False)
    department = models.CharField(max_length=200)
    email=models.EmailField()

    def __str__(self):
        return self.name


class patient(models.Model):
    name = models.CharField(max_length=100)
    mobile = PhoneNumberField(blank=False)
    gender = (
        (
            "M",
            "Male",
        ),
        (
            "F",
            "Female",
        ),
        (
            "U",
            "Other",
        ),
    )
    sex = models.CharField(max_length=1, choices=gender)
    address = models.TextField()
    print(type(gender))

    def __str__(self):
        return self.name


class appointment(models.Model):
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.patient.name
    
