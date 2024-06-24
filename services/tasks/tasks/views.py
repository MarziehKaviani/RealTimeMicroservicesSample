from rest_framework import viewsets, status, action
from rest_framework.response import Response

from common.statics import *
from common.utils.utils import BaseResponse
from common.validators import check_api_input_data
from .models import Task, Comment
from .serializers import TaskSerializer, CommentSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for Project model.
    """
    queryset = TaskSerializer.get_queryset(Task)

    def get_serializer_class(self):
        if self.action == 'comments':
            return CommentSerializer
        return TaskSerializer
    
    def list(self, request, *args, **kwargs):
        """
        Retrieve a list of all tasks.

        GET /tasks/

        Parameters
        ----------
        request : Request
            The HTTP request object.

        Returns
        -------
        Response
            A response object containing the list of tasks.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return BaseResponse(
            message=None,
            data=serializer.data,
            is_exception=False,
            http_status_code=status.HTTP_200_OK,
            business_status_code=BUSINESS_STATUS.SUCCESS
        )
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        """
        Retrieve a single task by ID.

        GET /tasks/<id>/

        Parameters
        ----------
        request : Request
            The HTTP request object.
        pk : int
            The primary key of the task to retrieve.

        Returns
        -------
        Response
            A response object containing the task details.
        """
        task = self.get_object()
        serializer = self.get_serializer(task)
        return BaseResponse(
            message=None,
            data=serializer.data,
            is_exception=False,
            http_status_code=status.HTTP_200_OK,
            business_status_code=BUSINESS_STATUS.SUCCESS
        )

    def create(self, request, *args, **kwargs):
        """
        Create a new task.

        POST /tasks/

        Parameters
        ----------
        request : Request
            The HTTP request object containing the data for the new task.

        Returns
        -------
        Response
            A response object containing the created task's details.
        """
        # Check input data
        required_fields = [NAME,]
        optional_fields = [DESCRIPTION]
        if not check_api_input_data(request, required_fields, optional_fields):
            return Response(status=status.HTTP_400_BAD_REQUEST, exception=True, data=INVALID_INPUT_DATA_MSG)

        # Send data to serializer
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return BaseResponse(
                message=INVALID_INPUT_DATA_MSG,
                data={DETAILS: serializer.errors},
                is_exception=True,
                http_status_code=status.HTTP_400_BAD_REQUEST,
                business_status_code=BUSINESS_STATUS.INVALID_INPUT_DATA,
            )

        # Create task
        serializer.save()
        return BaseResponse(
            message=TASK_CREATED_MSG,
            data=serializer.data,
            is_exception=False,
            http_status_code=status.HTTP_201_CREATED,
            business_status_code=BUSINESS_STATUS.SUCCESS
        )

    def update(self, request, pk=None, *args, **kwargs):
        """
        Update a project by ID.

        PUT /projects/<id>/

        Parameters
        ----------
        request : Request
            The HTTP request object containing the updated data for the project.
        pk : int
            The primary key of the project to update.

        Returns
        -------
        Response
            A response object containing the updated project's details.
        """
        project = self.get_object()
        serializer = self.get_serializer(project, data=request.data, partial=True)
        if not serializer.is_valid():
            return BaseResponse(
                message=INVALID_INPUT_DATA_MSG,
                data={DETAILS: serializer.errors},
                is_exception=True,
                http_status_code=status.HTTP_400_BAD_REQUEST,
                business_status_code=BUSINESS_STATUS.INVALID_INPUT_DATA,
            )

        # Update project
        serializer.save()
        return BaseResponse(
            message=TASK_UPDATED_MSG,
            data=serializer.data,
            is_exception=False,
            http_status_code=status.HTTP_200_OK,
            business_status_code=BUSINESS_STATUS.SUCCESS
        )

    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Delete a project by ID.

        DELETE /projects/<id>/

        Parameters
        ----------
        request : Request
            The HTTP request object.
        pk : int
            The primary key of the project to delete.

        Returns
        -------
        Response
            A response object confirming the deletion.
        """
        project = self.get_object()
        project.delete()
        return BaseResponse(
            message=TASK_DELETED_MSG,
            data=None,
            is_exception=False,
            http_status_code=status.HTTP_204_NO_CONTENT,
            business_status_code=BUSINESS_STATUS.SUCCESS
        )

    @action(detail=True, methods=[GET, POST],)
    def comments(self, request, pk=None):
        task = Task.objects.get(pk=pk)
        if request.method == GET:
            comments = Comment.objects.filter(task=task)
            return BaseResponse(
                http_status_code=status.HTTP_200_OK,
                business_status_code=BUSINESS_STATUS.SUCCESS,
                data=comments,
                is_exception=False,
                message=None
            )
        elif request.method == POST:
            # Check input data
            required_fields = [TASK, AUTHOR, CONTENT]
            if not check_api_input_data(request, required_fields):
                return Response(status=status.HTTP_400_BAD_REQUEST, exception=True, data=INVALID_INPUT_DATA_MSG)

            # Send data to serializer
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return BaseResponse(
                    message=INVALID_INPUT_DATA_MSG,
                    data={DETAILS: serializer.errors},
                    is_exception=True,
                    http_status_code=status.HTTP_400_BAD_REQUEST,
                    business_status_code=BUSINESS_STATUS.INVALID_INPUT_DATA,
                )
            # Create comment
            serializer.save()
            return BaseResponse(
                message=COMMENT_CREATED_MSG,
                data=serializer.data,
                is_exception=False,
                http_status_code=status.HTTP_201_CREATED,
                business_status_code=BUSINESS_STATUS.SUCCESS
            )
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, exception=True, data=None)