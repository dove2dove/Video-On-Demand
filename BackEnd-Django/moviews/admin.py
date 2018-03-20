from django.contrib import admin
from . models import General, SubscriptionPlan, Account, Category, Genres, Movies, Actors, Subscriptions, WatchList, WatchLog, Adverts

# Register your models here.
admin.site.register(General)
admin.site.register(SubscriptionPlan)
admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Genres)
admin.site.register(Movies)
admin.site.register(Actors)
admin.site.register(Subscriptions)
admin.site.register(WatchList)
admin.site.register(WatchLog)
admin.site.register(Adverts)