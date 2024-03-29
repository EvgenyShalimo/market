from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Wallet, PurchaseHistory


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Wallet.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/registr.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


@login_required(login_url='/users/login/')
def logout_view(request):
    logout(request)
    return redirect('/')


# Выводит бланс пользователя
@login_required(login_url='/users/login/')
def user_balance(request):
    user = request.user

    try:
        wallet = Wallet.objects.get(user=user)
        balance = wallet.balance
    except Wallet.DoesNotExist:
        # Обработка случая, когда кошелек не существует
        balance = 0

    purchase_history = PurchaseHistory.objects.filter(user=user)

    context = {
        'balance': balance,
        'purchase_history': purchase_history
    }
    return render(request, 'users/balance.html', context)






