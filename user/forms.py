from django import forms
from allauth.account.forms import SignupForm
from .models import CustomUser


class RegistrationForm(SignupForm):

    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")


    def save(self, request):
        user = super(RegistrationForm, self).save(request)
        user.save()

        return user