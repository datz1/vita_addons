odoo.define('hucke_print_delivery_slip_and_invoice.FormController', function (require) {
"use strict";

    var FormController = require('web.FormController');
    var dialogs = require('web.view_dialogs');
    var core = require('web.core');
    var web_client = require('web.web_client');
    var rpc = require('web.rpc');


    var FormController = FormController.include({

        _onButtonClicked: function (event) {

            if (event.data.attrs.name == 'button_invoice_and_print') {

                var data = this.initialState.data

                if (data.picking_type_code == "outgoing"){

                    rpc.query({
                        model: 'stock.picking',
                        method: 'do_print_invoice',
                        args: [data.id],
                    }).then(function(response) {

                        if (response) {

                            web_client.do_action(response);

                        } else {

                            console.log('Something went wrong while printing the invoice.')

                        }

                    });

                    rpc.query({
                        model: 'stock.picking',
                        method: 'do_print_delivery',
                        args: [data.id],
                    }).then(function(response) {

                        if (response) {

                            web_client.do_action(response);

                        } else {

                            console.log('Something went wrong while printing the delivery slip.')

                        }

                    });

                }

            }

            this._super(event);

        }

    });

});
