#dmart

from unicodedata import name


def calculate_final_price(name, bucket, GST):
    totalPrice = 0
    for item in bucket:
        productPrice = (item["qty"] * item["cost"])
        totalPrice += (productPrice - productPrice * item["discout"] / 100)

    finalPriceWithGST = (totalPrice * GST / 100) + totalPrice
    return name, totalPrice, finalPriceWithGST



finalPrice1 = calculate_final_price(
    name="Vishal",
    bucket=[{"itemName": "milk", "qty": 2, "cost": 40, "discout": 12}, {"discout": 12, "itemName": "icecream", "qty": 2, "cost": 50}],
    GST=18
)

finalPrice2 = calculate_final_price(
    name="Vishal1",
    bucket=[{"itemName": "xyz", "qty": 3, "cost": 70, "discout": 12}, {"discout": 12, "itemName": "icecream", "qty": 2, "cost": 50}],
    GST=18
)

print(finalPrice1)
print(finalPrice2)
# bucket=[{"itemName": "milk", "qty": 2, "cost": 40, "discout":12}, {"discout":12,"itemName": "icecream", "qty": 2, "cost": 50}]
# GST= 18
# totalPrice=0
# for item in bucket:
#     prductPrice =  (item["qty"]* item["cost"])
#     totalPrice= totalPrice+ (prductPrice - prductPrice*item["discout"]/100)

# finalPriceWithGST = (totalPrice*18/100) + totalPrice
# print(totalPrice)
# print(finalPriceWithGST)