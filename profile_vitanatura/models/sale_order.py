# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    ready_to_invoice = fields.Boolean(string='Ready to invoice', compute='check_invoicing_possibility',
                                      help='Check if the order can be invoiced', store=True, readonly=1)

    @api.depends('order_line.move_ids.state', 'invoice_status')
    def check_invoicing_possibility(self):
        """"
        Check if all ordered quantities (storable products) are available in stock.
        """
        for order in self:
            ready_to_invoice = False

            if order.invoice_status in ['to invoice', 'upselling']:
                move_ids = order.mapped('order_line.move_ids')
                if all(move.state in ['assigned', 'done', 'cancel'] for move in move_ids) or not move_ids:
                    ready_to_invoice = True
            order.ready_to_invoice = ready_to_invoice


