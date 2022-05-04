from .models import Client, Product, Expense, ExpenseTransaction, SalesLineTransaction, SalesTransaction
from ra.admin.admin import ra_admin_site, EntityAdmin, TransactionAdmin, TransactionItemAdmin


class ExpenseAdmin(EntityAdmin):
    pass


class ProductAdmin(EntityAdmin):
    pass


class ClientAdmin(EntityAdmin):
    pass


class SalesLineAdmin(TransactionItemAdmin):
    fields = ('product', 'price', 'quantity', 'value')
    model = SalesLineTransaction


class SalesOrderAdmin(TransactionAdmin):
    inlines = [SalesLineAdmin]
    fields = ['slug', 'doc_date', 'client', ]
    copy_to_formset = ['client']


ra_admin_site.register(Client, ClientAdmin)
ra_admin_site.register(Product, ProductAdmin)
ra_admin_site.register(Expense, ExpenseAdmin)
ra_admin_site.register(SalesTransaction, SalesOrderAdmin)