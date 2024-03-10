# Generated by Django 5.0 on 2024-03-09 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapi', '0003_feedbackform'),
    ]

    operations = [
        migrations.CreateModel(
            name='stars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(max_length=5)),
            ],
            options={
                'db_table': 'FeedBack_Stars_Table',
            },
        ),
    ]
