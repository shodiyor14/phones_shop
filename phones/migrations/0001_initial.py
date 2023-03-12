# Generated by Django 4.1.5 on 2023-01-29 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhonesBrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(max_length=50)),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.CreateModel(
            name='PhonesColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
        ),
        migrations.CreateModel(
            name='PhonesModelsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='PhonesTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(max_length=50)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='PhonesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=60)),
                ('os', models.CharField(max_length=30)),
                ('long_descriptions', models.TextField()),
                ('short_descriptions', models.TextField()),
                ('ram', models.CharField(max_length=50)),
                ('memory_card', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='phone')),
                ('number_of_sim_cards', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='phone', to='phones.phonesbrandmodel')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='phone', to='phones.phonesmodelscategory')),
                ('color', models.ManyToManyField(related_name='phone', to='phones.phonescolormodel')),
                ('tag', models.ManyToManyField(related_name='phone', to='phones.phonestagmodel')),
            ],
            options={
                'verbose_name': 'phone',
                'verbose_name_plural': 'phones',
            },
        ),
    ]
