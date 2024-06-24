from django.db import models
from django.utils.translation import gettext_lazy as _

from services.projects.projects.models import Project
from common.statics import *


class Task(models.Model):
    project = models.ForeignKey(Project, related_name=TASKS, on_delete=models.SET_NULL, null=True,   verbose_name=_("Project"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Task Description"))
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=PENDING, verbose_name=_("Status"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    due_date = models.DateTimeField(verbose_name=_("Due Date"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")
