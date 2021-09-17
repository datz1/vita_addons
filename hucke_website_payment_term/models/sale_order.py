# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    acquirer_id = fields.Many2one('payment.acquirer', string='Acquirer')

    # @api.multi
    def _create_payment_transaction(self, vals):
        transaction = super(SaleOrder, self)._create_payment_transaction(vals)
        if transaction.acquirer_id:
            if transaction.acquirer_id.payment_term_id:
                self.write({'payment_term_id': transaction.acquirer_id.payment_term_id.id,
                            'acquirer_id': transaction.acquirer_id.id})
            else:
                self.write({'acquirer_id': transaction.acquirer_id.id})
        return transaction
