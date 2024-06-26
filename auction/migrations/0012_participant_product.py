

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0011_auction_user_membership'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auction.Product'),
        ),
    ]
