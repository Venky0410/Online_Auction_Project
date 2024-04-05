

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0010_auto_20200615_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_user',
            name='membership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auction.Member_fee'),
        ),
    ]
