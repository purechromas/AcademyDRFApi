from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import User


class TestCourseEndPoints(APITestCase):
    def setUp(self):
        # Creating a user
        user = User.objects.create(email='test@gmail.com')
        # Hash the password
        user.set_password('test')
        # Saving the user
        user.save()
        # Taking token url:
        get_token_url = reverse('users:token_obtain_pair')
        # Sending a post request for access and refresh token
        resp_token = self.client.post(
            path=get_token_url, data={'email': 'test@gmail.com', 'password': 'test'})
        # Taking the access token
        token = resp_token.json().get('access')
        # Adding {'authorization': 'token'} in HEADER
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        # Create a course
        self.client.post(reverse('courses:course_create'),
                         {'name': 'Course Test', 'description': 'test'})

    def test_course_create_endpoint(self):
        course_create_url = reverse('courses:course_create')
        course_data = {'name': 'Course Test1', 'description': 'test1'}
        response = self.client.post(course_create_url, course_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_course_list_endpoint(self):
        course_list_url = reverse('courses:course_list')
        response = self.client.get(course_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.json().get('results')), 1)

    def test_course_retrieve_endpoint(self):
        list_response = self.client.get(reverse('courses:course_list'))
        retrieve_pk = list_response.json()['results'][0]['id']
        course_retrieve_url = reverse('courses:course_retrieve', kwargs={'pk': retrieve_pk})
        response = self.client.get(course_retrieve_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_update_endpoint(self):
        list_response = self.client.get(reverse('courses:course_list'))
        update_pk = list_response.json()['results'][0]['id']
        path = reverse('courses:course_update', kwargs={'pk': update_pk})
        response = self.client.put(path=path, data={'name': 'Course Test2', 'description': 'test2'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['description'], 'test2')

    def test_course_delete_endpoint(self):
        list_response = self.client.get(reverse('courses:course_list'))
        delete_pk = list_response.json()['results'][0]['id']
        course_delete_url = reverse('courses:course_destroy', kwargs={'pk': delete_pk})
        response = self.client.delete(course_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def tearDown(self):
        return super().tearDown()
