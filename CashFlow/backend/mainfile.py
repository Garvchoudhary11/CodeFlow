import sqlite3

conn=sqlite3.connect('cashflow.db')
c=conn.cursor()

food=fuel=outing=saving=misc=mandatory=0
salary=spending=saving=0

def update():
    food=c.execute("SELECT food FROM main WHERE user = 'Garv'").fetchone()[0]
    fuel=c.execute("SELECT fuel FROM main WHERE user = 'Garv'").fetchone()[0]
    outing=c.execute("SELECT outing FROM main WHERE user = 'Garv'").fetchone()[0]
    saving=c.execute("SELECT savings FROM main WHERE user = 'Garv'").fetchone()[0]
    misc=c.execute("SELECT misc FROM main WHERE user = 'Garv'").fetchone()[0]
    mandatory=c.execute("SELECT mandatory FROM main WHERE user = 'Garv'").fetchone()[0]
    spending=c.execute("SELECT spending FROM main WHERE user = 'Garv'").fetchone()[0]


def expense():
    print("""1.Food \n
             2.Fuel
             3.Outing
             4.Saving
             5.Misc
             6.Mandatory""")
    category=int(input("Enter Category no. : "))
    amount=int(input("Enter amount : "))
    if(category==1):
        food=+amount
        c.execute("UPDATE main SET food=? WHERE user='garv'",(food,))
    elif(category==2):
        fuel=+amount
    elif(category==3):
        outing=+amount
    elif(category==4):
        saving=+amount
    elif(category==5):
        misc=+amount
    elif(category==6):
        mandatory=+amount
    else:
        print("Enter a Valid Option")
        
def reset():
    print("Reset \n 1.All \n 2.Categories")
    choice=int(input())
    if(choice==1):
        salary=spending=saving=food=fuel=fastfood=misc=flatfee=0
    else:
         food=fuel=fastfood=misc=flatfee=0

def show():
    print("Amount Left :",spending)
    print("Saving :",saving)
    print("Food :",food)
    print("Fuel :",fuel)
    print("Outing :",outing)
    print("Misc :",misc)
    print("Mandatory :",mandatory)
    
def addfunds():
    salary=int(input("Enter your salary :"))
    saving=int(input("Enter saving amount :"))
    spending=salary-saving
    


choice=0 
while(choice!=5):  
    update()  
    print("                     CashFlow                     ")
    print("Amount Left :",spending)
    print("Menu")
    print("""1.Add Expense
2.Add Funds
3.Show
4.Reset
5.Exit""")
    choice=int(input("Enter a input"))
    if(choice==1):
        expense()
    elif(choice==2):
        addfunds()
    elif(choice==3):
        show()
    elif(choice==4):
        reset()
    else:
        choice=5
conn.commit()
conn.close()

        







