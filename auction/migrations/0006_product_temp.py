

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_auto_20200614_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='temp',
            field=models.IntegerField(null=True),
        ),
    ]
