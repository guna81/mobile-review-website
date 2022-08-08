from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=60)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    avg_rating = models.IntegerField(null=True, blank=True, default=5)

    def __str__(self):
        return f"{self.name}, {self.brand}, {self.avg_rating}"

class Latest(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.model}"

class PopularMobiles(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.model}"

class RecentMobiles(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.model}, {self.user}"

class PopularComparisions(models.Model):
    mobile1 = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='pmodel1')
    mobile2 = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='pmodel2')

    def __str__(self):
        return f"{self.mobile1}, {self.mobile2}"

class RecentComparisions(models.Model):
    mobile1 = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='rmodel1')
    mobile2 = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='rmodel2')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.mobile1}, {self.mobile2}, {self.user}"

class Varient(models.Model):
    ram = models.IntegerField()
    storage = models.IntegerField()
    price = models.IntegerField()
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.ram}, {self.storage}, {self.model}"

class Spec(models.Model):
    display_size = models.DecimalField(max_digits=4,decimal_places=2)
    display_resolution = models.CharField(max_length=50, null=True, blank=True)
    front_camera = models.CharField(max_length=60)
    rear_camera = models.CharField(max_length=60)
    processor = models.CharField(max_length=60)
    battery = models.IntegerField()
    os = models.CharField(max_length=60, null=True, blank=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.display_size}, {self.front_camera}, {self.rear_camera}, {self.processor}, {self.battery}, {self.os}, {self.model}"

class Review(models.Model):
    rating = models.IntegerField()
    review = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rating}, {self.review}, {self.user}, {self.mobile}"
