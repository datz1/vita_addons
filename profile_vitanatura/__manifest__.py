# -*- coding: utf-8 -*-
{
    'name': 'Profile Vitanatura',
    'version': '12.0.1.0.0',
    'author': 'Hucke Media GmbH & Co. KG/IFE GmbH',
    'category': 'Custom',
    'website': 'https://www.hucke-media.de/',
    'licence': 'AGPL-3',
    'summary': 'Customizations for Vita Natura',
    'depends': [
        'base',
        'mrp',
        'sale_stock',
        'website_sale'
    ],
    'data': [
        'views/mrp_production_views.xml',
        'views/sale_order_views.xml',
        'views/product_template_view.xml',
        'views/website_sale_templates.xml',
        'wizard/sale_make_invoice_advance_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}
