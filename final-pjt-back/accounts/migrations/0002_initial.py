<<<<<<< HEAD
# Generated by Django 4.2.8 on 2024-05-21 12:00
=======
# Generated by Django 4.2.13 on 2024-05-21 08:25
>>>>>>> 6d1582427f04e4c4178951bf119572470ddf9be0

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('accounts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
=======
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0001_initial'),
>>>>>>> 6d1582427f04e4c4178951bf119572470ddf9be0
        ('financial_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='deposit',
            field=models.ManyToManyField(related_name='interested_users_deposit', to='financial_products.depositproduct'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='saving',
            field=models.ManyToManyField(related_name='interested_users_saving', to='financial_products.savingproduct'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
