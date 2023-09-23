from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label = "", widget=forms.TextInput(attrs={'Class':'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={'Class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={'Class':'form-control','placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'format-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span_class="form-text text-muted"><small>Required. 150 characters or fewer digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'format-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li><Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your passwords can\'t be a commonly used password. </li><li>Your passwords can\'t be entirely numeric. </li><ul>'

        self.fields['password2'].widget.attrs['class'] = 'format-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted small"><li><Your password has to be the same as before, for verification.</small></span>'