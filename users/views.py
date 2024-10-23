from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/user_form.html'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False