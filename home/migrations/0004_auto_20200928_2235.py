# Generated by Django 3.1.1 on 2020-09-28 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200928_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='tag',
            field=models.ForeignKey(default='No tag', null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(default='None', max_length=50, null=True),
        ),
    ]
