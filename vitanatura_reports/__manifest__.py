# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.
{
    'name': 'VitaNatura Reports',
    'version': '12.0.1.0.0',
    'author': 'Hucke Media GmbH & Co. KG/IFE GmbH',
    'category': 'Custom',
    'website': 'https://www.hucke-media.de/',
    'licence': 'AGPL-3',
    'summary': 'Customizations for Reports Vita Natura',
    'depends': [
        'base',
        'sale',
        'stock',
        'stock_barcode',
    ],
    'data': [
        'reports/layout.xml',
        'reports/report_deliveryslip.xml',
        'reports/report_invoice_document.xml',
        'views/products_views.xml',
        'views/stock_move_views.xml',
    ],
    'qweb': [
        'static/src/xml/qweb_templates.xml',
    ],
    'installable': True,
    'application': False,
}
