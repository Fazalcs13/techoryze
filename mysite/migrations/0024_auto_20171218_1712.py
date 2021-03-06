# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0023_auto_20171214_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_video_1',
            field=models.FileField(default=b'', upload_to='video/'),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_video_2',
            field=models.FileField(default=b'', upload_to='video/'),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_video_3',
            field=models.FileField(default=b'', upload_to='video/'),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_video_4',
            field=models.FileField(default=b'', upload_to='video/'),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_video_5',
            field=models.FileField(default=b'', upload_to='video/'),
        ),
    ]
