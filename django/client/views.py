from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.contrib.auth.views import LoginView

# Create your views here.
def redirect_to_account(request):
    if request.user.is_authenticated:
        return redirect('/user/'+request.user.username+'/')
    if request.method == "POST":
        form = RegisterForm(request. POST)
        if form.is_valid():
            form.save()
            return redirect('/user/login/')
    else:
        form = RegisterForm()
    return render(request, "client/register.html", {"form":form})

@csrf_protect    
def loggovia(request):
    if request.method == 'GET':
        logout(request)
        # Redirect to a success page or home page
        return redirect('/user/')
    else:
        # Handle other HTTP methods like GET, if necessary
        # In this case, you may render a form with a CSRF token
        pass

def user_page(request, name):
    return render(request, "client/userPage.html")
    # my_vars = {"name":name}       #qui ci posso mettere anche tutto un oggetto e me lo ritrovo accessibile nel http e posso usarlo direttamente li

    # html_response = """
    # <html>
    # <head><title>Home Page</title></head>
    # <body>
    # <h1>Ciao {name} - default</h1>
    # <a href="{% url 'logout' %}">Logout now</a>
    # </body>
    # </html>
    # """.format(**my_vars)

    # return HttpResponse(html_response)

def test_page(request):
    html_response = """
    <html>
    <head><title>Home Page</title></head>
    <body>
    <h1>Test - default</h1>
    </body>
    </html>
    """
    return HttpResponse(html_response)

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
        return super().form_valid(form)