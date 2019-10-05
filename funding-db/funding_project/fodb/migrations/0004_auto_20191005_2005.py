# Generated by Django 2.2.4 on 2019-10-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fodb', '0003_auto_20190916_1137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funding_opportunity',
            options={'ordering': ['name'], 'verbose_name': 'Funding Opportunity', 'verbose_name_plural': 'Funding Opportunities'},
        ),
        migrations.RemoveField(
            model_name='funding_opportunity',
            name='herdc',
        ),
        migrations.AddField(
            model_name='funding_opportunity',
            name='EOI_deadline',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Expression of interest deadline'),
        ),
        migrations.AddField(
            model_name='funding_opportunity',
            name='External_deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='funding_opportunity',
            name='Forecast_Month',
            field=models.CharField(blank=True, choices=[('1', 'Jan'), ('2', 'Feb'), ('3', 'Mar'), ('4', 'Apr'), ('5', 'May'), ('6', 'Jun'), ('7', 'Jul'), ('8', 'Aug'), ('9', 'Sep'), ('10', 'Oct'), ('11', 'Nov'), ('12', 'Dec')], max_length=15),
        ),
        migrations.AddField(
            model_name='funding_opportunity',
            name='Internal_deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='funding_opportunity',
            name='Minimum_data_deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='funding_opportunity',
            name='fable',
            field=models.BooleanField(default=False, verbose_name='FABLE'),
        ),
        migrations.AddField(
            model_name='funding_opportunity',
            name='provider',
            field=models.CharField(default='none', max_length=100, verbose_name='Funding provider'),
        ),
        migrations.AlterField(
            model_name='funding_opportunity',
            name='closing_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='funding_opportunity',
            name='duration_type',
            field=models.CharField(choices=[('Y', 'year'), ('M', 'month')], max_length=6),
        ),
        migrations.AlterField(
            model_name='funding_opportunity',
            name='ecr',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='funding_opportunity',
            name='international',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='funding_opportunity',
            name='is_hidden',
            field=models.BooleanField(default=False, verbose_name='Hidden from regular view'),
        ),
        migrations.AlterField(
            model_name='funding_opportunity',
            name='max_amount',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='funding_opportunity',
            name='max_duration',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='funding_opportunity',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='funding_opportunity',
            name='phd',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='funding_opportunity',
            name='science',
            field=models.BooleanField(default=False, verbose_name='SCI'),
        ),
        migrations.AlterField(
            model_name='funding_opportunity',
            name='travel',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='funding_opportunity',
            name='visiting',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='funding_opportunity',
            name='wir',
            field=models.BooleanField(default=False),
        ),
    ]
