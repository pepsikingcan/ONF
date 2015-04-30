from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from car.models import Car
from django.core.files.images import ImageFile


# Create your tests here.
class APITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.img = ImageFile(open('c:/temp/honda.jpg', 'rb'))

        self.data1 = {'id': 1,
                'description':'car1',
                'engine': '2.0L',
                'year':2015,
                'make':'Honda',
                'owner':'Chris',
                }
        photo_dict = {'photo': self.img}
        self.data1_p = dict(self.data1.items()|photo_dict.items())

        self.data2 = {'id': 2,
                'description':'car2',
                'engine': '2.0L',
                'year':2015,
                'make':'Bugatti',
                'owner':'Dan'
                }
        self.data2_p = dict(self.data2.items()|photo_dict.items())
        
        self.data1_u = {'id': 1,
                'description':'car1 updated',
                'engine': '3.0L',
                'year':2015,
                'make':'Honda',
                'owner':'Chris',
                }

    def test_no_cars(self):
        cars = Car.objects.all()
        self.assertEqual(len(cars), 0)

    def test_one_car(self):
        car1 = Car(description='car1',
                   engine='2L',
                   year=2015,
                   make='Honda',
                   owner='Chris',
                   photo=self.img)
        car1.save()
        cars = Car.objects.all()
        self.assertEqual(len(cars), 1)

    def test_get_empty_car_list(self):
        resp = self.client.get('/api/cars/')
        self.assertEqual(resp.data, [])

    def test_post_add_one_car(self):
        resp = self.client.post('/api/cars/', self.data1)
        cars = Car.objects.all()
        self.assertEqual(len(cars), 1)
        self.assertEqual(resp.data['id'], 1, 'bad id')
        self.assertEqual(resp.data['owner'], 'Chris', 'bad owner')
        self.assertEqual(status.HTTP_201_CREATED, resp.status_code)

    def test_post_add_one_car_with_photo(self):
        resp = self.client.post('/api/cars/', self.data1_p, format='multipart')
        cars = Car.objects.all()
        self.assertEqual(len(cars), 1)
        self.assertIn('jpg', resp.data['photo'], 'bad photo')
        self.assertEqual(status.HTTP_201_CREATED, resp.status_code)

    def test_post_add_two_cars(self):
        resp = self.client.post('/api/cars/', self.data1)
        resp = self.client.post('/api/cars/', self.data2)

        cars = Car.objects.all()
        self.assertEqual(len(cars), 2)
        self.assertEqual(status.HTTP_201_CREATED, resp.status_code)

    def test_get_one_car_with_photo(self):
        resp = self.client.post('/api/cars/', self.data1_p, format='multipart')
        resp = self.client.post('/api/cars/', self.data2)

        cars = Car.objects.all()
        self.assertEqual(len(cars), 2)

        resp = self.client.get('/api/cars/1')
        self.assertEqual(resp.data['id'], 1, 'bad id')
        
    def test_put_one_car_with_photo(self):
        resp = self.client.post('/api/cars/', self.data1_p, format='multipart')
        cars = Car.objects.all()
        self.assertEqual(len(cars), 1)
        
        resp = self.client.put('/api/cars/1', self.data1_u)
        self.assertEqual(resp.data['description'], 'car1 updated',
                         'bad update on description')
    
    def test_delete_one_car_with_photo(self):
        resp = self.client.post('/api/cars/', self.data1_p, format='multipart')
        cars = Car.objects.all()
        self.assertEqual(len(cars), 1)

        resp = self.client.delete('/api/cars/1')
        self.assertEqual(status.HTTP_204_NO_CONTENT, resp.status_code)
        cars = Car.objects.all()
        self.assertEqual(len(cars), 0)
#         self.assertEqual(resp.data['id'], 1, 'bad id')