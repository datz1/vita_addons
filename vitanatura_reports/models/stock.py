# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class StockMove(models.Model):
    _inherit = "stock.move"

    lot_id = fields.Char(string="Lots", compute='_get_lots_move_line', store=True)

    @api.depends('move_line_ids')
    def _get_lots_move_line(self):
        for record in self:
            lot_ids = record.move_line_ids.mapped('lot_id')
            if lot_ids:
                record.lot_id = ', '.join(lot_ids.mapped('name'))


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def get_barcode_view_state(self):
        """"
            Overridden to add 'loc_rack', 'loc_raw' fields to product fields dictionary .
            - The context 'read_loc' is checked in 'product.product' read method .
        """
        return super(StockPicking, self.with_context(read_loc=True)).get_barcode_view_state()
