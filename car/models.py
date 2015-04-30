from django.db import models


class Car(models.Model):
    description = models.TextField()
    engine = models.CharField(max_length=30)
    year = models.IntegerField()
    make = models.CharField(max_length=20)
    owner = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos', blank=True)

    def __repr__(self):
        return '<Car: %s, %s, %s, %s, %s, %s, %s>' % (self.id,
                                                  self.description,
                                                  self.engine,
                                                  self.year,
                                                  self.make,
                                                  self.owner,
                                                  self.photo.name)