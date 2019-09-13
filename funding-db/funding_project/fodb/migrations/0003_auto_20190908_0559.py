# Generated by Django 2.2.4 on 2019-09-08 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fodb', '0002_boolean_tags_funding_funding_opportunity1_importantdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='funding_opportunity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2500)),
                ('herdc', models.IntegerField(blank=True)),
                ('closing_month', models.DateTimeField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('link', models.URLField(max_length=260)),
                ('limit_per_uni', models.BooleanField(default=False)),
                ('max_amount', models.IntegerField(blank=True)),
                ('max_duration', models.IntegerField(blank=True)),
                ('amount_estimated', models.BooleanField(default=False)),
                ('duration_estimated', models.BooleanField(default=False)),
                ('ecr', models.BooleanField(default=False)),
                ('travel', models.BooleanField(default=False)),
                ('visiting', models.BooleanField(default=False)),
                ('wir', models.BooleanField(default=False)),
                ('phd', models.BooleanField(default=False)),
                ('international', models.BooleanField(default=False)),
                ('hms', models.BooleanField(default=False)),
                ('ems', models.BooleanField(default=False)),
                ('science', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='important_date',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('milestone', models.CharField(max_length=35)),
                ('date', models.DateTimeField()),
                ('date_status', models.CharField(max_length=20)),
                ('funding_opportunity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fodb.funding_opportunity')),
            ],
        ),
        migrations.RemoveField(
            model_name='funding',
            name='Funding_Opportunity1',
        ),
        migrations.RemoveField(
            model_name='importantdate',
            name='Opportunity_ID',
        ),
        migrations.DeleteModel(
            name='Boolean_Tags',
        ),
        migrations.DeleteModel(
            name='Funding',
        ),
        migrations.DeleteModel(
            name='Funding_Opportunity1',
        ),
        migrations.DeleteModel(
            name='ImportantDate',
        ),
    ]