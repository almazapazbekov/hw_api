# Generated by Django 3.2 on 2022-12-08 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20221209_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='fullname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.position'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
