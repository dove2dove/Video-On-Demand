from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import logging

logger = logging.getLogger(__name__)
# Create your tests here.
class TestViewAPI(APITestCase):

    def test_MovieByCategory(self):
        url = reverse('Movie_Category_Type_List')
        response = self.client.get(url, {'Category': 2, 'Limiter': 8, 'MovieType': 'FM', 'ByRandom': True}, format='json')
        logger.info('Response from Movies : '+response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#/Users/dove/PycharmProjects/aviva/src/movie - path to movies
#/Users/dove/PycharmProjects/aviva/src/img/movies
#/Users/dove/PycharmProjects/aviva/src/img/genres
#/Users/dove/PycharmProjects/aviva/src/img/tv
#/Users/dove/PycharmProjects/aviva/src/img/kids