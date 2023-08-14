from django import forms
from .models import Image, Profile, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ["user", "profile", "likes", "likers"]


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comments",
        ]


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.label = False
            if field_name == "username":
                field.widget = forms.TextInput(attrs={"placeholder": "Username"})
            elif field_name == "password1":
                field.widget = forms.PasswordInput(attrs={"placeholder": "Password"})
            elif field_name == "password2":
                field.widget = forms.PasswordInput(
                    attrs={"placeholder": "Confirm Password"}
                )

    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="Optional",
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "First Name"}),
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="Optional",
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Last Name"}),
    )
    email = forms.EmailField(
        max_length=254,
        help_text="Enter a valid email address",
        label=False,
        widget=forms.EmailInput(attrs={"placeholder": "Email Address"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
