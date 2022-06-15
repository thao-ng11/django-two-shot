from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from receipts.models import Account, ExpenseCategory, Receipt

# Create your views here.

# class ExpenseCategoryListView(ListView):
#     model = ExpenseCategory
#     template_name = "receipts/list.html"
#     paginate_by = 2


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipts/list.html"
    paginate_by = 2

    def get_queryset(self):
        return Receipt.objects.filter()


# class AccountListView(ListView):
#     model = Account
#     template_name = "receipts/list.html"
#     paginate_by = 2
