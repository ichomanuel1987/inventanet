# Generated by Django 2.0.1 on 2018-04-30 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0004_auto_20180429_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number_entry', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('plate', models.CharField(max_length=50)),
                ('count', models.CharField(max_length=100)),
                ('price_c', models.FloatField(max_length=50)),
                ('stock', models.IntegerField(max_length=55)),
                ('serial', models.CharField(max_length=100)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacenes.Entry')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacenes.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type_person', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('type_document', models.CharField(max_length=50)),
                ('number_document', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacenes.Person'),
        ),
    ]
