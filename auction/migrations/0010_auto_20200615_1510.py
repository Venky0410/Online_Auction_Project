

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0009_auto_20200614_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member_fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bidder',
            name='membership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auction.Member_fee'),
        ),
    ]
