# Generated by Django 5.1 on 2024-08-30 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('especialidade', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
    ]
