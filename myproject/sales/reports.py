from django.utils.translation import ugettext_lazy as _
from ra.reporting.decorators import register_report_view
from ra.reporting.views import ReportView
from .models import Client, SimpleSales, Product


@register_report_view
class ClientTotalBalance(ReportView):
    report_title = _('Clients Balances')

    base_model = Client
    report_model = SimpleSales

    form_settings = {'group_by': 'client',
                     'group_columns': ['slug', 'title', '__balance__']}
    chart_settings = [
        {
            'id': 'pie_chart',
            'type': 'pie',
            'title': _('Client Balances'),
            'data_source': '__balance__',
            'title_source': 'client__title',
        },
        {
            'id': 'bar_chart',
            'type': 'bar',
            'title': _('Client Balances [Bar]'),
            'data_source': '__balance__',
            'title_source': 'client__title',
        },
    ]


@register_report_view
class ProductTotalSales(ReportView):
    # Title will be displayed on menus, on page header etc...
    report_title = _('Product Sales')

    # What model is this report about
    base_model = Product

    # What model hold the data that we want to compute.
    report_model = SimpleSales

    # The meat and potato of the report.
    # We group the records in SimpleSales by Client ,
    # And we display the columns `slug` and `title` (relative to the `base_model` defined above)
    # the magic field `__balance__` computes the balance (of the base model)
    form_settings = {'group_by': 'product',
                     'group_columns': ['slug', 'title', '__balance__']}


class ClientList(ReportView):
    report_title = _('Our Clients')

    base_model = Client
    report_model = SimpleSales

    # will not appear on the reports menu
    hidden = True

    form_settings = {
        'group_by': 'client',
        'group_columns': ['slug', 'title'],

        # adds + sign in the start of the report table
        'add_details_control': True,
    }


@register_report_view
class ProductClientSales(ReportView):
    report_title = _('Client Sales for each product')

    base_model = Client
    report_model = SimpleSales

    must_exist_filter = 'client_id'
    header_report = ClientList

    form_settings = {
        'group_by': 'product',
        'group_columns': ['slug', 'title', '__balance_quan__', '__balance__'],
    }


@register_report_view
class ClientDetailedStatement(ReportView):
    report_title = _('client Statement')
    base_model = Client
    report_model = SimpleSales

    must_exist_filter = 'client_id'
    header_report = ClientList

    form_settings = {
        'group_columns': ['slug', 'doc_date', 'doc_type', 'product__title', 'quantity', 'price', 'value'],
    }
