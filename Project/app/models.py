from django.db import models

# Create your models here.
class Product(models.Model):
    productid = models.AutoField(db_column='productId', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=45)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    location = models.CharField(db_column='Location', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Product'


class Transaction(models.Model):
    transactionid = models.AutoField(db_column='transactionId', primary_key=True)  # Field name made lowercase.
    productid = models.IntegerField(Product, db_column='productId')  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    length = models.IntegerField(db_column='Length', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(max_length=45, blank=True, null=True)
    lname = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    number = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Transaction'


class User(models.Model):
    user_id = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)
    username = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'User'