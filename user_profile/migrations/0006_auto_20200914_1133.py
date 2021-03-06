# Generated by Django 3.1.1 on 2020-09-14 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20200914_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='follow',
            name='user_follow',
        ),
        migrations.AddField(
            model_name='follow',
            name='user_follow',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_followers', to='user_profile.user'),
            preserve_default=False,
        ),
    ]
