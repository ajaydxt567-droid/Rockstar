value=True
report={"Water": 1000,
        "Milk":500,
        "Coffee":760,
        "Money":10
}
while value:
    x=0
    coffee_type=input("What would you like: (espresso/latte/cappuccino): ").lower()
    rupees=int(input("Input your coin here: "))
    if coffee_type=="espresso":

        if report["Water"]<200:
            print("Sorry we have in sufficient amount of Water")
            value=False
        if report["Milk"]<50:
            print("Sorry we have in sufficient amount of Milk")
            value=False
        if report["Coffee"]<20:
            print("Sorry we have in sufficient amount of Coffee")
            value=False
        if rupees<10:
            print("Sorry we have in sufficient amount of Money")
            value=False
        else:
            report["Water"]-=200
            report["Milk"]-=50
            report["Coffee"]-=20
            report["Money"]+=10
            print([report])
    if coffee_type=="latte":
        if report["Water"] < 150:
            print("Sorry we have in sufficient amount of Water")
            value = False
        if report["Milk"] < 70:
            print("Sorry we have in sufficient amount of Milk")
            value = False
        if report["Coffee"] < 25:
            print("Sorry we have in sufficient amount of Coffee")
            value = False
        if rupees<16:
            print("Sorry we have in sufficient amount of Money")
            value = False
        else:
            report["Water"]-=150
            report["Milk"]-=70
            report["Coffee"]-=25
            report["Money"]+=16
            print([report])
    if coffee_type=="cappuccino":
        if report["Water"] < 100:
            print("Sorry we have in sufficient amount of Water")
            value = False
        if report["Milk"] < 100:
            print("Sorry we have in sufficient amount of Milk")
            value = False
        if report["Coffee"] < 30:
            print("Sorry we have in sufficient amount of Coffee")
            value = False
        if rupees < 20:
            print("Sorry we have in sufficient amount of Rupee")
            value = False
        else:
            report["Water"]-=100
            report["Milk"]-=100
            report["Coffee"]-=30
            report["Money"]+=20
            print([report])

    else:
        print("please choose the right flavour")
