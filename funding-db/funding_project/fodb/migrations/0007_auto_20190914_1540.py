# Generated by Django 2.2.4 on 2019-09-14 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fodb', '0006_auto_20190914_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='important_date',
            name='funding_opportunity',
        ),
        migrations.CreateModel(
            name='fodb_date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_id', models.ManyToManyField(to='fodb.important_date')),
                ('fodb_id', models.ManyToManyField(to='fodb.funding_opportunity')),
            ],
        ),
    ]
