from django.db import models


class Timeslot(models.Model):
    dentist = models.TextField()
    startTime = models.TextField()
    date = models.DateField()
    status = models.TextField(choices=[('available', 'Available'), ('reserved', 'Reserved')])

    def __str__(self):
        return f'{self.startTime} o\'clock on {self.date} with {self.dentist} is {self.status}'
