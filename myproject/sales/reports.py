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


@register_report_view
class ProductSalesMonthly(ReportView):
    report_title = _('Product Sales Monthly')

    base_model = Product
    report_model = SimpleSales

    form_settings = {
        'group_by': 'product',
        'group_columns': ['slug', 'title'],

        # how we made the report a time series report
        'time_series_pattern': 'monthly',
        'time_series_fields': ['__balance_quan__', '__balance__'],
    }

    swap_sign = True

    chart_settings = [
        {
            'id': 'movement_column_total',
            'title': _('comparison - Bar - Total'),
            'data_source': '__balance__',
            'title_source': 'product__title',
            'type': 'bar',
            'plot_total': True,
        },
        {
            'id': 'movement_column_ns',
            'title': _('comparison - Bar'),
            'data_source': '__balance__',
            'title_source': 'product__title',
            'type': 'bar',
            'stacked': False,
        },
        {
            'id': 'movement_bar',
            'title': _('comparison - Bar - Stacked'),
            'data_source': '__balance__',
            'title_source': 'product__title',
            'type': 'bar',
            'stacked': True,
        },
        {
            'id': 'movement_line_total',
            'title': _('comparison - line - Total'),
            'data_source': '__balance__',
            'title_source': 'product__title',
            'type': 'line',
            'plot_total': True,
        },
        {
            'id': 'movement_line',
            'title': _('comparison - line'),
            'data_source': '__balance__',
            'title_source': 'product__title',
            'type': 'line',
        },
        {
            'id': 'movement_line_stacked',
            'title': _('comparison - line - Stacked'),
            'data_source': '__balance__',
            'title_source': 'product__title',
            'type': 'line',
            'stacked': True,
        },
    ]


@register_report_view
class ClientSalesMonthlySeries(ReportView):
    report_title = _('Client Sales Monthly')

    base_model = Client
    report_model = SimpleSales

    form_settings = {
        'group_by': 'client',
        'group_columns': ['slug', 'title'],

        'time_series_pattern': 'monthly',
        'time_series_fields': ['__balance__'],
    }


@register_report_view
class ProductClientSalesMatrix(ReportView):
    base_model = Product
    report_model = SimpleSales
    report_title = _('Product Client sales Cross-tab')

    form_settings = {
        'group_by': 'product',
        'group_columns': ['slug', 'title'],

        # cross tab settings
        'matrix': 'client',
        'matrix_columns': ['__total__'],

    }

    # sales decreases our product balance, accounting speaking,
    # but for reports sometimes we need the value sign reversed.
    swap_sign = True
