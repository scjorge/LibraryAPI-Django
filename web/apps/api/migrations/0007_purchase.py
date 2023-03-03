# Generated by Django 4.0.4 on 2023-03-01 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_book_author_alter_book_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'On Cart'), (2, 'Purchese Made'), (3, 'Paid'), (4, 'Delivered')], default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchase', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]