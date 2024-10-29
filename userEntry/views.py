from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request, "UserEntry/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        # Add any additional validation for password confirmation here
        if password == confirmpassword:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
                return redirect("signup")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username already registered")
                return redirect("signup")
            else:
                # Create the user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect("signin")

        else:
            messages.error(request, "Passwords do not match")
            return redirect("signup")
    else:
      return render(request, "UserEntry/signup.html")


def SignIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username=username, password=password)
        # user = User.objects.filter(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')  # Redirect to homepage or any other page after login
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('signin')  # Redirect back to sign in on failure

    return render(request, "UserEntry/signin.html")


def SignOut(request):
    # Implement sign-out logic here
    logout(request)  # Logs the user out
    messages.success(request, "You have successfully logged out")
    return redirect('signin')


def my_view(request):
    # Add a message to be displayed
    messages.success(request, 'Your operation was successful!')

    # Prepare context
    context = {
        'messages': messages.get_messages(request),
        'myUser': request.user,
        'fname': request.user.first_name,  # Assuming you want the user's first name
    }

    return render(request, '', context)  # Replace 'my_template.html' with your actual template name