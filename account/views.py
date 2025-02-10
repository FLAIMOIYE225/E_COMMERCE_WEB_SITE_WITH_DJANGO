from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login, authenticate, logout, get_user

User = get_user_model()

# Create your views here.

def signUp(request):

    user = get_user(request)


    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        userEmail = request.POST.get('email')

        print(f'---------------------------------------------------------------------------------------------------------------------------------------------------------------------- {username} {password}')

        user = User.objects.create_user(username=username, email=userEmail, password=password)

        login(request, user)

        return redirect('index')
    
    if user.is_authenticated :
        return redirect('index')

    return render(request, 'account/signupPage.html')



def login_user(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user :
        login(request, user)
        return redirect('index')
    
    return redirect(to='signUp')



def disconnect_user(request):

    logout(request)

    return redirect('signUp')