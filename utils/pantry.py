from datetime import datetime
import json

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FILE = os.path.join(BASE_DIR, "data", "grocery_data.json")
print("USING FILE:", DATA_FILE)
grocery_list = []

def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(grocery_list, file, indent=4)


def load_data():
    global grocery_list

    try:
        with open(DATA_FILE, "r") as file:
            grocery_list = json.load(file)

    except:
        grocery_list = []

def add_item(item, category, unit, price, qty, fresh_for):
    for a in grocery_list:
        if item.lower()==a["item"]:
            a["qty"]+=qty
            print(f"{item} is already there in the Pantry. Updated the quantity")
            save_data()
            return
    print(f"{item} added successfully!")
    grocery_list.append({"item":item.lower(),"category": category,"price":price,'qty':qty,"unit": unit,"fresh_for":fresh_for,"date_added":datetime.now().strftime("%d-%m-%Y")})
    save_data()

def delete_item(item):
    for a in grocery_list:
        if a["item"]==item.lower():
            grocery_list.remove(a)
            save_data()
            break 
    else:
        print("Item not found")
    
def update_item(item,new_price=None,new_qty=None,new_fresh_for=None):
    for a in grocery_list:
        if a["item"]==item.lower():
            if new_price !="":
                a["price"]=float(new_price)
            if new_qty !="":
                a["qty"]=int(new_qty)
            if  new_fresh_for !="" :
                a["fresh_for"]=int(new_fresh_for)
            print("Updates The item Succesfully")
            save_data()
            break
    else:
        print("item Not in the pantry")
    
def show_items():
    if grocery_list:
        print("Printing Grocery List")
        for a in grocery_list:
            print("Item Name :",a["item"])
            print("Price : $",a["price"])
            print("Quantity :", a["qty"], a["unit"])
            print("Fresh For :",a["fresh_for"]," Days")
            print("Date Added :", a["date_added"])
            date_added=datetime.strptime(a['date_added'],"%d-%m-%Y")
            days_passed=(datetime.now()-date_added).days
            days_left=a["fresh_for"]-days_passed
            print("Days Left :", days_left)
            print("Category :", a["category"])
            print("Unit :", a["unit"])
            if days_left <= 0:
                print("Status : EXPIRED")
            elif days_left <= 2:
                print("Status : Expiring Soon")
            else:
                print("Status : Fresh")
    else:
        print("Pantry is empty")

def total_value():
    total=0
    for a in grocery_list:
        total+=a["price"] * a['qty']
    print("Total Pantry Value : $",total)

def search_item(item):
    for a in grocery_list:
        if a['item']==item.lower():
            print("Item found")
            print("Item Name :",a["item"])
            print("Price : $",a["price"])
            print("Quantity :",a["qty"])
            print("Fresh For :",a["fresh_for"]," Days")
            print("Date Added :", a["date_added"])
            date_added=datetime.strptime(a['date_added'],"%d-%m-%Y")
            days_passed=(datetime.now()-date_added).days
            days_left=a["fresh_for"]-days_passed
            print("Days Left :", days_left)
            print("Category :", a["category"])
            print("Quantity :", a["qty"], a["unit"])
            if days_left <= 0:
                print("Status : EXPIRED")
            elif days_left <= 2:
                print("Status : Expiring Soon")
            else:
                print("Status : Fresh")
            return
    print("Item Not in the Pantry")
def main():
    while True:
        print("\n\nGrocery APP")
        print("1.Add Item ")
        print("2.Delete Item")
        print("3.Update Item")
        print("4.Display Item")
        print("5.Display Total Pantry Value")
        print("6.Search For an Item")
        print("7.Exit")
        ch=int(input("Enter your choice :  "))
        if ch==1:
            item=input("Name of the item :")
            try:
                price=float(input("Price: "))
            except:
                print("Invalid input")
                continue
            try:
                qty=int(input("Quantity: "))
            except:
                print("Invalid input")
                continue
            try:
                fresh_for=int(input("How long does the item stays Fresh for (in Days) "))
            except:
                print("Invalid input")
                continue
            category = input("Category : ")
            unit = input("Unit (kg/liters/pcs/etc): ")
            add_item(item, category, unit, price, qty, fresh_for)
        elif ch==2:
            item=input("Name of the Item u wish to delete :")
            delete_item(item)
        elif ch==3:
            item=input("Which item do you wish to update :")
            price=input("Enter the Price (Press enter to skip)")
            qty = input("New quantity (Press Enter to skip): ")
            fresh_for = input("New fresh for (Press Enter to skip): ")
            update_item(item,price,qty,fresh_for)
        elif ch==4:
            show_items()
        elif ch==5:
            total_value()
        elif ch==6:
            item=input("Enter the Item U wish to search for :")
            search_item(item)
        elif ch==7:
            print("Exiting the App ....")
            break
        else:
            print("Invalid Input Try Again")


