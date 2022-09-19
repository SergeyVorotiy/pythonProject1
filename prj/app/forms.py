from django import forms

from .models import FileWordCounts


class FileForm(forms.ModelForm):
    class Meta:
        model = FileWordCounts
        fields = [
            'file',
        ]



