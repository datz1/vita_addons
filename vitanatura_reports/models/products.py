from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    loc_rack = fields.Char("Regal")
    loc_row = fields.Char("Zeile")


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.multi
    def read(self, fields=None, load='_classic_read'):
        add_loc = self.env.context.get('read_loc', False)
        if add_loc and fields:
            fields.append('loc_rack')
            fields.append('loc_row')
        return super(ProductProduct, self).read(fields=fields, load=load)
