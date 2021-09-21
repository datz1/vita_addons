# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (C) 2017 by Hucke Media GmbH & Co. KG/IFE GmbH <http://www.hucke-media.de>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

from odoo import api, fields, models


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    weight_distribution = fields.Selection('get_type_selection', 'Weight Distribution', required=True,
                                           default='equal_weight')
    max_weight = fields.Float(string='Max Weight')

    @api.model
    def get_type_selection(self):
        return [('equal_weight', 'Equal weight distribution'), ('equal_weight_plus', 'Max Weight by pack plus rest'),
                ('max_weight', 'Fixed Amount')]
