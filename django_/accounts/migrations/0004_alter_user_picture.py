# Generated by Django 4.2.7 on 2023-11-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='/accounts/images/annon.png', null=True, upload_to='accounts/images/%Y/%m/%d/%H/%M/%S/'),
        ),
    ]