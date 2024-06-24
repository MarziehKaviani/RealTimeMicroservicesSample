from django.db import models
from django.utils.translation import gettext_lazy as _

from common.statics import *
from services.tasks.tasks.models import Task


class Comment(models.Model):
    task = models.ForeignKey(Task, related_name=COMMENTS, on_delete=models.CASCADE, verbose_name=_("Task"))
    author = models.CharField(max_length=255, verbose_name=_("Author"))
    content = models.TextField(verbose_name=_("Content"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    def __str__(self):
        return _(f'Comment by {self.author} on {self.task}')

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
