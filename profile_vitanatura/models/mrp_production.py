from odoo import fields, models, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.model
    def _get_default_picking_type(self):
        """ Get picking type by name = 'Manufacturing Production' else call super. """

        # Get picking type by name
        picking_type_id = self.env['stock.picking.type'].search([
            ('code', '=', 'mrp_operation'),
            ('name', '=', 'Manufacturing Produktionslager')
        ], limit=1).id

        # When no picking type was found, return the default function
        if not picking_type_id:
            return super(MrpProduction, self)._get_default_picking_type()

        # Return picking type
        return picking_type_id

    picking_type_id = fields.Many2one(default=_get_default_picking_type)
