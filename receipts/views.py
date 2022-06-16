from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from receipts.models import Account, ExpenseCategory, Receipt

# Create your views here.

# class ExpenseCategoryListView(ListView):
#     model = ExpenseCategory
#     template_name = "receipts/list.html"
#     paginate_by = 2


# class AccountListView(ListView):
#     model = Account
#     template_name = "receipts/list.html"
#     paginate_by = 2


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipts/list.html"

    def get_queryset(self):
        return Receipt.objects.filter(purchaser=self.request.user)


class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    template_name = "receipts/create.html"
    fields = ["vendor", "total", "tax", "date", "category", "account"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.purchaser = self.request.user
        item.save()
        return redirect("home")
