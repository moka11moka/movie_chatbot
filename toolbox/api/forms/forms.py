from django import forms


class BaseAPIForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.request, self.instance = kwargs.pop('request', None), kwargs.pop('instance', None)
        super(BaseAPIForm, self).__init__(*args, **kwargs)
        self.context = dict(request=self.request)

    def update_context(self, context):
        self.context.update(context)


class BaseListAPIForm(BaseAPIForm):

    model = None

    def __init__(self, *args, **kwargs):
        super(BaseListAPIForm, self).__init__(*args, **kwargs)
        self.object_list = []

    @classmethod
    def get_all(cls, include=None):
        object_list = cls.model.objects.all().is_deleted(False) if cls.model is not None else []
        if isinstance(include, list):
            object_list = object_list.pks(include)
        return object_list


class BaseRetrieveAPIForm(BaseAPIForm):

    model = None

    def __init__(self, *args, **kwargs):
        super(BaseRetrieveAPIForm, self).__init__(*args, **kwargs)
        self.instance = None

    def clean(self):
        super(BaseRetrieveAPIForm, self).clean()
        self.instance = self.cleaned_data.get('pk')

    def get_object(self):
        return self.instance

    @classmethod
    def get_object_by_pk(cls, pk):
        return cls.model.objects.get_one_by_pk(pk)


class BaseCreateAPIForm(BaseAPIForm):

    def get_success_message(self):
        return ""

    def get_error_message(self):
        return ""


class BaseUpdateAPIForm(BaseAPIForm):

    def is_valid(self):
        valid = super(BaseUpdateAPIForm, self).is_valid()
        if not isinstance(self.instance, self.model):
            return False

        return valid

    def get_success_message(self):
        return ""

    def get_error_message(self):
        return ""


class BaseDeleteAPIForm(BaseAPIForm):

    model = None

    def clean(self):
        super(BaseDeleteAPIForm, self).clean()
        self.instance = self.cleaned_data.get('instance', None)

    def save(self):
        if isinstance(self.instance, self.model):
            return self.perform_delete()

    def perform_delete(self):
        return self.instance.delete()

    def get_success_message(self):
        return ""

    def get_error_message(self):
        return ""


class BaseAPIModelForm(forms.ModelForm):

    INVALID_FIELD_UNIQUE = "The %s is already used"

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(BaseAPIModelForm, self).__init__(*args, **kwargs)
        self.context, self.error_list = dict(request=self.request), []

    @classmethod
    def make_error_message(cls, message, field_names):
        return message % field_names


class BaseCreateAPIModelForm(BaseAPIModelForm):

    def get_success_message(self):
        return ""

    def get_error_message(self):
        return ""


class BaseUpdateAPIModelForm(BaseAPIModelForm):

    def is_valid(self):
        valid = super(BaseUpdateAPIModelForm, self).is_valid()
        if self.instance is None or self.instance.id is None:
            return False

        return valid

    def get_success_message(self):
        return ""

    def get_error_message(self):
        return ""




