# Generated by Django 2.1.5 on 2019-01-11 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PastEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('mobile_number', models.CharField(max_length=200)),
                ('money', models.FloatField()),
                ('credit_card_numer', models.CharField(max_length=200)),
                ('user_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserPastEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('past_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.PastEvent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
