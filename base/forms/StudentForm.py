from django.forms import ModelForm, TextInput, EmailInput, Select, DateInput
from base.models import Student, City, Study


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
                'placeholder': 'Nom'
            }),
            'city': Select(attrs={
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
                    'placeholder': 'Établissement',
                }),

            'study': Select(
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

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.all().order_by('name')
        self.fields['study'].queryset = Study.objects.all().order_by('name')

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
                'Minimum 3 characters required'])

        # return any errors if found
        return self.cleaned_data
