from rest_framework import serializers
from . models import General, SubscriptionPlan, Account, Category, Genres, Movies, Subscriptions, WatchList, WatchLog, Adverts, Actors, MovieGenreMap

class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields= '__all__'


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    subscriptionPlan = SubscriptionPlanSerializer()
    class Meta:
        model = Account
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'


class MoviesSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Movies
        fields = '__all__'

class SubscriptionsSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    category = CategorySerializer()
    class Meta:
        model = Subscriptions
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    movie = MoviesSerializer()
    class Meta:
        model = WatchList
        fields = '__all__'

class WatchLogSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    movie = MoviesSerializer()
    class Meta:
        model = WatchLog
        fields = '__all__'

class AdvertsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Adverts
        fields = '__all__'

class ActorsSerializer(serializers.ModelSerializer):
    movie = MoviesSerializer()
    class Meta:
        model = Actors
        fields = '__all__'

class movieGenreMapSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    movie = MoviesSerializer()
    class Meta:
        model = MovieGenreMap
        fields = '__all__'