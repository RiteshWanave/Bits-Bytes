# Generated by Django 3.1.1 on 2021-05-24 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brooklyn', '0003_auto_20210521_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='endpointURL',
            new_name='EndpointURL',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='field1Name',
            new_name='Field1Name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='field2Name',
            new_name='Field2Name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='field3Name',
            new_name='Field3Name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='field4Name',
            new_name='Field4Name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='field5Name',
            new_name='Field5Name',
        ),
        migrations.RenameField(
            model_name='projectobject',
            old_name='field1',
            new_name='Field1',
        ),
        migrations.RenameField(
            model_name='projectobject',
            old_name='field2',
            new_name='Field2',
        ),
        migrations.RenameField(
            model_name='projectobject',
            old_name='field3',
            new_name='Field3',
        ),
        migrations.RenameField(
            model_name='projectobject',
            old_name='field4',
            new_name='Field4',
        ),
        migrations.RenameField(
            model_name='projectobject',
            old_name='field5',
            new_name='Field5',
        ),
        migrations.RenameField(
            model_name='projectobject',
            old_name='project',
            new_name='Project',
        ),
        migrations.RemoveField(
            model_name='projectobject',
            name='dateTime',
        ),
        migrations.AddField(
            model_name='projectobject',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 24, 18, 39, 47, 126683)),
        ),
    ]
