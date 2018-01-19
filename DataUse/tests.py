from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse

from .models import DataPull_ID, DataPull_Detail, DataPull_Title, DataPull_Author, DataPull_Keyword
User = get_user_model()

class DataUseAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username='testsimon', email='sliu5@health.nyc.gov')
        user_obj.set_password('123456random')
        user_obj.save()

        #DataPull_ID
        pull_obj = DataPull_ID(pullname='NYC monthly pull',
                    pullquery='NYC Birth and Death Records',
                    pulltype='keyword',
                    pullsource='Pubmed',
                    pullby=user_obj)
        pull_obj.save()

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_datapull(self):
        pull_count = DataPull_ID.objects.count()
        self.assertEqual(pull_count, 1)

    def test_get_userlist(self):
        data = {}
        url = api_reverse('user-list')
        user = User.objects.get(username = 'testsimon')
        self.client.force_authenticate(user=user)
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_userlist(self):
        data = {'username': 'anothertestuser',
                'email': 'blah@blah.gov',
                'password': '1234random'}
        url = api_reverse('user-list')
        user = User.objects.get(username = 'testsimon')
        self.client.force_authenticate(user=user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_auth_user(self):
        # test if we need to be logged in to access this endpoint
        data = {}
        url = api_reverse('user-list')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_grouplist(self):
        data = {}
        url = api_reverse('group-list')
        user = User.objects.get(username = 'testsimon')
        self.client.force_authenticate(user=user)
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_grouplist(self):
        data = {}
        url = api_reverse('group-list')
        user = User.objects.get(username = 'testsimon')
        self.client.force_authenticate(user=user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_pulls(self):
        data = {}
        url = api_reverse('pull-list')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_pulls(self):
        data = {'pullname': 'NYC monthly pull 2',
                'pullquery': 'NYC Birth and Death Records',
                'pulltype': 'author',
                'pullsource': 'Pubmed',
                'pullby': 'testsimon'}
        url = api_reverse('pull-list')
        user = User.objects.first()
        self.client.force_authenticate(user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_model_relation(self):
        try:
            datapull_obj = DataPull_ID(pullname='another pull',
                                    pullquery='Nyc birth and death',
                                    pulltype='author',
                                    pullsource='pubmed',
                                    pullby='simon142414')
            datapull_obj.save()
        except Exception as e:
            print(e.args)

        self.assertEqual(DataPull_ID.objects.filter(pullname='another pull').count(), 0)

    def test_get_pull_detail_list(self):
        data = {}
        url = api_reverse('')