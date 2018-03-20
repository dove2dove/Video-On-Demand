from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import General, SubscriptionPlan, Account, Category, Genres, Movies, Subscriptions, WatchList, WatchLog, \
    Adverts, Actors, MovieGenreMap
from .serializers import GeneralSerializer, SubscriptionPlanSerializer, AccountSerializer, CategorySerializer, \
    GenresSerializer, MoviesSerializer, SubscriptionsSerializer, WatchListSerializer, WatchLogSerializer, \
    AdvertsSerializer, ActorsSerializer, movieGenreMapSerializer

# Create your views here.
class General_List(APIView):
    def get(self, request, format=None):
        allSetting = General.objects.all()
        serializer = GeneralSerializer(allSetting, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeneralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ======================================================
class General_Details(APIView):
    def get(self, request, pk, format=None):
        try:
            settings = General.objects.get(pk=pk)
            serializer = GeneralSerializer(settings)
            return Response(serializer.data)
        except General.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            settings = General.objects.get(pk=pk)
            serializer = GeneralSerializer(settings, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except General.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            settings = General.objects.get(pk=pk)
            settings.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except General.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ======================================================
class SubscriptionPlan_List(APIView):
    def get(self, request, format=None):
        allPlan = SubscriptionPlan.objects.all()
        serializer = SubscriptionPlanSerializer(allPlan, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubscriptionPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ======================================================
class SubscriptionPlan_Details(APIView):
    def get(self, request, pk, format=None):
        try:
            plans = SubscriptionPlan.objects.get(pk=pk)
            serializer = SubscriptionPlanSerializer(plans)
            return Response(serializer.data)
        except SubscriptionPlan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            plans = SubscriptionPlan.objects.get(pk=pk)
            serializer = SubscriptionPlanSerializer(plans, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except SubscriptionPlan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            plans = SubscriptionPlan.objects.get(pk=pk)
            plans.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SubscriptionPlan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ======================================================
class Account_List(APIView):
    def get(self, request, format=None):
        allAccount = Account.objects.all()
        serializer = AccountSerializer(allAccount, many=True)
        return Response(serializer.data)


def post(self, request, format=None):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ======================================================
class Account_Details(APIView):
    def get(self, request, pk, format=None):
        try:
            account = Account.objects.get(pk=pk)
            serializer = AccountSerializer(account)
            return Response(serializer.data)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            account = Account.objects.get(pk=pk)
            serializer = AccountSerializer(account, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            account = Account.objects.get(pk=pk)
            account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ======================================================
class Category_List(APIView):
    def get(self, request, format=None):
        allCategory = Category.objects.all()
        serializer = CategorySerializer(allCategory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ======================================================
class Category_Details(APIView):
    def get(self, request, pk, format=None):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ======================================================
class Genres_List(APIView):
    def get(self, request, format=None):
        allGenries = Genres.objects.all()
        serializer = GenresSerializer(allGenries, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GenresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ======================================================
class Genres_Details(APIView):
    def get(self, request, pk, format=None):
        try:
            genrie = Genres.objects.get(pk=pk)
            serializer = GenresSerializer(genrie)
            return Response(serializer.data)
        except Genres.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            genrie = Genres.objects.get(pk=pk)
            serializer = GenresSerializer(genrie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Genres.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            genrie = Genres.objects.get(pk=pk)
            genrie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Genres.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ======================================================
class Movies_List(APIView):
    def get(self, request, format=None):
        allMovies = Movies.objects.all()
        serializer = MoviesSerializer(allMovies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ======================================================
class Movies_Details(APIView):
    def get(self, request, pk, format=None):
        try:
            movies = Movies.objects.get(pk=pk)
            serializer = MoviesSerializer(movies)
            return Response(serializer.data)
        except Movies.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            movies = Movies.objects.get(pk=pk)
            serializer = MoviesSerializer(movies, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Movies.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            movies = Movies.objects.get(pk=pk)
            movies.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Movies.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ======================================================
class Subscriptions_List(APIView):
    def get(self, request, format=None):
        allSubscriptions = Subscriptions.objects.all()
        serializer = SubscriptionsSerializer(allSubscriptions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubscriptionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ======================================================
class Subscriptions_Details(APIView):
    def get(self, request, pk, format=None):
        try:
            subscriptions = Subscriptions.objects.get(pk=pk)
            serializer = SubscriptionsSerializer(subscriptions)
            return Response(serializer.data)
        except Subscriptions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            subscriptions = Subscriptions.objects.get(pk=pk)
            serializer = SubscriptionsSerializer(subscriptions, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Subscriptions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            subscriptions = Subscriptions.objects.get(pk=pk)
            subscriptions.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Subscriptions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ======================================================
class WatchList_List(APIView):
    def get(self, request, format=None):
        allWatch = WatchList.objects.all()
        serializer = WatchListSerializer(allWatch, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ======================================================
class WatchList_Details(APIView):
    def get(self, request, pk, format=None):
        try:
            watch = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(watch)
            return Response(serializer.data)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            watch = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(watch, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            watch = WatchList.objects.get(pk=pk)
            watch.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ======================================================
class WatchLog_List(APIView):
    def get(self, request, format=None):
        allWatchLog = WatchLog.objects.all()
        serializer = WatchLogSerializer(allWatchLog, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WatchLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ======================================================
class WatchLog_Details(APIView):
    def get(self, request, pk, format=None):
        try:
            watchLog = WatchLog.objects.get(pk=pk)
            serializer = WatchLogSerializer(watchLog)
            return Response(serializer.data)
        except WatchLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            watchLog = WatchLog.objects.get(pk=pk)
            serializer = WatchLogSerializer(watchLog, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except WatchLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            watchLog = WatchLog.objects.get(pk=pk)
            watchLog.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except WatchLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ======================================================
class Adverts_List(APIView):
    def get(self, request, format=None):
        allAdverts = Adverts.objects.all()
        serializer = AdvertsSerializer(allAdverts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdvertsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ======================================================
class Adverts_Details(APIView):
    def get(self, request, pk, format=None):
        try:
            adverts = Adverts.objects.get(pk=pk)
            serializer = AdvertsSerializer(adverts)
            return Response(serializer.data)
        except Adverts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            adverts = Adverts.objects.get(pk=pk)
            serializer = AdvertsSerializer(adverts, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Adverts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            adverts = Adverts.objects.get(pk=pk)
            adverts.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Adverts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ======================================================
class Actors_List(APIView):
    def get(self, request, format=None):
        allActors = Actors.objects.all()
        serializer = ActorsSerializer(allActors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ActorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ======================================================
class Actors_Details(APIView):
    def get(self, request, pk, format=None):
        try:
            actors = Actors.objects.get(pk=pk)
            serializer = ActorsSerializer(actors)
            return Response(serializer.data)
        except Actors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            actors = Actors.objects.get(pk=pk)
            serializer = ActorsSerializer(actors, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Actors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            actors = Actors.objects.get(pk=pk)
            actors.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Actors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ======================================================
class MovieGenreMap_List(APIView):
    def get(self, request, format=None):
        allMovieGenreMap = MovieGenreMap.objects.all()
        serializer = movieGenreMapSerializer(allMovieGenreMap, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = movieGenreMapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ======================================================
class MovieGenreMap_Details(APIView):
    def get(self, request, pk, format=None):
        try:
            movieGenreMap = MovieGenreMap.objects.get(pk=pk)
            serializer = movieGenreMapSerializer(movieGenreMap)
            return Response(serializer.data)
        except MovieGenreMap.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            movieGenreMap = MovieGenreMap.objects.get(pk=pk)
            serializer = movieGenreMapSerializer(movieGenreMap, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MovieGenreMap.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            movieGenreMap = MovieGenreMap.objects.get(pk=pk)
            movieGenreMap.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MovieGenreMap.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
# ======================================================