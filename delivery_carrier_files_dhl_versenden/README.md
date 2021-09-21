# README #

### How to set up? ###

To be used with https://bitbucket.org/huckemedia/base_delivery_carrier_files.dd

pip install iso3166

### What is this repository for? ###

* Create DHL Versenden text files to be imported with DHL Versenden Polling Client

### Notes ###


#### Handling of DHL "PACKSTATION" ####

In Germany we use "Packstation" as special addresses for delivery. This is handled in defined manner with DHL Versenden:

Delivery address should be in Odoo:

* res.partner.street = "PACKSTATION" (case does NOT matter) 
* res.partner.street_number = f.e. "123" (Number of Packstation) 
* res.partner.street2 = f.e. "12345678" (Postnummer = customer number for Packstation user)

BDD for Packstation:

SCENARIO Customer wants Packstation as delivery address 

GIVEN res.partner.street."uppercase" is "PACKSTATION" 

THEN make output file field "Empfänger Name 2 / Postnummer" = partner.street2 (this fiel should contain "Postnummer" (ex. 40244212))