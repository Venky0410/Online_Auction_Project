"""ADMIN.PY"""
from django.contrib import admin
from .models import (
    Bidder, Result, Payment, Memberfee, Status,
    SendFeedback, AuctionUser, Category,
    SubCategory, Sessiondate, SessionTime,
    Product, AuctedProduct, Participant
)
# Register your models here.
admin.site.register(Bidder)
admin.site.register(Result)
admin.site.register(Payment)
admin.site.register(Memberfee)
admin.site.register(Status)
admin.site.register(SendFeedback)
admin.site.register(AuctionUser)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Sessiondate)
admin.site.register(SessionTime)
admin.site.register(Product)
admin.site.register(AuctedProduct)
admin.site.register(Participant)
