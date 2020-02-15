from toolbox.api.forms.forms import forms, BaseCreateAPIForm
from api.service.conversation.demo import ServiceChatBot


class ServiceForm(BaseCreateAPIForm):

    content = forms.CharField(required=True)

    def clean(self):
        super(ServiceForm, self).clean()
        self.content = self.cleaned_data.get("content", None)

    def save(self):
        return dict(content=ServiceChatBot.get_item(self.content))
