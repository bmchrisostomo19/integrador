<<<<<<< HEAD
# Generated by Django 3.2.7 on 2021-10-07 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('thumb', models.ImageField(upload_to='thumb_cursos')),
            ],
        ),
    ]
=======
# Generated by Django 3.2.7 on 2021-10-07 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('thumb', models.ImageField(upload_to='thumb_cursos')),
            ],
        ),
    ]
>>>>>>> 1651482b46c304b36ab1d5056382003c08636891
