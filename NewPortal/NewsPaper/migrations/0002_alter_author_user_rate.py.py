

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPaper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='user_rate',
            field=models.IntegerField(default=0),
        ),
    ]