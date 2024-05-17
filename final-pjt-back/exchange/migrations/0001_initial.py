# Generated by Django 4.2.8 on 2024-05-17 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cur_unit', models.CharField(max_length=100)),
                ('cur_nm', models.CharField(max_length=100)),
                ('ttb', models.CharField(max_length=100)),
                ('tts', models.CharField(max_length=100)),
                ('deal_bas_r', models.CharField(max_length=100)),
                ('bkpr', models.CharField(max_length=100)),
                ('yy_efee_r', models.CharField(max_length=100)),
                ('ten_dd_efee_r', models.CharField(max_length=100)),
                ('kftc_deal_bas_r', models.CharField(max_length=100)),
                ('kftc_bkpr', models.CharField(max_length=100)),
            ],
        ),
    ]
