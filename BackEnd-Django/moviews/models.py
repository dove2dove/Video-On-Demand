from django.db import models


# Create your models here.
class General(models.Model):
    Organisation = models.CharField(max_length=100, null=False, blank=False)
    MoviePathType = models.CharField(max_length=25, null=False, blank=False, default='Local')
    LogoPath = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        # return "<Employee: {} {}>".format(self.first_name, self.last_name)
        return str(self.id) + ', ' + self.Organisation + ', ' + self.MoviePathType


class SubscriptionPlan(models.Model):
    Name = models.CharField(max_length=50, null=False, blank=False)
    Details = models.TextField(max_length=2000, null=True, blank=True)
    InitialFreedays = models.IntegerField(default=0)
    Price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    FeatureAddOns = models.CharField(max_length=50, null=True, blank=True)
    PremiumAddOns = models.CharField(max_length=50, null=True, blank=True)
    RenewFrequency = models.CharField(max_length=25, null=True, blank=True)
    Categories = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id) + ', ' + self.Name + ', ' + str(self.Price)


class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    subscriptionPlan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    LoginNameEmail = models.CharField(max_length=100, null=False, blank=False)
    Passwd = models.CharField(max_length=100, null=True, blank=True)
    Role = models.CharField(max_length=25, null=False, blank=False)
    Enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id) + ', ' + self.LoginNameEmail + ', ' + self.Role


class Category(models.Model):
    Name = models.CharField(max_length=50, null=False, blank=False)
    Details = models.CharField(max_length=100, null=True, blank=True)
    IndexOrder = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + ', ' + self.Name + ', ' + self.Details


class Genres(models.Model):
    TV = 'TV'
    MOVIES = 'MV'
    BOTH = 'BT'
    CATEGORY_TYPE = (
        (TV, 'Tv'),
        (MOVIES, 'Movies'),
        (BOTH, 'Both'),
    )
    Name = models.CharField(max_length=50, null=False, blank=False)
    Details = models.CharField(max_length=500, null=True, blank=True)
    displayphoto = models.CharField(max_length=100, null=True, blank=True)
    categoryType = models.CharField(max_length=25, null=True, blank=True, choices=CATEGORY_TYPE, default=BOTH)

    def __str__(self):
        return str(self.id) + ', ' + self.Name + ', ' + self.Details


class Movies(models.Model):
    FULLMOVIE = 'FM'
    TRAILER = 'TR'
    SHORTMOVIE = 'SM'
    MOVIE_TYPE = (
        (FULLMOVIE, 'FullMovie'),
        (TRAILER, 'Trailer'),
        (SHORTMOVIE, 'ShortMovie'),
    )
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    Name = models.CharField(max_length=50, null=False, blank=False)
    Details = models.TextField(max_length=1000, null=True, blank=True)
    ShortDetails = models.CharField(max_length=500, null=True, blank=True)
    BigPicture = models.CharField(max_length=100, null=True, blank=True)
    mediumPicture = models.CharField(max_length=100, null=True, blank=True)
    SmallPicture = models.CharField(max_length=100, null=True, blank=True)
    ReleaseDate = models.DateTimeField('Date Released')
    Duration = models.BigIntegerField(default=0)
    Season = models.IntegerField(default=0)
    Episode = models.IntegerField(default=0)
    ViewersRestriction = models.CharField(max_length=25, null=True, blank=True)
    Rating = models.FloatField(default=0.0)
    Producers = models.CharField(max_length=100, null=True, blank=True)
    Directors = models.CharField(max_length=100, null=True, blank=True)
    MoviePathLocal = models.CharField(max_length=100, null=True, blank=True)
    MoviePathCloud = models.CharField(max_length=100, null=True, blank=True)
    Type = models.CharField(max_length=25, null=True, blank=True, choices=MOVIE_TYPE, default=FULLMOVIE)
    # Full-Movie, Trailer, Short-Movie
    LanguageCC = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return str(self.id) + ', ' + self.Name + ', ' + str(self.ReleaseDate)


