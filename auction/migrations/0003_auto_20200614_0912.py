

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_send_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterModelTable(
            name='category',
            table='auction_category',
        ),
        migrations.AlterModelTable(
            name='session_date',
            table='auction_session_date',
        ),
        migrations.AlterModelTable(
            name='session_time',
            table='auction_session_time',
        ),
        migrations.AlterModelTable(
            name='sub_category',
            table='auction_sub_category',
        ),
    ]
