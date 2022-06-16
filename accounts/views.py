from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.


def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        # print(request.method)
        # print(request.POST)
        # Process the data from the form
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # user = form.save()
            # # Save the data to the database
            username = request.POST["username"]
            password = request.POST["password1"]
            user = User.objects.create_user(
                username=username, password=password
            )
            user.save()
            login(request, user)
            # Log the user in
            # Maybe redirect somewhere?
            return redirect("home")
        # Show blank form
    context = {
        "form": form,
    }
    return render(request, "registration/signup.html", context)
