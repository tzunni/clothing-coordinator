# Generated by Django 5.1.1 on 2024-12-02 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('Top', 'Top'), ('Bottom', 'Bottom'), ('Accessory', 'Accessory')], default='Top', max_length=10),
        ),
    ]
