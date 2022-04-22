# Generated by Django 4.0.4 on 2022-04-20 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('RESOl', 'Resolved'), ('UNRES', 'Unresolved'), ('FROZN', 'Frozen')], default='FROZN', max_length=5)),
            ],
        ),
    ]
