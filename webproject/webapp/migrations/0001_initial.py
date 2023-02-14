# Generated by Django 3.2.5 on 2023-01-14 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.PositiveSmallIntegerField(verbose_name='Course Id')),
                ('c_name', models.CharField(max_length=30, verbose_name='Course Name')),
                ('c_duration', models.PositiveSmallIntegerField(verbose_name='Duration')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=37, verbose_name='Dept Name')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_id', models.PositiveSmallIntegerField(verbose_name='Teacher Id')),
                ('t_name', models.CharField(max_length=25, verbose_name='Teacher Name')),
                ('t_join', models.DateTimeField(auto_now_add=True, verbose_name='Join Date')),
                ('t_course', models.CharField(max_length=30, verbose_name='District')),
                ('t_rating', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Rating')),
                ('t_department', models.ManyToManyField(to='webapp.Department')),
                ('t_sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.course')),
            ],
        ),
    ]
