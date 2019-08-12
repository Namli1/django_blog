# Generated by Django 2.2.4 on 2019-08-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-date_of_creation']},
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='description',
            field=models.TextField(help_text='Your comment for the blog post.', max_length=200),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date_of_creation',
            field=models.DateField(auto_now_add=True),
        ),
    ]
