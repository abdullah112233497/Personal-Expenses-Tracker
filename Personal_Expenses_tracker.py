# import json

# def load():
#     try:
#         with open("Expenses.json","r") as f:
#             data= json.load(f)
#             if data is None:
#                 return []
#             else:
#                 return data

            

#     except (FileNotFoundError, json.JSONDecodeError):
#          expenses=[]
# expenses=load()
# def save():
#     with open("Expenses.json","w") as p:
#         json.dump(expenses,p)
# def entery():
#     expense={}
#     expense["catagory"]=input("Enter your catagory: ")
#     expense["Rupees"]=int(input("Enter your rupees: "))
#     expenses.append(expense)
    
#     save()
    
# def show():
#     total=sum(e["Rupees"] for e in expenses)
#     print(f"Total: {total}")
#     for e in expenses:
#         catagories={}
#         catagories[e["catagory"]]=catagories.get(e["catagory"],0)+ e["Rupees"]
#         print(catagories)
    


# while True:
#     choice=int(input(f"Enter the 1-Entery \n 2-Save \n 3-Show:"))
#     if choice==1:
#         entery()
#     elif choice==2:
#         save()
#     elif choice==3:
#         show()
#     else:
#         print("Choice is not avaliable.")


import json
def load():
    try:
        with open("Expenses.json","r") as f:
            data=json.load(f)
            if data is None:
                return []
            else:
                return data
    except (FileNotFoundError,json.JSONDecodeError) :
        return []
expenses=load()
def save():
    with open("Expenses.json","w") as f:
        json.dump(expenses,f)
def add():
    expense={}
    expense["Catagory"]=input("Enter the catagory: ")
    expense["Amount"]=int(input("Enter the Amount: "))
    expenses.append(expense)
    save()
def show():
    catagories={}
    total=sum(e["Amount"] for e in expenses)
    for i in expenses:
        catagories[i["Catagory"]]=catagories.get(i["Catagory"],0)+i["Amount"]
    print(catagories)
    print(f"Total Amount is :{total}")
    print("-------------------------------------------")

c=True
while c:
    choice=int(input(f"""
    Enter Your choice:
    (1- See
     2- Add
     3- Exit)
    """))
    if choice==1:
        show()
    elif choice==2:
        add()
    elif choice==3:
        c=False
    else:
        print ("Choice is not avaliable.")
        