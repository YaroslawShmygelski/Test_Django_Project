from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import LoginForm, RegistrationForm, UserProfileForm


# Create your views here.
# def login_users(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'],
#                                 password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#     else:
#         form = LoginForm()
#
#     return render(request, 'users/login.html', {'form': form})

class LoginUsers(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    # def get_success_url(self):
    #     return reverse_lazy('home')


#
# def logout_users(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('users:login'))

class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = 'users/register.html'
    extra_context = {'title': "Registration"}
    success_url = reverse_lazy('users:login')


# def register_user(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return render(request, 'users/register_done.html')
#     else:
#         form = RegistrationForm()
#     return render(request, 'users/register.html', context={'form': form})


class UserProfile(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = 'users/user_profile.html'
    extra_context = {'title': "Profile"}

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
