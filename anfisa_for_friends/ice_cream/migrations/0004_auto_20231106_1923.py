# Generated by Django 3.2.16 on 2023-11-06 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0003_auto_20231106_1847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='icecream',
            options={'ordering': ('output_order', 'title'), 'verbose_name': 'Мороженое', 'verbose_name_plural': 'Мороженые'},
        ),
        migrations.AlterField(
            model_name='icecream',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
