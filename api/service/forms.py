from toolbox.api.forms.forms import forms, BaseCreateAPIForm
from api.service.dictionaries import ServiceDictionary
from api.service.conversation.demo import ServiceChatBot
from src.Movie_main import main


class ServiceForm(BaseCreateAPIForm):

    content = forms.CharField(required=True)

    def clean(self):
        super(ServiceForm, self).clean()
        self.content = self.cleaned_data.get("content", None)

    def save(self):
        result = main(self.content)
        if result == "123":
            object_list = Movie.objects.all().icontains("title")
        return object_list
