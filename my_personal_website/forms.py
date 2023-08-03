from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(max_length=200, required=True)
    subject = forms.CharField(max_length=500, required=True)
    text = forms.CharField(max_length=10000, required=True)

    def __str__(self):
        return self.name
