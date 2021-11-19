from django.forms import ModelForm, TextInput, EmailInput, Select, DateInput
from base.models import Newsletter


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email"]
        widgets = {
            'email': EmailInput(attrs={
                'class': 'form-control mr-3',
                'placeholder': 'Émail',
            }),

        }

    def clean(self):

        # data from the form is fetched using super function
        super(NewsletterForm, self).clean()

        # return any errors if found
        return self.cleaned_data
