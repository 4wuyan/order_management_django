# Generated by Django 2.0.1 on 2018-01-26 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='actual_deduction_CNY',
            field=models.DecimalField(blank=True, db_column='actual_deduction_CNY', decimal_places=2, max_digits=10, null=True, verbose_name='实扣'),
        ),
    ]
