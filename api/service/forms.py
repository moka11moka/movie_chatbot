from toolbox.api.forms.forms import forms, BaseCreateAPIForm
from api.service.dictionaries import ServiceDictionary


class ServiceForm(BaseCreateAPIForm):

    message = forms.CharField(required=True)

    def clean(self):
        super(ServiceForm, self).clean()
        self.message = self.cleaned_data.get("message", None)

    def save(self):
        return dict(content=ServiceDictionary.get_item(self.message))
