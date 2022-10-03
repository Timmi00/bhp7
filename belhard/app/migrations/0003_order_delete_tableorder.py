# Generated by Django 4.1.1 on 2022-09-28 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_alter_product_options_tableorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='время создания')),
                ('is_paid', models.BooleanField(default=False, verbose_name='оплата')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.product', verbose_name='товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'корзина',
                'verbose_name_plural': 'корзины',
                'db_table': 'app_Orders',
                'ordering': ('date_created',),
            },
        ),
        migrations.DeleteModel(
            name='TableOrder',
        ),
    ]