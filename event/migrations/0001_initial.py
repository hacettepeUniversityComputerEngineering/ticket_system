# Generated by Django 2.1.3 on 2018-12-30 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BuildingEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CityEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.City')),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Category')),
            ],
        ),
        migrations.CreateModel(
            name='EventCreation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Director')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_site', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EventSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_date_of_schedule', models.TimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Salon')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Date')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('seat', models.FloatField()),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Block')),
            ],
        ),
        migrations.AddField(
            model_name='eventschedule',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Schedule'),
        ),
        migrations.AddField(
            model_name='eventcreation',
            name='event_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventOwner'),
        ),
        migrations.AddField(
            model_name='cityevent',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event'),
        ),
        migrations.AddField(
            model_name='buildingevent',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event'),
        ),
        migrations.AddField(
            model_name='block',
            name='salon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Salon'),
        ),
    ]