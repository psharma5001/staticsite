# Generated by Django 3.2.13 on 2022-05-08 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=b'I01\n')),
                ('summary', models.TextField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('is_generated', models.BooleanField(default=b'I00\n')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_rendered', markdownfield.models.RenderedMarkdownField()),
                ('text', markdownfield.models.MarkdownField(rendered_field='text_rendered', use_editor=False)),
                ('filename', models.CharField(max_length=60, unique=b'I01\n')),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.website')),
            ],
        ),
    ]