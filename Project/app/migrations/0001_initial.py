# Generated by Django 3.2.7 on 2021-10-13 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productid', models.IntegerField(db_column='productId', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=45, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('images', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, db_column='Location', max_length=45, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transactionid', models.IntegerField(db_column='transactionId', primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
                ('length', models.IntegerField(blank=True, db_column='Length', null=True)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=45, null=True)),
                ('amount', models.FloatField(blank=True, db_column='Amount', null=True)),
                ('fname', models.CharField(blank=True, max_length=45, null=True)),
                ('lname', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('number', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'Transaction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(db_column='User_id', primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=45)),
                ('lname', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
        ),
    ]