from django.contrib.auth.forms import UserCreationForm

from diary.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Приведение формы отображения для заполнения"""

    class Meta:
        model = User
        fields = ("email", "password1", "password2")
