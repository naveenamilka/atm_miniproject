customername = input("Enter customer name: ")

lists = '''
Rice       Rs1000/bag
Teapowder  Rs50/packet
oil        Rs100/packet
Flour      Rs100/kg
Bottles    Rs60/2
soap       Rs30
'''

price = 0
totalprice = 0
Finalprice = 0

itemlist = []
quantitylist = []
pricelist = []

items = {
    "rice": 1000,
    "teapowder": 50,
    "oil": 100,
    "flour": 100,
    "bottles": 60,
    "soap": 30
}

while True:

    option = input("Enter 1 for shopping or 2 to exit: ")

    if option == "2":
        print("Thank you for Shopping")
        break

    elif option == "1":

        print(lists)

        while True:

            process = input("To Buy Enter 1 or Enter 2 for exit: ")

            if process == "2":
                print("Thank you for shopping")
                break

            elif process == "1":

                item = input("Choose your items: ").lower()

                if item in items:

                    while True:

                        quantity_ip = input("Enter Quantity: ")

                        if quantity_ip.isdigit():
                            quantity = int(quantity_ip)
                            break

                        else:
                            print("Please enter a valid quantity")

                    price = quantity * items[item]

                    totalprice += price

                    itemlist.append(item)
                    quantitylist.append(quantity)
                    pricelist.append(price)

                else:
                    print("Selected item is not available")

        # BILL SECTION
        if totalprice > 0:

            tax = (totalprice * 18) / 100
            Finalprice = tax + totalprice

            print(25 * "=", "NR Supermarket", 25 * "=")
            print(30 * " ", "Jagityal")

            print("Name:", customername)
            print(75 * "-")

            print("S.No\tItems\t\tQty\tPrice")

            for i in range(len(pricelist)):

                print(
                    i + 1, "\t",
                    itemlist[i], "\t\t",
                    quantitylist[i], "\t",
                    pricelist[i]
                )

            print(75 * "-")

            print("Total Amount:\t\tRs", totalprice)
            print("Tax Amount:\t\tRs", tax)
            print("Final Amount:\t\tRs", Finalprice)

            print(75 * "-")
            print("      Thank You & Visit Again")
            print(75 * "-")