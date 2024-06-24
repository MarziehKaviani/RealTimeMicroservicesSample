from django.utils.translation import gettext_lazy as _


PENDING = "pending"
IN_PROGRESS = "in_progress"
COMPLETED = "completed"
TASKS = "tasks"
TASK = "task"
COMMENTS = "comments"
GET = "GET"
PUT = "PUT"
DELETE = "DELETE"
POST = "POST"
DATA = "data"
MESSAGE = "message"
BUISSINES_STATUS_CODE = "business_status_code"
NAME = "name"
DESCRIPTION = "description"
CREATED_AT = "created_at"
UPDATED_AT = "updated_at"
DETAILS = "details"
PROJECTS = 'projects'
AUTHOR = "author"
CONTENT = "content"

INVALID_INPUT_DATA_MSG = _("Invalid input data")
PROJECT_CREATED_MSG = _("Project created successfully.")
PROJECT_DELETED_MSG = _("Project deleted successfully.")
PROJECT_UPDATED_MSG = _("Project updated successfully.")
TASK_CREATED_MSG = _("Task created successfully.")
TASK_DELETED_MSG = _("Task deleted successfully.")
TASK_UPDATED_MSG = _("Task updated successfully.")
COMMENT_CREATED_MSG = _("Comment created successfully.")

STATUS_CHOICES = [
    (PENDING, _('Pending')),
    (IN_PROGRESS, _('In Progress')),
    (COMPLETED, _('Completed')),
]

class BusinessStatusCodes:
    """
    3000-3999 for validation errors
    4000-4999 for system errors
    """
    SUCCESS = 200
    INVALID_INPUT_DATA = 3001
    INVALID_LOGIN_CREDENTIONAL = 3002
    REDIS_IS_DOWN = 4001


BUSINESS_STATUS = BusinessStatusCodes()
