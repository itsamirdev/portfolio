from django import forms

from items.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message'}),
        }

        error_messages = {
            "name": {"required": "Please enter your name."},
            "email": {"required": "Please enter your email."},
            "message": {"required": "Please enter your message."},
        }
