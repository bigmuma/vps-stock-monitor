# Generated by Django 2.2.5 on 2020-06-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vps', '0010_auto_20200617_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='arch',
            field=models.CharField(choices=[('KVM', 'KVM'), ('OpenVZ', 'OpenVZ')], default='KVM', max_length=256, verbose_name='架构'),
        ),
    ]