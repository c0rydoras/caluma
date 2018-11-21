# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-09 07:41
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import localized_fields.fields.field
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Form",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("slug", models.SlugField(primary_key=True, serialize=False)),
                ("name", localized_fields.fields.field.LocalizedField(required=["en"])),
                (
                    "description",
                    localized_fields.fields.field.LocalizedField(blank=True, null=True),
                ),
                ("meta", django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ("is_published", models.BooleanField(default=False)),
                ("is_archived", models.BooleanField(default=False)),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="FormQuestion",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "sort",
                    models.PositiveIntegerField(
                        db_index=True, default=0, editable=False
                    ),
                ),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="form.Form"
                    ),
                ),
            ],
            options={"ordering": ("-sort", "id")},
        ),
        migrations.CreateModel(
            name="Option",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("slug", models.SlugField(primary_key=True, serialize=False)),
                (
                    "label",
                    localized_fields.fields.field.LocalizedField(required=["en"]),
                ),
                ("meta", django.contrib.postgres.fields.jsonb.JSONField(default={})),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("slug", models.SlugField(primary_key=True, serialize=False)),
                (
                    "label",
                    localized_fields.fields.field.LocalizedField(required=["en"]),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("checkbox", "checkbox"),
                            ("integer", "integer"),
                            ("float", "float"),
                            ("radio", "radio"),
                            ("textarea", "textarea"),
                            ("text", "text"),
                        ],
                        max_length=10,
                    ),
                ),
                ("is_required", models.TextField(default="false")),
                ("is_hidden", models.TextField(default="false")),
                ("is_archived", models.BooleanField(default=False)),
                (
                    "configuration",
                    django.contrib.postgres.fields.jsonb.JSONField(default={}),
                ),
                ("meta", django.contrib.postgres.fields.jsonb.JSONField(default={})),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="QuestionOption",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "sort",
                    models.PositiveIntegerField(
                        db_index=True, default=0, editable=False
                    ),
                ),
                (
                    "option",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="form.Option"
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="form.Question"
                    ),
                ),
            ],
            options={"ordering": ("-sort", "id")},
        ),
        migrations.AddField(
            model_name="question",
            name="options",
            field=models.ManyToManyField(
                related_name="questions",
                through="form.QuestionOption",
                to="form.Option",
            ),
        ),
        migrations.AddField(
            model_name="formquestion",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="form.Question"
            ),
        ),
        migrations.AddField(
            model_name="form",
            name="questions",
            field=models.ManyToManyField(
                related_name="forms", through="form.FormQuestion", to="form.Question"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="questionoption", unique_together=set([("option", "question")])
        ),
        migrations.AlterUniqueTogether(
            name="formquestion", unique_together=set([("form", "question")])
        ),
    ]