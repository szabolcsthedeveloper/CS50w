# Generated by Django 4.1 on 2022-08-30 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0015_comments_comment_comments_date_comments_listing_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="user",
            field=models.CharField(max_length=32),
        ),
    ]