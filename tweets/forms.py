from django import forms

from .models import tweet

class TweetModelForm(forms.ModelForm):
    content=forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': "What's Today?","class":"form-control",'style':'resize:none;', 'rows':'6','cols':'22'}))
    class Meta:
        model=tweet
        fields=[
           # "user",
            "content"
        ]

    def clean_content(self, *args, **kwargs):
        content=self.cleaned_data.get("content")
        if content=="abc":
            raise forms.ValidationError("Cannot be abc")
        return content