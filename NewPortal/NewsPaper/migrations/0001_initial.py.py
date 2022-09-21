

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_rate', models.FloatField(default=0.0)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_category', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('A', 'Статься'), ('N', 'Новость')], default='N', max_length=1)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('post_rate', models.IntegerField(default=0)),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaper.author')),
                ('post_category', models.ManyToManyField(to='NewsPaper.Category')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_category', models.ManyToManyField(to='NewsPaper.Category')),
                ('post_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaper.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.TextField()),
                ('comment_date_created', models.DateField(auto_now_add=True)),
                ('comment_rate', models.IntegerField(default=0)),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaper.post')),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]