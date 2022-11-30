from django.shortcuts import render
from .models import Transaction
from django.contrib.auth.decorators import login_required


@login_required
def get_transactions(request):
    current_user = request.user
    transactions = Transaction.objects.filter(user=current_user)
    context = {"transactions": transactions}
    return render(request, "transactions/list.html", context)
