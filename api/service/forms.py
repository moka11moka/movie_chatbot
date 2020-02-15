from toolbox.api.forms.forms import forms, BaseCreateAPIForm
from api.service.dictionaries import ServiceDictionary
from api.service.conversation.demo import serviceChatBot


class ServiceForm(BaseCreateAPIForm):

    content = forms.CharField(required=True)

    def clean(self):
        super(ServiceForm, self).clean()
        self.content = self.cleaned_data.get("content", None)

    def save(self):
        return dict(content=ServiceDictionary.get_item(self.content))
