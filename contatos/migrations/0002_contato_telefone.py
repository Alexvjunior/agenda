# Generated by Django 3.2.7 on 2021-09-14 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='telefone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
