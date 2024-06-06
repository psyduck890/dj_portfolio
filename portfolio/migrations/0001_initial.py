# Generated by Django 5.0.6 on 2024-06-06 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('categories', models.CharField(choices=[('Website', 'Website'), ('Web App', 'Web App')], default='Website', max_length=50)),
                ('img', models.ImageField(upload_to='static/assets/img/portfolio/')),
            ],
        ),
    ]