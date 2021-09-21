# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2017 Hucke Media GmbH & Co. KG (http://www.hucke-media.com)
#   @author Michael Hucke
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
import csv
from datetime import datetime
from iso3166 import countries
from odoo.addons.base_delivery_carrier_files.csv_writer import UnicodeWriter
from odoo.addons.base_delivery_carrier_files.generator import BaseLine
from odoo.addons.base_delivery_carrier_files.generator import CarrierFileGenerator


class dhlversendenLineVersenden(BaseLine):
    fields = ("reference",
              "send_date",
              "sender_name1",
              "sender_name2",
              "sender_name3",
              "sender_street",
              "sender_housenumber",
              "sender_zip",
              "sender_place",
              "sender_province",
              "sender_country",
              "sender_reference",
              "sender_email",
              "sender_phone",
              "recipient_name1",
              "recipient_name2",
              "recipient_name3",
              "recipient_street",
              "recipient_housenumber",
              "recipient_zip",
              "recipient_place",
              "recipient_province",
              "recipient_country",
              "recipient_reference",
              "recipient_email",
              "recipient_phone",
              "weight",
              "length",
              "width",
              "height",
              "produkt",
              "return_recipient_name1",
              "return_recipient_name2",
              "return_recipient_name3",
              "return_recipient_street",
              "return_recipient_housenumber",
              "return_recipient_zip",
              "return_recipient_place",
              "return_recipient_province",
              "return_recipient_country",
              "return_recipient_email",
              "return_recipient_phone",
              "return_billing_number",
              "billing_number",
              "service_shipping_conf_email_template",
              "service_shipping_conf_email",
              "service_cashondelivery_customerref",
              "service_cashondelivery_amount",
              "service_cashondelivery_iban",
              "service_cashondelivery_bic",
              "service_cashondelivery_payee",
              "service_cashondelivery_bankname",
              "service_cashondelivery_usage1",
              "service_cashondelivery_usage2",
              "service_transportversicherung_amount",
              "service_worldpackage_sendertype",
              "service_advance_booking",
              "service_DHLEuropaket_frankaturtyp",
              "shipment_declaration",
              "shipment_invoice",
              "shipment_approv_number",
              "shipment_cert_number",
              "shipment_consignment",
              "shipment_description",
              "shipment_charges",
              "shipment_netweight",
              "shipment_description_wp1",
              "shipment_quantity_wp1",
              "shipment_custom_valuation_wp1",
              "shipment_country_of_origin_wp1",
              "shipment_customs_commodity_code_wp1",
              "shipment_weight_wp1",
              "shipment_description_wp2",
              "shipment_quantity_wp2",
              "shipment_custom_valuation_wp2",
              "shipment_country_of_origin_wp2",
              "shipment_customs_commodity_code_wp2",
              "shipment_weight_wp2",
              "shipment_description_wp3",
              "shipment_quantity_wp3",
              "shipment_custom_valuation_wp3",
              "shipment_country_of_origin_wp3",
              "shipment_customs_commodity_code_wp3",
              "shipment_weight_wp3",
              "shipment_description_wp4",
              "shipment_quantity_wp4",
              "shipment_custom_valuation_wp4",
              "shipment_country_of_origin_wp4",
              "shipment_customs_commodity_code_wp4",
              "shipment_weight_wp4",
              "shipment_description_wp5",
              "shipment_quantity_wp5",
              "shipment_custom_valuation_wp5",
              "shipment_country_of_origin_wp5",
              "shipment_customs_commodity_code_wp5",
              "shipment_weight_wp5",
              "shipment_description_wp6",
              "shipment_quantity_wp6",
              "shipment_custom_valuation_wp6",
              "shipment_country_of_origin_wp6",
              "shipment_customs_commodity_code_wp6",
              "shipment_weight_wp6",
              "sending_ref_return",
              "sender_adress_add1",
              "sender_adress_add2",
              "sender_delivery_information",
              "sender_contact_person",
              "recipient_adress_add1",
              "recipient_adress_add2",
              "recipient_delivery_information",
              "recipient_contact_person",
              "return_recipient_adress_add1",
              "return_recipient_adress_add2",
              "return_recipient_delivery_information",
              "return_recipient_contact_person",
              "service_desired_neighbor_details",
              "service_desired_location_details",
              "service_age_screening_test_age_limit",
              "service_shipment_hand",
              "service_any_reference_text",
              "service_delivery_date",
              "service_delivery_time_window",
              "consignment_documents_submission_office",
              "creation_software"
              "service_ind_shipment_specifications",
              "service_ident_check_first_name",
              "service_ident_check_last_name",
              "service_ident_check_late_of_birth",
              "service_ident_Check_minimum_age",
              )


