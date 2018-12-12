# Generated by Django 2.1.4 on 2018-12-10 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StoryBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_text', models.CharField(max_length=1000)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Story')),
            ],
        ),
    ]