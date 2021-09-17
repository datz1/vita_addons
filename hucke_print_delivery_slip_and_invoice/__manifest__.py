{
    'name': 'hucke_print_delivery_slip_and_invoice',
    'version': '12.0.1.0.0',
    'summary': 'Prints Delivery Slip and Invoice when validating a delivery order',
    'category': 'Sale',
    'author': 'Tom Kramer, Hucke Media Gmbh & Co KG',
    'website': 'https://www.hucke-media.de',
    'license': 'AGPL-3',
    'depends': [
        'stock',
        'sale_stock'
    ],
    'data': [
        'views/stock_picking_views.xml'
    ]
}
