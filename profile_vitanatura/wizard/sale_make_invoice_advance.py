# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    @api.model
    def _default_can_be_invoiced(self):
        """"
        Check if the ordered quantities are available in stock (storable products), and prevent the invoicing if
        some products are not available.
        """
        order_ids = self.env['sale.order'].browse(self.env.context['active_ids'])
        if not all(sale.ready_to_invoice for sale in order_ids):
            raise UserError(_("Sorry, "
                              "you can't create an invoice if some ordered products are not yet available in stock!"))
        return True

    can_be_invoiced = fields.Boolean(help='Check if the active orders can be invoiced', default=_default_can_be_invoiced)

