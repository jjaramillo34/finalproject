
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from user.forms import CustomAuthenticationForm, CustomUserCreationForm, UpdateProfileForm, UpdateUserForm, UserRegisterForm, UserEditForm, AvatarForm
from user.models import Avatar
from django.urls import reverse_lazy

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalCreateView
)

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm

class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'user/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('user:login')

class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'user/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('blog:home')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente!")
            return redirect("user:user-login")
    form = UserRegisterForm()
    return render(
        request=request,
        context={"form":form},
        template_name="user/register.html",
    )


#def login_request(request):
#    if request.method == "POST":
#        form = AuthenticationForm(request, data=request.POST)
#        if form.is_valid():
#            username = form.cleaned_data.get('username')
#            password = form.cleaned_data.get('password')
#            user = authenticate(username=username, password=password)
#            if user is not None:
#                login(request, user)
#                return redirect("home:main")
#
#        return render(
#            request=request,
#            context={'form': form},
#            template_name="user/login.html",
#        )
#
#    form = AuthenticationForm()
#    return render(
#        request=request,
#        context={'form': form},
#        template_name="user/login.html",
#    )


def logout_request(request):
      logout(request)
      return redirect("blog:home")


#@login_required
#def user_update(request):
#    user = request.user
#    if request.method == 'POST':
#        form = UserEditForm(request.POST, instance=request.user)
#        if form.is_valid():
#            form.save()
#
#            return redirect('home:main')
#
#    form= UserEditForm(model_to_dict(user))
#    return render(
#        request=request,
#        context={'form': form},
#        template_name="user/user_form.html",
#    )
#
#
#@login_required
#def avatar_load(request):
#    if request.method == 'POST':
#        form = AvatarForm(request.POST, request.FILES)
#        if form.is_valid  and len(request.FILES) != 0:
#            image = request.FILES['image']
#            avatars = Avatar.objects.filter(user=request.user.id)
#            if not avatars.exists():
#                avatar = Avatar(user=request.user, image=image)
#            else:
#                avatar = avatars[0]
#                if len(avatar.image) > 0:
#                    os.remove(avatar.image.path)
#                avatar.image = image
#            avatar.save()
#            messages.success(request, "Imagen cargada exitosamente")
#            return redirect('home:main')
#
#    form= AvatarForm()
#    return render(
#        request=request,
#        context={"form": form},
#        template_name="user/avatar_form.html",
#    )

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'user/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='blog:home')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('blog:home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'user/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('blog:home')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was updated successfully')
            return redirect(to='user:user-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'user/profile.html', {'user_form': user_form, 'profile_form': profile_form})
