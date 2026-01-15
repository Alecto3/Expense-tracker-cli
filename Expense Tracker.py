from datetime import date
import json
def main():
    global Expenses
    Expenses=[]
    load_expenses()
    func="""
    1- Add an expense
    2- Update an expense
    3- Delete an expense
    4- View all expenses
    5- View a summary of all expenses
    6- View a summary of expenses for a specific month
    7- Quit 
    """
    while True:
        print(func)
        choice=input("Enter the number of the function: ")
        if choice.isdigit():
            if choice=="1":
                add_expense()
            elif choice=="2":
                update_expense()
            elif choice=="3":
                delete_expense()
            elif choice=="4":
                view_expenses()
            elif choice=="5":
                view_summary_all()
            elif choice=="6":
                view_summary_month()
            elif choice=="7":
                saving_expenses()
                break
        else:
            print("Invald entry .. please try again ")

#دوال الحفظ و التحميل #

# اولاً: الحفظ
def saving_expenses():
    with open("expens.json" , "w") as js:
        json.dump(Expenses, js)

#ثانيًا: التحميل
def load_expenses():
    global Expenses
    try:
        with open("expens.json" , "r") as js:
                Expenses=json.load(js)
    except FileNotFoundError:
        Expenses=[]

#الدوال الاساسية#

#إضافة مصروف 
def add_expense():
    expens = {"ID": len(Expenses) + 1,"description":input("Enter the description: "),"amount":int(input("Enter the  an the amount: ")),"date":str(date.today()),"month":date.today().month}
    Expenses.append(expens)
    print("Expense added successfully")

#عرض جميع المصروفات 
def view_expenses():
    if Expenses:
        for ex in Expenses:
            print(f'{ex["ID"]} | {ex["date"]} | {ex["description"]} | ${ex["amount"]} ')
    else:
        print("There is no expenses to view..")
        return 
    
#تعديل مصروف 
def update_expense():
    if not Expenses:
        print("There is no expenses to Update..")
        return
    else:
        view_expenses()
    choice=input("Enter the ID of the expense you want to update: ")
    if choice.isdigit():
        for i in Expenses:
            if int(choice) == i["ID"]:
                print(f'Current expense: {i["ID"]} | {i["date"]} | {i["description"]} |  ${i["amount"]}')
                description=input("Enter new description (or leave blank to keep): ")
                amount=input("Enter new amount (or leave blank to keep): ")
            else:
                print("please choose from the IDs shown")
                return
            if description:
                i.update({"description":description})
            if amount:
                i.update({"amount":amount})
            print("Expense updated successfuly")
    else:
        print("Invald entry .. please try again ")
        return

#مسح مصروف 
def delete_expense():
    if not Expenses:
        print("There is no expenses to delete..")
        return
    else:
        view_expenses()
    choice=input("Enter the ID of the expense you want to delete: ")
    if choice.isdigit():
        for i in Expenses:
            if int(choice) == i["ID"]:
                if input("are you sure you want to delete the selected expense?(Y/N)").upper()=="Y":
                    Expenses.remove(i)
                    print("Expense deleted successfuly")
                else:
                    return
                
#عرض مجموع المصروفات(كامل)
def view_summary_all():    
    if Expenses:
        print(f"Total amount: ${sum(x["amount"]for x in Expenses)}")    
    else:
        print("There is not expenses to calculat..")
        return
    
#عرض مجموع مصروفات (شهر)    
def view_summary_month():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if Expenses:
        
        choice=int(input("Enter the month: "))
        print(f'Total amount for {months[choice-1]}: ${sum(x["amount"]for x in Expenses if x["month"]==choice)}')
    else:
        print("There is not expenses to calculat..")
        return
main()
