## Print Delivery Slip and Invoice from Delivery Order

A new Button was added "Invoice & Print". It's only visible for outgoing delivery orders which have a sale id and are in done state. The button calls two python functions via javascript. Both of them return a report action, which prints the Invoice and Delivery Slip. The Invoice is created and validated before printing.

### Add barcode to the pdf

If you want to add the barcode to the barcode pdf which can be downloaded in the settings, you need to find the `make_barcodes.sh` in the `stock_barcode` module. Add your barcode here and run the script. Now your barcode will be shown in the pdf.

### Dependencies:
 - stock
 - sale_stock
