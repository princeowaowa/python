productname = input("Enter the product name: ")
bucket=[
    {"itemname":"milk" ,"price":20},
    {"itemname":"redbull","price":120},
    {"itemname":"monster","price":125}
]

for item in bucket:
    if item["itemname"] == productname:
        print(f"the price of {productname} is {item['price']}")
        found = True
        break
else:
        print(f"{productname} is not available :( ")