class SubMovies(models.Model):
    FULLMOVIE = 'FM'
    TRAILER = 'TR'
    SHORTMOVIE = 'SM'
    MOVIE_TYPE = (
        (FULLMOVIE, 'FullMovie'),
        (TRAILER, 'Trailer'),
        (SHORTMOVIE, 'ShortMovie'),
    )
    id = models.BigAutoField(primary_key=True)
    movie = models.ForeignKey(Movies, on_delete=models.DO_NOTHING)
    Name = models.CharField(max_length=50, null=False, blank=False)
    Details = models.TextField(max_length=1000, null=True, blank=True)
    ShortDetails = models.CharField(max_length=500, null=True, blank=True)
    BigPicture = models.CharField(max_length=100, null=True, blank=True)
    mediumPicture = models.CharField(max_length=100, null=True, blank=True)
    SmallPicture = models.CharField(max_length=100, null=True, blank=True)
    ReleaseDate = models.DateTimeField('Date Released')
    Duration = models.BigIntegerField(default=0)
    Season = models.IntegerField(default=0)
    Episode = models.IntegerField(default=0)
    ViewersRestriction = models.CharField(max_length=25, null=True, blank=True)
    Rating = models.FloatField(default=0.0)
    Producers = models.CharField(max_length=100, null=True, blank=True)
    Directors = models.CharField(max_length=100, null=True, blank=True)
    MoviePathLocal = models.CharField(max_length=100, null=True, blank=True)
    MoviePathCloud = models.CharField(max_length=100, null=True, blank=True)
    Type = models.CharField(max_length=25, null=True, blank=True, choices=MOVIE_TYPE, default=FULLMOVIE)
    # Full-Movie, Trailer, Short-Movie
    LanguageCC = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return str(self.id) + ', ' + self.Name + ', ' + str(self.ReleaseDate)


class Subscriptions(models.Model):
    ACTIVE = 'AC'
    INACTIVE = 'IA'
    SUB_STATUS = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'InActive'),
    )
    id = models.BigAutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    SubscriptDate = models.DateTimeField('Date Subscribed')
    NextRenewal = models.DateTimeField('Next Renewal')
    Status = models.CharField(max_length=25, null=True, blank=True, choices=SUB_STATUS,
                              default=INACTIVE)  # Active, Inactive

    def __str__(self):
        return str(self.id) + ', ' + self.SubscriptDate + ', ' + self.Status


class WatchList(models.Model):
    id = models.BigAutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.DO_NOTHING)
    Dated = models.DateTimeField('Date WatchListed')

    def __str__(self):
        return str(self.id) + ', ' + self.Dated


class WatchLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.DO_NOTHING)
    ViewDate = models.DateTimeField('Date Viewed')

    def __str__(self):
        return str(self.id) + ', ' + self.ViewDate


class Adverts(models.Model):
    DOCUMENTARY = 'DC'
    GENRES = 'GR'
    RECENT = 'RC'
    STAFFPICKS = 'SP'
    NETWORKS = 'NW'
    POPULAR = 'PP'
    MOVIENIGHTS = 'MN'
    ADVERT_TYPE = (
        (DOCUMENTARY, 'Documentaries'),
        (GENRES, 'Genres'),
        (RECENT, 'Recently-Added'),
        (STAFFPICKS, 'Staff-Picks'),
        (NETWORKS, 'Networks'),
        (POPULAR, 'Popular'),
        (MOVIENIGHTS, 'Movie-Nights'),
    )
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    Name = models.CharField(max_length=100, null=False, blank=False)
    IndexOrder = models.IntegerField(default=0)
    groupings = models.TextField(max_length=200, null=True, blank=True)
    Style = models.CharField(max_length=45, null=True, blank=True)
    Type = models.CharField(max_length=45, null=True, blank=True, choices=ADVERT_TYPE, default=GENRES)

    # TV, Movies, Kids, TV-Documentary, TV-Genries, Movie-Documentary, Movie-Genrie

    def __str__(self):
        return str(self.id) + ', ' + self.Name + ', ' + self.IndexOrder


class Actors(models.Model):
    id = models.BigAutoField(primary_key=True)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, null=False, blank=False)
    RolePlayed = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return str(self.id) + ', ' + self.Name + ', ' + self.RolePlayed


class MovieGenreMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    movie = models.ForeignKey(Movies, on_delete=models.DO_NOTHING)
    genres = models.ForeignKey(Genres, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)
