from dataclasses import dataclass
from typing import Optional

from django.contrib.auth.models import User
from django.template import Context

from dashboards.component import Chart, Component, Stat
from dashboards.component.text import StatData
from dashboards.types import ValueData


@dataclass
class SSEStat(Stat):
    template_name: str = "dashboards/components/sse_stat.html"
    poll_rate: Optional[int] = 10

    @staticmethod
    def pushpin_url():
        """
        Assuming docker pushpin is running, in real world this would be proxied to application.
        """
        return "http://127.0.0.1:7999/events/"


@dataclass
class SSEChart(Chart):
    template_name: str = "dashboards/components/sse_chart.html"
    poll_rate: Optional[int] = None

    @staticmethod
    def pushpin_url():
        """
        Assuming docker pushpin is running, in real world this would be proxied to application.
        """
        return "http://127.0.0.1:7999/events/"


@dataclass
class SharedComponent(Stat):
    """
    Example of a component, where value is set at a class level so the component can be added simply as

        SharedComponent()
    """

    value: ValueData = lambda **kwargs: StatData(
        text=User.objects.count(), sub_text="User Count"
    )


@dataclass
class GaugeData:
    title: str = ""
    value: Optional[ValueData] = None
    max_value: ValueData = 100


@dataclass
class Gauge(Component):
    template_name: str = "demo/includes/gauge.html"


@dataclass
class NoTemplateComponent(Component):
    def render_as_html(self, context: Context):
        return (
            f"<i>Rendered this value with no template: {context['rendered_value']}</i>"
        )