class dhlFileGeneratorVersenden(CarrierFileGenerator):

    @classmethod
    def carrier_for(cls, carrier_name):
        return carrier_name == 'dhl_versenden'

    def _get_filename_single(self, picking, configuration, extension='csv'):
        return super(dhlFileGeneratorVersenden, self)._get_filename_single(
            picking, configuration, extension='txt')

    def _get_filename_grouped(self, configuration, extension='csv'):
        return super(dhlFileGeneratorVersenden, self)._get_filename_grouped(
            configuration, extension='txt')

    def _get_rows(self, picking, configuration):
        """
        Returns the rows to create in the file for a picking

        :param browse_record picking: the picking for which we generate a row in the file
        :param browse_record configuration: configuration of the file to generate
        :return: list of rows
        """
        lines_list = []
        shipped_weight = 0
        recipient_address = picking.partner_id
        sender_address = picking.company_id.partner_id
        for i in range(0,picking.number_of_packages or 1):
            packet_config = picking.carrier_id.weight_distribution
            if packet_config == 'equal_weight':
                weight = ('%.2f' % (picking.weight / (picking.number_of_packages or 1))).replace('.', ',')
            elif packet_config == 'max_weight':
                weight = ('%.2f' % (picking.carrier_id.max_weight)).replace('.', ',')
            else:
                remaining_weight = picking.weight - shipped_weight
                if remaining_weight > picking.carrier_id.max_weight:
                    weight = ('%.2f' % (picking.carrier_id.max_weight)).replace('.', ',')
                    shipped_weight += picking.carrier_id.max_weight
                else :
                    weight = ('%.2f' % (remaining_weight)).replace('.', ',')
                    shipped_weight += remaining_weight
            line = dhlversendenLineVersenden()
            line.reference = picking.name
            if picking.date_done or picking.min_date:
                shipping_date = datetime.strptime(picking.date_done or picking.min_date, '%Y-%m-%d %H:%M:%S').date().strftime('%d.%m.%Y')
                line.send_date = shipping_date
            if recipient_address:
                line.recipient_name1 = recipient_address.name
                line.recipient_name2 = (('packstation' in recipient_address.street_name.lower()) and recipient_address.street2) or  recipient_address.parent_id and recipient_address.parent_id.name or ''
                line.recipient_name3 = (not ('packstation' in recipient_address.street_name.lower()) and recipient_address.street2) or ''
                line.recipient_street = recipient_address.street_name or ''
                line.recipient_housenumber = recipient_address.street_number or ''
                line.recipient_zip = recipient_address.zip or ''
                line.recipient_place = recipient_address.city or ''
                line.recipient_province = recipient_address.state_id and recipient_address.state_id.name or ''
                line.recipient_country = recipient_address.country_id and countries.get(recipient_address.country_id.code).alpha3 or ''
                line.recipient_reference = recipient_address.ref or ''
                line.recipient_email = recipient_address.email or ''
                line.recipient_phone = recipient_address.phone or recipient_address.mobile or ''
            if sender_address:
                line.sender_name1 = line.return_recipient_name1 = sender_address.name
                line.sender_name2 = line.return_recipient_name2 = ''
                line.sender_name3 = line.return_recipient_name3 = sender_address.street2 or ''
                line.sender_street = line.return_recipient_street = sender_address.street_name or ''
                line.sender_housenumber = line.return_recipient_housenumber = sender_address.street_number or ''
                line.sender_zip = line.return_recipient_zip = sender_address.zip or ''
                line.sender_place = line.return_recipient_place = sender_address.city or ''
                line.sender_province = line.return_recipient_province = sender_address.state_id and sender_address.parent_id.state_id.name or ''
                line.sender_country = line.return_recipient_country = sender_address.country_id and countries.get(sender_address.country_id.code).alpha3 or ''
                line.sender_reference = line.return_recipient_reference = sender_address.ref = sender_address.ref
                line.sender_email = line.return_recipient_email = sender_address.email or ''
                line.sender_phone = line.return_recipient_phone = sender_address.phone or sender_address.mobile or ''
            dest_in_eu = False
            european_union = picking.env.ref('base.europe')
            if recipient_address and recipient_address.country_id:
                dest_in_eu = recipient_address.country_id in european_union.country_ids
            line.shipment_declaration = ''
            if picking.carrier_id.carrier_file_id and picking.carrier_id.carrier_file_id.dhl_package_type.code:
                line.produkt =  picking.carrier_id.carrier_file_id and picking.carrier_id.carrier_file_id.dhl_package_type.code or ''
            line.weight = weight
            line.height = ''
            line.width = ''
            line.length = ''
            line.shipment_invoice = picking.sale_id and picking.sale_id.invoice_ids and picking.sale_id.invoice_ids[0].number or ''
            line.shipment_approv_number = ''
            line.shipment_cert_number = ''
            line.shipment_consignment = 'OTHER'
            line.shipment_description = 'miscellaneous'
            line.shipment_charges = str(picking.carrier_price).replace('.', ',') or ''
            line.shipment_netweight = weight
            line.return_billing_number = picking.carrier_id and picking.carrier_id.carrier_file_id and picking.carrier_id.carrier_file_id.billing_number or ''
            line.billing_number = picking.carrier_id.carrier_file_id and picking.carrier_id.carrier_file_id.billing_number or ''
            line.service_shipping_conf_email_template = ''
            line.service_shipping_conf_email = ''
            line.service_cashondelivery_customerref = ''
            if (picking.carrier_id.name == 'DHL Versenden Nachnahme' or picking.carrier_id.name == 'Nachnahme'):
                line.service_cashondelivery_amount = str(picking.sale_id and picking.sale_id.amount_total).replace('.', ',')
            line.service_cashondelivery_iban = ''
            line.service_cashondelivery_bic = ''
            line.service_cashondelivery_payee = ''
            line.service_cashondelivery_bankname = ''
            line.service_cashondelivery_usage1 = ''
            line.service_cashondelivery_usage2 = ''
            line.service_transportversicherung_amount = ''
            line.service_worldpackage_sendertype = ''
            line.service_advance_booking = ''
            line.service_DHLEuropaket_frankaturtyp = ''
            moves = {}
            index = 0
            if not dest_in_eu:
                for move_line in picking.move_lines:
                    if move_line.product_tmpl_id.customs_commodity_code:
                        if not move_line.product_tmpl_id.customs_commodity_code in moves:
                            moves[move_line.product_tmpl_id.customs_commodity_code] = {}
                        if not 'qty' in moves[move_line.product_tmpl_id.customs_commodity_code]:
                            moves[move_line.product_tmpl_id.customs_commodity_code]['qty'] = 0
                        if not 'weight' in moves[move_line.product_tmpl_id.customs_commodity_code]:
                            moves[move_line.product_tmpl_id.customs_commodity_code]['weight'] = 0
                        if not 'price' in moves[move_line.product_tmpl_id.customs_commodity_code]:
                            moves[move_line.product_tmpl_id.customs_commodity_code]['price'] = 0
                        moves[move_line.product_tmpl_id.customs_commodity_code]['qty'] += move_line.product_qty
                        moves[move_line.product_tmpl_id.customs_commodity_code]['weight'] = move_line.product_id.weight
                        moves[move_line.product_tmpl_id.customs_commodity_code]['name'] = move_line.name.replace('\n', ' ').replace(';', '').replace('|', '').replace('"','')
                        moves[move_line.product_tmpl_id.customs_commodity_code]['price'] = move_line.product_id.list_price
                for customs_commodity_code in moves:
                    index += 1
                    setattr(line, "shipment_description_wp" + str(index), moves[customs_commodity_code]['name'] or '')
                    setattr(line, "shipment_quantity_wp" + str(index), str(moves[customs_commodity_code]['qty']).replace('.', ',') or '')
                    setattr(line, "shipment_custom_valuation_wp" + str(index), str(moves[customs_commodity_code]['price']).replace('.', ',') or '')
                    setattr(line, "shipment_country_of_origin_wp" + str(index),
                            sender_address.country_id and countries.get(sender_address.country_id.code).alpha3 or '')
                    setattr(line, "shipment_weight_wp" + str(index), ('%.2f' % moves[customs_commodity_code]['weight']).replace('.', ',') or '')
                    setattr(line, "shipment_customs_commodity_code_wp" + str(index), customs_commodity_code or '')
            line.sender_adress_add1 = ''
            line.sender_adress_add2 = ''
            line.sender_delivery_information = ''
            line.sender_contact_person = picking.sale_id and picking.sale_id.user_id.name or ''
            line.recipient_adress_add1 = ''
            line.recipient_adress_add2 = ''
            line.recipient_delivery_information = picking.note and picking.note.replace('\n', ' ').replace(';', '').replace('|', '').replace('"','') or ''
            line.recipient_contact_person = ''
            line.return_recipient_adress_add1 = ''
            line.return_recipient_adress_add2 = ''
            line.return_recipient_delivery_information = ''
            line.return_recipient_contact_person = picking.sale_id and picking.sale_id.user_id.name or ''
            line.service_desired_neighbor_details = ''
            line.service_desired_location_details = ''
            line.service_age_screening_test_age_limit = ''
            line.service_shipment_hand = ''
            line.service_any_reference_text = ''
            line.service_delivery_date = ''
            line.service_delivery_time_window = ''
            line.consignment_documents_submission_office = ''
            line.creation_software = ''
            line.service_ind_shipment_specifications = ''
            line.service_ident_check_first_name = ''
            line.service_ident_chec_last_name = '',
            line.service_ident_check_late_of_birth = ''
            line.service_ident_Check_minimum_age = ''
            lines_list += [line.get_fields()]
        return lines_list



    def _write_rows(self, file_handle, rows, configuration):
        """
        Write the rows in the file (file_handle)

        :param StringIO file_handle: file to write in
        :param rows: rows to write in the file
        :param browse_record configuration: configuration of the file to generate
        :return: the file_handle as StringIO with the rows written in it
        """
        writer = UnicodeWriter(file_handle, encoding='iso_8859_1',delimiter=';', quotechar='"',
                               lineterminator='\n', quoting=csv.QUOTE_NONE)
        rows.insert(0, (
        'Sendungsreferenz', 'Sendungsdatum', 'Absender Name 1', 'Absender Name 2', 'Absender Name 3', ('Absender Straße').decode('utf-8'),
        'Absender Hausnummer', 'Absender PLZ', 'Absender Ort', 'Absender Provinz', 'Absender Land', 'Absenderreferenz',
        'Absender E-Mail-Adresse', 'Absender Telefonnummer', ('Empfänger Name 1').decode('utf-8'), ('Empfänger Name 2 / Postnummer').decode('utf-8'),
        ('Empfänger Name 3').decode('utf-8'), ('Empfänger Straße').decode('utf-8'), ('Empfänger Hausnummer').decode('utf-8'), ('Empfänger PLZ').decode('utf-8'), ('Empfänger Ort').decode('utf-8'),
        ('Empfänger Provinz').decode('utf-8'), ('Empfänger Land').decode('utf-8'), ('Empfängerreferenz').decode('utf-8'), ('Empfänger E-Mail-Adresse').decode('utf-8'),
        ('Empfänger Telefonnummer').decode('utf-8'), 'Gewicht', ('Länge').decode('utf-8'), 'Breite', ('Höhe').decode('utf-8'), 'Produkt- und Servicedetails',
        ('Retourenempfänger Name 1').decode('utf-8'), ('Retourenempfänger Name 2').decode('utf-8'), ('Retourenempfänger Name 3').decode('utf-8'), ('Retourenempfänger Straße').decode('utf-8'),
        ('Retourenempfänger Hausnummer').decode('utf-8'), ('Retourenempfänger PLZ').decode('utf-8'), ('Retourenempfänger Ort').decode('utf-8'), ('Retourenempfänger Provinz').decode('utf-8'),
        ('Retourenempfänger Land').decode('utf-8'), ('Retourenrempfänger E-Mail-Adresse').decode('utf-8'), ('Retourenempfänger Telefonnummer').decode('utf-8'),
        'Retouren-Abrechnungsnummer', 'Abrechnungsnummer', ('Service - Versandbestätigung - E-Mail Text-Vorlage').decode('utf-8'),
        ('Service - Versandbestätigung - E-Mail-Adresse').decode('utf-8'), 'Service - Nachnahme - Kontoreferenz',
        'Service - Nachnahme - Betrag', 'Service - Nachnahme - IBAN', 'Service - Nachnahme - BIC',
        ('Service - Nachnahme - Zahlungsempfänger').decode('utf-8'), 'Service - Nachnahme - Bankname',
        'Service - Nachnahme - Verwendungszweck 1', 'Service - Nachnahme - Verwendungszweck 2',
        'Service - Transportversicherung - Betrag', ('Service - Weltpaket - Vorausverfügungstyp').decode('utf-8'),
        ('Service - Vorausverfügung').decode('utf-8'), 'Service - DHL Europaket - Frankaturtyp', 'Sendungsdokumente - Ausfuhranmeldung',
        'Sendungsdokumente - Rechnungsnummer', 'Sendungsdokumente - Genehmigungsnummer',
        'Sendungsdokumente - Bescheinigungsnummer', 'Sendungsdokumente - Sendungsart',
        'Sendungsdokumente - Beschreibung', 'Sendungsdokumente - Entgelte', 'Sendungsdokumente - Gesamtnettogewicht',
        'Sendungsdokumente - Beschreibung (WP1)', 'Sendungsdokumente - Menge (WP1)',
        'Sendungsdokumente - Zollwert (WP1)', 'Sendungsdokumente - Ursprungsland (WP1)',
        'Sendungsdokumente - Zolltarifnummer (WP1)', 'Sendungsdokumente - Gewicht (WP1)',
        'Sendungsdokumente - Beschreibung (WP2)', 'Sendungsdokumente - Menge (WP2)',
        'Sendungsdokumente - Zollwert (WP2)', 'Sendungsdokumente - Ursprungsland (WP2)',
        'Sendungsdokumente - Zolltarifnummer (WP2)', 'Sendungsdokumente - Gewicht (WP2)',
        'Sendungsdokumente - Beschreibung (WP3)', 'Sendungsdokumente - Menge (WP3)',
        'Sendungsdokumente - Zollwert (WP3)', 'Sendungsdokumente - Ursprungsland (WP3)',
        'Sendungsdokumente - Zolltarifnummer (WP3)', 'Sendungsdokumente - Gewicht (WP3)',
        'Sendungsdokumente - Beschreibung (WP4)', 'Sendungsdokumente - Menge (WP4)',
        'Sendungsdokumente - Zollwert (WP4)', 'Sendungsdokumente - Ursprungsland (WP4)',
        'Sendungsdokumente - Zolltarifnummer (WP4)', 'Sendungsdokumente - Gewicht (WP4)',
        'Sendungsdokumente - Beschreibung (WP5)', 'Sendungsdokumente - Menge (WP5)',
        'Sendungsdokumente - Zollwert (WP5)', 'Sendungsdokumente - Ursprungsland (WP5)',
        'Sendungsdokumente - Zolltarifnummer (WP5)', 'Sendungsdokumente - Gewicht (WP5)',
        'Sendungsdokumente - Beschreibung (WP6)', 'Sendungsdokumente - Menge (WP6)',
        'Sendungsdokumente - Zollwert (WP6)', 'Sendungsdokumente - Ursprungsland (WP6)',
        'Sendungsdokumente - Zolltarifnummer (WP6)', 'Sendungsdokumente - Gewicht (WP6)', 'Sendungsreferenz (Retoure)',
        'Absender Adresszusatz 1', 'Absender Adresszusatz 2', 'Absender Zustellinformation', 'Absender Ansprechpartner',
        ('Empfänger Adresszusatz 1').decode('utf-8'), ('Empfänger Adresszusatz 2').decode('utf-8'), ('Empfänger Zustellinformation').decode('utf-8'),
        ('Empfänger Ansprechpartner').decode('utf-8'), ('Retourenempfänger Adresszusatz 1').decode('utf-8'), ('Retourenempfänger Adresszusatz 2').decode('utf-8'),
        ('Retourenempfänger Zustellinformation').decode('utf-8'), ('Retourenempfänger Ansprechpartner').decode('utf-8'),
        'Service - Wunschnachbar - Details', 'Service - Wunschort - Details',
        ('Service - Alterssichtprüfung - Altersgrenze').decode('utf-8'), 'Service - Sendungshandling', 'Service - beliebiger Hinweistext',
        'Service - Zustelldatum', 'Service - Zustellzeitfenster', 'Sendungsdokumente - Einlieferungsstelle',
        'Creation-Software', 'Service - ind. Versendervorgabe Kennzeichen', 'Service - Ident-Check - Vorname',
        'Service - Ident-Check - Nachname', 'Service - Ident-Check - Geburtsdatum',
        'Service - Ident-Check - Mindestalter'))
        writer.writerows(rows)
        return file_handle
