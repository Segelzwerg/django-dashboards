# Generated by Django 4.1.3 on 2023-01-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "pipelines",
            "0013_pipelineexecution_completed_pipelineresult_completed_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pipelineresult",
            name="input_data",
        ),
        migrations.AddField(
            model_name="pipelineexecution",
            name="input_data",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
