# Generated by Django 4.0.2 on 2022-02-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_item_likeduser_item_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='writerName',
            field=models.CharField(default='', max_length=15, verbose_name='작성자 닉네임'),
        ),
    ]