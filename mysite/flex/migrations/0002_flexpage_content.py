# Generated by Django 3.2.7 on 2021-09-29 23:28

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('Title_and_Text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your Title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True))]))], blank=True, null=True),
        ),
    ]