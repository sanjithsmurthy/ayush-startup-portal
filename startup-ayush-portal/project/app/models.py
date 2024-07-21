from django.db import models
from django.contrib.postgres.fields import JSONField

class Animation(models.Model):
    name = models.CharField(max_length=255)
    data = JSONField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']