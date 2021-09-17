# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = 'res.company'
    
    street_number = fields.Char(string='Street number', required=True)
    country_id = fields.Many2one(required=True)