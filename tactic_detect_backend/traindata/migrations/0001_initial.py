# Generated by Django 3.2.5 on 2022-09-01 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authenticate',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('text', models.CharField(default='', max_length=1000)),
                ('label', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Authorize',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('method_name', models.CharField(max_length=500)),
                ('method_parameter', models.CharField(max_length=500)),
                ('method_return', models.CharField(max_length=500)),
                ('method_call', models.CharField(max_length=500)),
                ('label', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cache',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('method_name', models.CharField(max_length=500)),
                ('method_parameter', models.CharField(max_length=500)),
                ('method_return', models.CharField(max_length=500)),
                ('method_call', models.CharField(max_length=500)),
                ('label', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Checkpoint',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('method_name', models.CharField(max_length=500)),
                ('method_parameter', models.CharField(max_length=500)),
                ('method_return', models.CharField(max_length=500)),
                ('method_call', models.CharField(max_length=500)),
                ('label', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fifo',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('method_name', models.CharField(max_length=500)),
                ('method_parameter', models.CharField(max_length=500)),
                ('method_return', models.CharField(max_length=500)),
                ('method_call', models.CharField(max_length=500)),
                ('label', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Heartbeat',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('method_name', models.CharField(max_length=500)),
                ('method_parameter', models.CharField(max_length=500)),
                ('method_return', models.CharField(max_length=500)),
                ('method_call', models.CharField(max_length=500)),
                ('label', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pingecho',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('method_name', models.CharField(max_length=500)),
                ('method_parameter', models.CharField(max_length=500)),
                ('method_return', models.CharField(max_length=500)),
                ('method_call', models.CharField(max_length=500)),
                ('label', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('method_name', models.CharField(max_length=500)),
                ('method_parameter', models.CharField(max_length=500)),
                ('method_return', models.CharField(max_length=500)),
                ('method_call', models.CharField(max_length=500)),
                ('label', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Redundancy',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('method_name', models.CharField(max_length=500)),
                ('method_parameter', models.CharField(max_length=500)),
                ('method_return', models.CharField(max_length=500)),
                ('method_call', models.CharField(max_length=500)),
                ('label', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('method_name', models.CharField(max_length=500)),
                ('method_parameter', models.CharField(max_length=500)),
                ('method_return', models.CharField(max_length=500)),
                ('method_call', models.CharField(max_length=500)),
                ('label', models.IntegerField()),
            ],
        ),
    ]
