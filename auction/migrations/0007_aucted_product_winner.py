

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_product_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='aucted_product',
            name='winner',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
