# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    base_price = fields.Float(
        'base_price',
        compute='_compute_get_base_price'
    )
    calculation_uom_id = fields.Many2one(
        'uom.uom',
        'Calc. Unit of Measure'
    )
    calculation_qty = fields.Float(
        'Calculation qty',
        default=1
    )
    baseprice_uom_id = fields.Many2one('uom.uom', 'Base Unit of Measure')
    base_qty = fields.Float(
        'Base qty',
        default=1
    )
    baseprice_char = fields.Char(
        'base_price',
        compute='_compute_baseprice_char'
    )

    @api.multi
    def _compute_get_base_price(self):
        for record in self:
            record.base_price = (
                record.list_price /
                (record.calculation_qty or 1) *
                (record.base_qty / record._convert_unit())
            )

    @api.multi
    def _convert_unit(self):
        for record in self:
            if record.baseprice_uom_id:
                if (
                    record.baseprice_uom_id.category_id.id ==
                    record.calculation_uom_id.category_id.id
                ):
                    if (
                        record.baseprice_uom_id.id !=
                        record.calculation_uom_id.id
                    ):
                        uom_factor = record.calculation_uom_id._compute_quantity(
                            1,
                            record.baseprice_uom_id)
                        return uom_factor
                    else:
                        return 1
                else:
                    return 1
            else:
                return 1

    @api.multi
    def _compute_baseprice_char(self):
        for record in self:
            if record.baseprice_uom_id:
                record.baseprice_char = "/" + str('{0:g}'.format(record.base_qty)) + " " + (record.baseprice_uom_id.name or '')

    @api.multi
    @api.constrains('baseprice_uom_id', 'calculation_uom_id')
    def check_baseprice_uom(self):
        for record in self:
            if (
                record.baseprice_uom_id.category_id.id !=
                record.calculation_uom_id.category_id.id
            ):
                raise ValidationError(
                    "Base price UOM and Sale UOM"
                    " must belong to the same category !!"
                )
