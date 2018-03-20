from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
import logging
import random
import ast
from moviews.models import General, SubscriptionPlan, Account, Category, Genres, Movies, Subscriptions, WatchList, WatchLog, \
    Adverts, Actors
from moviews.serializers import GeneralSerializer, SubscriptionPlanSerializer, AccountSerializer, CategorySerializer, \
    GenresSerializer, MoviesSerializer, SubscriptionsSerializer, WatchListSerializer, WatchLogSerializer, \
    AdvertsSerializer, ActorsSerializer
from django.db.models import Q

logger = logging.getLogger(__name__)
# Create your views here.
class MovieByCategoryAndType(APIView):
    def get(self, request, format=None):
        category = self.request.query_params.get('Category', None)
        limiter = self.request.query_params.get('Limiter', None)
        movieType = self.request.query_params.get('MovieType', None)
        byRandom = self.request.query_params.get('ByRandom', None)
        logger.info('Parameters : , ' + category + ', ' + movieType + ', ' + str(limiter) + ', ' + byRandom)
        cat_list = Category.objects.all()
        cat_id = 0
        limits = int(limiter)
        isRandom = ast.literal_eval(byRandom)
        for catrec in cat_list:
            if catrec.Name.strip().upper() == category.strip().upper():
                cat_id = catrec.id
                break
        if cat_id != 0 and movieType is not None:
            logger.info('Parameter checks was Okay')
            try:
                data_pool = list(Movies.objects.filter(Q(category__exact=cat_id) & Q(Type__exact=movieType)))
                if isRandom:
                    logger.info('There was a shuffle')
                    random.shuffle(data_pool)
                if limits > 0:
                    movielist = data_pool[:limits]
                else:
                    movielist = data_pool
                mov_serializer = MoviesSerializer(movielist, many=True)
                return Response(mov_serializer.data)
            except General.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)