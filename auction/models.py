"""VIEWS.PY"""
from django.db import models
from django.contrib.auth.models import User

class Memberfee(models.Model):
    """string"""
    fee = models.CharField(max_length=20,null=True)
    def __str__(self):
        return str(self.fee)

class Bidder(models.Model):
    """string"""
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=10,null=True)
    image = models.FileField(null=True)
    membership = models.ForeignKey(Memberfee,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.user.username)
        
class AuctionUser(models.Model):
    """string"""
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=10,null=True)
    image = models.FileField(null=True)
    membership = models.ForeignKey(Memberfee,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.user.username)

class Category(models.Model):
    """string"""
    name = models.CharField(max_length=100,null=True)
    def __str__(self):
        return str(self.name)

class SubCategory(models.Model):
    """string"""
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    def __str__(self):
        return str(self.name+" "+self.category.name)

class Sessiondate(models.Model):
    """string"""
    date = models.CharField(max_length=30,null=True)
    def __str__(self):
        return str(self.date)

class SessionTime(models.Model):
    """string"""
    date = models.ForeignKey(Sessiondate,on_delete=models.CASCADE,null=True)
    time = models.CharField(max_length=30,null=True)
    def __str__(self):
        return str(self.date.date+" "+self.time)

class Status(models.Model):
    """string"""
    status = models.CharField(max_length=30,null=True)
    def __str__(self):
        return str(self.status)

class Product(models.Model):
    """string"""
    temp = models.IntegerField(null=True)
    status  =models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    min_price = models.IntegerField(null=True)
    images = models.FileField(null=True)
    session = models.ForeignKey(SessionTime,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.name)

class AuctedProduct(models.Model):
    """string"""
    winner = models.CharField(max_length=100,null=True)
    user = models.ForeignKey(AuctionUser,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.user.user.username+ " " + self.product.name)

class Result(models.Model):
    """string"""
    result = models.CharField(max_length=100,null=True)
    def __str__(self):
        return str(self.result)

class Payment(models.Model):
    """string"""
    pay = models.CharField(max_length=100,null=True)
    def __str__(self):
        return str(self.pay)

class Participant(models.Model):
    """string"""
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,null=True)
    new_price = models.IntegerField(null=True)
    result = models.ForeignKey(Result,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(Bidder,on_delete=models.CASCADE,null=True)
    auctedproduct = models.ForeignKey(AuctedProduct,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)

class SendFeedback(models.Model):
    """string"""
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message1 = models.TextField(null=True)
    date = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.profile.username)
        