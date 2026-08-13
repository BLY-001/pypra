def get_vat(price, vat_percent):
    VAT = (price * vat_percent)/100
    return VAT

s = get_vat(200, 5)
print(s)
