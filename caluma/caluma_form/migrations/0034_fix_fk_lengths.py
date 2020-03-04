# Generated by Django 2.2.10 on 2020-02-27 13:42

from django.db import migrations

from caluma.utils import fix_foreign_key_types


def fix_fk_types_migration(apps, schema_editor):

    fix_foreign_key_types(apps, schema_editor.connection)


class Migration(migrations.Migration):

    dependencies = [
        ("caluma_form", "0033_slugfield_length"),
        ("caluma_workflow", "0019_slugfield_length"),
    ]

    operations = [
        migrations.RunPython(fix_fk_types_migration, migrations.RunPython.noop)
    ]
