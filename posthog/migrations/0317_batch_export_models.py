# Generated by Django 3.2.18 on 2023-05-30 09:06

from django.db import migrations, models
import django.db.models.deletion
import posthog.models.utils


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0316_action_href_text_matching"),
    ]

    operations = [
        migrations.CreateModel(
            name="BatchExportDestination",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=posthog.models.utils.UUIDT, editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("S3", "S3")],
                        help_text="A choice of supported BatchExportDestination types.",
                        max_length=64,
                    ),
                ),
                (
                    "config",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="A JSON field to store all configuration parameters required to access a BatchExportDestination.",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="The timestamp at which this BatchExportDestination was created."
                    ),
                ),
                (
                    "last_updated_at",
                    models.DateTimeField(
                        auto_now=True, help_text="The timestamp at which this BatchExportDestination was last updated."
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BatchExport",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=posthog.models.utils.UUIDT, editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        help_text="The team this belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="posthog.team",
                    ),
                ),
                ("name", models.TextField(help_text="A human-readable name for this BatchExport.")),
                (
                    "destination",
                    models.ForeignKey(
                        help_text="The destination to export data to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="posthog.batchexportdestination",
                    ),
                ),
                (
                    "interval",
                    models.CharField(
                        choices=[("hour", "hour"), ("day", "day"), ("week", "week")],
                        default="hour",
                        help_text="The interval at which to export data.",
                        max_length=64,
                    ),
                ),
                ("paused", models.BooleanField(default=False, help_text="Whether this BatchExport is paused or not.")),
                (
                    "deleted",
                    models.BooleanField(default=False, help_text="Whether this BatchExport is deleted or not."),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="The timestamp at which this BatchExport was created."
                    ),
                ),
                (
                    "last_updated_at",
                    models.DateTimeField(
                        auto_now=True, help_text="The timestamp at which this BatchExport was last updated."
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BatchExportRun",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=posthog.models.utils.UUIDT, editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Cancelled", "Cancelled"),
                            ("Completed", "Completed"),
                            ("ContinuedAsNew", "Continuedasnew"),
                            ("Failed", "Failed"),
                            ("Terminated", "Terminated"),
                            ("TimedOut", "Timedout"),
                            ("Running", "Running"),
                            ("Starting", "Starting"),
                        ],
                        help_text="The status of this run.",
                        max_length=64,
                    ),
                ),
                (
                    "records_completed",
                    models.IntegerField(help_text="The number of records that have been exported.", null=True),
                ),
                (
                    "latest_error",
                    models.TextField(help_text="The latest error that occurred during this run.", null=True),
                ),
                ("data_interval_start", models.DateTimeField(help_text="The start of the data interval.")),
                ("data_interval_end", models.DateTimeField(help_text="The end of the data interval.")),
                ("cursor", models.TextField(help_text="An opaque cursor that may be used to resume.", null=True)),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="The timestamp at which this BatchExportRun was created."
                    ),
                ),
                (
                    "finished_at",
                    models.DateTimeField(
                        help_text="The timestamp at which this BatchExportRun finished, successfully or not.", null=True
                    ),
                ),
                (
                    "last_updated_at",
                    models.DateTimeField(
                        auto_now=True, help_text="The timestamp at which this BatchExportRun was last updated."
                    ),
                ),
                (
                    "batch_export",
                    models.ForeignKey(
                        help_text="The BatchExport this run belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="posthog.batchexport",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]