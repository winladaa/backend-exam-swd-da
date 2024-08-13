# apis/tests.py
from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework import status
from apis.models import School, Classroom, Teacher, Student

class SchoolTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create schools
        self.school1 = School.objects.create(
            name='Sunshine High School',
            abbreviation='SHS',
            address='123 Sunshine Avenue'
        )
        self.school2 = School.objects.create(
            name='Rainbow Academy',
            abbreviation='RA',
            address='456 Rainbow Road'
        )

    def test_list_schools(self):
        response = self.client.get('/api/v1/schools/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')

    def test_create_school(self):
        response = self.client.post('/api/v1/schools/', data={
            'name': 'Test School',
            'abbreviation': 'TS',
            'address': '123 Test St.'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'success')