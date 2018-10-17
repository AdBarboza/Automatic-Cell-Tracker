# Generated by Django 2.1.1 on 2018-10-17 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=1)),
                ('gp_sanguineo', models.CharField(max_length=2)),
                ('factor_h', models.CharField(max_length=1)),
                ('alergias', models.CharField(max_length=1000)),
                ('padecimiento', models.CharField(max_length=1000)),
            ],
        ),
    ]
