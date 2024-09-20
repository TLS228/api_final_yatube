# Generated by Django 3.2.16 on 2024-09-20 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20240920_1709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('author', '-pub_date')},
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.group'),
        ),
    ]
