

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_auto_20200614_0912'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table=None,
        ),
        migrations.AlterModelTable(
            name='session_date',
            table=None,
        ),
        migrations.AlterModelTable(
            name='session_time',
            table=None,
        ),
        migrations.AlterModelTable(
            name='sub_category',
            table=None,
        ),
    ]
