from django.forms import ModelForm, TextInput, EmailInput, Select, DateInput
from base.models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "email", 'last_name', 'birthday', 'city', 'phone_number', 'study', 'address', 'level',
                  'school']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prénom'
            }),

            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Émail',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prénom'
            }),
            'city': TextInput(attrs={
                'class': 'form-control',
                'list': 'ville_list',
                'placeholder': 'ville',
                'autocomplete': "off"
            }),
            'birthday': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'phone_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Téléphone',
                'type': 'tel'
            }),
            'address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Adresse',

            }),
            'school': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'École',
                }),

            'study': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Étude',
                    'list': 'etude_list',
                    'autocomplete': "off"
                }),
            'level': Select(attrs={
                'class': 'form-control',
            })
        }

    def clean(self):

        # data from the form is fetched using super function
        super(StudentForm, self).clean()

        # extract the username and text field from the data
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        # conditions to be met for the username length
        if len(first_name) < 2:
            self._errors['first_name'] = self.error_class([
                'Minimum 3 characters required'])
        if len(last_name) < 2:
            self._errors['last_name'] = self.error_class([
                'Post Should Contain a minimum of 10 characters'])

        # return any errors if found
        return self.cleaned_data
