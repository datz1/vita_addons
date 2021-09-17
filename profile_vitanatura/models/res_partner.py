# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    street_number = fields.Char(required=True)
    country_id = fields.Many2one(required=True)
    
    
    @api.constrains('vat')
    def check_vat(self):
        return False

    @api.model
    def create(self, vals):
        res = super(ResPartner, self).create(vals)
        if res.type == 'delivery':
            res.email = res.parent_id.email
        return res

    @api.multi
    def write(self, vals):
        for record in self:
            if record.type == 'delivery':
                vals['email'] = record.parent_id.email
        return super(ResPartner, self).write(vals)