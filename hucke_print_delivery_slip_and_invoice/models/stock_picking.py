from odoo import api, fields, models


class Picking(models.Model):
    _inherit = "stock.picking"

    def do_print_invoice(self):
        """
        Create, validate and print Invoice.
        """

        self.ensure_one()

        # Only when picking is outgoing and has a sale order
        if self.picking_type_code == "outgoing" and self.sale_id:

            # Create Invoices
            invoice_ids = self.sale_id.action_invoice_create()

            # Get Invoices
            invoices = self.env["account.invoice"].browse(invoice_ids)

            # Validate Invoices
            invoices.action_invoice_open()

            return invoices.invoice_print()

        return self



    def do_print_delivery(self):
        """
        Print Delivery Slip.
        """

        self.ensure_one()

        return self.env.ref('stock.action_report_delivery').report_action(self)

    def button_invoice_and_print(self):
        """
        Action for Invoice & Print Button.
        """

        return self
