from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from toolbox.api.constants.message import *
from toolbox.api.response import APIResponse


class BasePagination(PageNumberPagination):

    page_size = 30

    def get_pagination(self):
        return dict(total_pages=self.page.paginator.num_pages, current_page=self.page.number)


class BaseAPIView:

    def __init__(self):
        super(BaseAPIView, self).__init__()
        self.request, self.response, self.form = None, dict(), None

    def get_parameter_data(self):
        return self.request.GET if not self.request.data else self.request.data

    def get_success_message(self):
        return ''

    def get_error_message(self):
        return ''

    def additional_queryset(self):
        pass


class BaseCreateAPIView(BaseAPIView, CreateAPIView):
    create_form, is_create_serializer = None, True
    create_success_message, create_error_message = ADD_SUCCESS, ADD_ERROR

    def __init__(self, *args, **kwargs):
        super(BaseCreateAPIView, self).__init__(*args, **kwargs)

    def get_create_form(self):
        if not self.create_form:
            return None
        return self.create_form(self.get_parameter_data(), self.request.FILES, request=self.request)

    def create(self, request, *args, **kwargs):
        self.form, response_data = self.get_create_form(), dict()
        if self.form.is_valid():
            instance = self.form.save()
            if self.is_create_serializer:
                serializer = self.get_serializer(instance)
                response_data = dict(object=serializer.data)
            self.response = APIResponse.success_response(response_data, message=self.get_success_message())
        else:
            self.response = APIResponse.error_response(errors=self.form.errors, message=self.get_error_message())
        self.additional_queryset()
        return Response(self.response)

    def get_success_message(self):
        if self.create_form is None:
            return self.create_success_message
        return self.form.get_success_message()

    def get_error_message(self):
        if self.create_form is None:
            return self.create_error_message
        return self.form.get_error_message()

