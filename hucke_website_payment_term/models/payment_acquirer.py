from odoo import models, fields


class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    payment_term_id = fields.Many2one('account.payment.term', 'Payment Terms')
