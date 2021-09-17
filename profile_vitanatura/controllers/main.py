# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):
    
       
    def _checkout_form_save(self, mode, checkout, all_values):
        Partner = request.env['res.partner']
        if mode[0] == 'new':
            checkout['street_name'] = all_values.get('street', False)
            checkout['street_number'] = all_values.get('street_number', False)
            name = all_values.get('name')
            partner_id = int(all_values.get('partner_id', 0))
            partner = Partner.sudo().search([('id', '=', partner_id)], limit=1)
            if partner:
                partner.sudo().write(checkout)
            else:
                partner_id = Partner.sudo().create(checkout).id
        elif mode[0] == 'edit':
            partner_id = int(all_values.get('partner_id', 0))
            if partner_id:
            #double check
                order = request.website.sale_get_order()
                shippings = Partner.sudo().search([("id", "child_of", order.partner_id.commercial_partner_id.ids)])
                if partner_id not in shippings.mapped('id') and partner_id != order.partner_id.id:
                    return Forbidden()
                checkout['street_number'] = all_values.get('street_number', False)
                checkout['street_name'] = all_values.get('street', False)
                Partner.browse(partner_id).sudo().write(checkout)        
        return  partner_id

    
    @http.route(['/shop/payment/transaction/',
        '/shop/payment/transaction/<int:so_id>',
        '/shop/payment/transaction/<int:so_id>/<string:access_token>'], type='json', auth="public", website=True)
    def payment_transaction(self, acquirer_id, save_token=False, so_id=None, access_token=None, token=None, **kwargs):    
        # Retrieve the sale order
        if so_id:
            env = request.env['sale.order']
            domain = [('id', '=', so_id)]
            if access_token:
                env = env.sudo()
                domain.append(('access_token', '=', access_token))
            order = env.search(domain, limit=1)
        else:
            order = request.website.sale_get_order()
        domain=[('name','=','Kauf auf Rechnung')]
        acquirer_ids = request.env['payment.acquirer'].search(domain).id
        if acquirer_id == acquirer_ids:
            order.action_confirm()
            order.force_quotation_send()
        return super(WebsiteSale, self).payment_transaction(acquirer_id,so_id) 