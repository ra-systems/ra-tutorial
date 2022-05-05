from django.db import models
from ra.base.models import EntityModel, TransactionModel, TransactionItemModel, QuantitativeTransactionItemModel
from ra.base.registry import register_doc_type
from django.utils.translation import gettext_lazy as _


class Product(EntityModel):
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

class Client(EntityModel):
    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')


class Expense(EntityModel):
    class Meta:
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')


class ExpenseTransaction(TransactionItemModel):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Expense Transaction')
        verbose_name_plural = _('Expense Transactions')


class SalesTransaction(TransactionModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Sale')
        verbose_name_plural = _('Sales')


class SalesLineTransaction(QuantitativeTransactionItemModel):
    sales_transaction = models.ForeignKey(SalesTransaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Sale Transaction Line')
        verbose_name_plural = _('Sale Transaction Lines')