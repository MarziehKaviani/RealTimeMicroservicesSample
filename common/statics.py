from django.utils.translation import gettext_lazy as _


PENDING = _("Pending")
IN_PROGRESS = _("in_progress")
COMPLETED = _("completed")
TASKS = _("tasks")
TASK = _("task")
COMMENTS = _("comments")

STATUS_CHOICES = [
    (PENDING, 'Pending'),
    (IN_PROGRESS, 'In Progress'),
    (COMPLETED, 'Completed'),
]
