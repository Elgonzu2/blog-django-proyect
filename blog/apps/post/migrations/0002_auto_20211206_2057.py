# Generated by Django 3.0 on 2021-12-06 23:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['-id']},
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='description',
            new_name='comentario',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='texto',
        ),
        migrations.AddField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
