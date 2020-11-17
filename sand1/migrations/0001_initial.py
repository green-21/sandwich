# Generated by Django 3.1.3 on 2020-11-16 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.CharField(max_length=20, primary_key='true', serialize=False)),
                ('pw', models.CharField(max_length=50)),
                ('picture', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=20)),
                ('msg', models.CharField(blank='true', default='', max_length=200)),
                ('time', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('msg', models.CharField(max_length=200)),
                ('time', models.DateTimeField(verbose_name='date published')),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sand1.account')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('picture', models.CharField(max_length=200)),
                ('msg', models.CharField(max_length=200)),
                ('time', models.DateTimeField(verbose_name='date published')),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sand1.account')),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sand1.account')),
                ('post_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sand1.post')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('from_id', models.ManyToManyField(related_name='from_user', to='sand1.Account')),
                ('to_id', models.ManyToManyField(related_name='to_user', to='sand1.Account')),
            ],
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('comment_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sand1.comment')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sand1.post'),
        ),
    ]
