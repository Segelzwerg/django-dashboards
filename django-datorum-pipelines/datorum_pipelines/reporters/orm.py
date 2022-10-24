from typing import Optional

from django.utils import timezone

from datorum_pipelines import BasePipelineReporter

from ..models import PipelineExecution, PipelineLog, TaskLog
from ..status import PipelineTaskStatus


class ORMReporter(BasePipelineReporter):
    def report(
        self,
        pipeline_id: Optional[str],
        pipeline_task: Optional[str],
        task_id: Optional[str],
        status: PipelineTaskStatus,
        message: str,
    ):
        if pipeline_id:
            PipelineLog.objects.create(
                pipeline_id=pipeline_id, status=status.value, message=message
            )

            # TODO moved this out of base so that ORM is not required, not sure tho if it's used/needed?
            if status == PipelineTaskStatus.RUNNING:
                PipelineExecution.objects.update_or_create(
                    pipeline_id=pipeline_id, defaults={"last_run": timezone.now()}
                )

        else:
            TaskLog.objects.create(
                pipeline_task=pipeline_task,
                task_id=task_id,
                status=status.value,
                message=message,
            )
