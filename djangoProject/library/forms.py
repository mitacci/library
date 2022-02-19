from django import forms
from django.forms import TextInput

from djangoProject.library.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }
        widgets = {
            'first_name': TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'image_url': TextInput(
                attrs={
                    'placeholder': 'URL',
                }
            ),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }


class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class EditBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


