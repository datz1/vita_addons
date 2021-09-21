# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.

from odoo import fields, models


class DeliveryDHLPackageType(models.Model):
    _name = 'delivery.dhl.package.type'

    name = fields.Char('DHL Package Type')
    code = fields.Char('DHL Package Type Code')
