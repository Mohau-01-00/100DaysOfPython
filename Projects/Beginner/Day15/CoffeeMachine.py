from  Machine_Data import resources
from  Machine_Data import MENU



def calc_money(nickle,dime,quarter,pennie,cup_price):
    if cup_price=="latte":
       cup_price=MENU['latte']['cost']
    elif cup_price=='espresso':
       cup_price=MENU['espresso']['cost']
    elif cup_price=='cappucino':
       MENU['espresso']['cost']


       
    total=float((quarter*0.25)+(nickle*0.05)+(dime*0.1)+(pennie*0.01))
    total=round(total,2)
    if total>cup_price:
       change=total-cup_price
       change=round(change,2)
       print(f"Your change is $ {change}")
    elif total<cup_price:
       print(f"Your money was not enough")

    print(f"The total you gave is $ {total} ")




def res(choice):
 
    water=resources["water"]
    milk=resources["milk"]
    coffee=resources["coffee"]
  


    if choice=="latte":
        water=water-MENU['latte']['ingredients']['water']
        coffee=coffee-MENU['latte']['ingredients']['coffee']
        milk=milk-MENU['latte']['ingredients']['milk']
    elif choice=="cappuccino":
        water=water-MENU['cappuccino']['ingredients']['water']
        coffee=coffee-MENU['cappuccino']['ingredients']['coffee']
        milk=milk-MENU['cappuccino']['ingredients']['milk']
    elif choice=="espresso":
        water=water-MENU['espresso']['ingredients']['water']
        coffee=coffee-MENU['espresso']['ingredients']['coffee']
       
  
    resources.update({"milk":milk,"water":water,"coffee":coffee})
    
    if choice=="report":
       for content in resources:
        print(f"{content}: {resources[content]}")
             #print(resources)
    for ingred in resources:
        if resources[ingred]<0:
         print(f"Not enough {ingred}")
         main()

#main programme

should_continue=True
def main():

    ask_again=True
    

    while ask_again:
        drink=input("What would you like?(espresso/latte/cappuccino): ").lower()
        if drink!='latte' and drink!='espresso' and drink!= 'cappuccino':
           print("Wrong Input")
           ask_again=True
           res(choice=drink)  
        elif drink!="report":
            ask_again=False
    
    
    print("Please insert coins")
    
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes?: "))
    nickles=int(input("How many nickles?: "))
    pennies=int(input("How many pennies?: "))
    calc_money(nickle=nickles,dime=dimes,quarter=quarters,pennie=pennies,cup_price=drink)

while should_continue:
    main()

    


