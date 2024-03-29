# Generated by Django 5.0.1 on 2024-01-10 19:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_post_date_alter_post_content_alter_post_excerpt_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="posts",
                to="blog.author",
            ),
        ),
    ]
