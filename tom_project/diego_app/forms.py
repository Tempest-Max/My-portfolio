# forms.py (optional, if you want a custom form for contact messages)
from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@example.com', 'class': 'form-input'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Project Proposal', 'class': 'form-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Hello and Goodbye', 'class': 'form-textarea', 'rows': 4}),
        }