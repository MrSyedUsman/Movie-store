from datetime import date, timedelta

class MovieStore:
    global list_dict
    list_dict = {
            "movie1": {"name":"Lord of the rings","release":"2001","runtime":"251 minutes","stock":"3","loan":"0"},
            "movie2": {"name":"The Matrix","release":"1999","runtime":"136 minutes","stock":"3","loan":"0"},
            "movie3": {"name":"Fear and Loathing in Las Vegas","release":"1998","runtime":"118 minutes","stock":"3","loan":"0"},
            "movie4": {"name":"Gladiator","release":"2000","runtime":"155 minutes","stock":"3","loan":"0"},
            "movie5": {"name":"Pirates of the Caribbean","release":"2003","runtime":"153 minutes","stock":"3","loan":"0"}
        }
    
    def __init__(self, name):
        self.name = name
        
    def list_all_movies(self):      
        for key in list_dict:
            print("Name: {}\nRelease Date: {}\nDuration: {}\nStock Available: {}\non Loan: {}\n\n".format(list_dict[key]["name"], list_dict[key]["release"], list_dict[key]["runtime"], list_dict[key]["stock"], list_dict[key]["loan"]))
            
            
    def borrow_movies(self,name,amount,customer_name):
        if (int(self.amount)>2):
            print("\nSORRY! You can borrow Max 2 movies!\n")
        elif (int(self.amount)<=2):
            for key in list_dict:
                if (list_dict[key]["name"] == self.name):
                    list_dict[key]["stock"] = 3-int(self.amount)
                    list_dict[key]["loan"] = 0+int(self.amount)
                    print("\n!--- {}, You borrowed {} movie(s) ---!".format(self.customer_name,self.amount))
                    dt = date.today() + timedelta(3)
                    print("!--- Return due date: {} ---!\n".format(dt))
                    

class Customers(MovieStore):
    def __init__(self, name, customer_name, amount):
        MovieStore.__init__(self,name)
        self.customer_name = customer_name
        self.amount = amount
        
class Videos(MovieStore):
    def __init__(self, name):
        self.name=name
        
    def check_availablity(self,name):
        for key in list_dict:
            if (list_dict[key]["name"] == self.name):
                if(int(list_dict[key]["stock"]) >2):
                    print("\n{} ---> Available Units = {}".format(list_dict[key]["name"],list_dict[key]["stock"]))
                    print("{} ---> On Loan = {}\n".format(list_dict[key]["name"],list_dict[key]["loan"]))
                elif(int(list_dict[key]["stock"]) >0 and int(list_dict[key]["stock"])<3):
                    print("\n{} ---> Available Units = {}".format(list_dict[key]["name"],list_dict[key]["stock"]))
                    print("{} ---> On Loan = {}".format(list_dict[key]["name"],list_dict[key]["loan"]))
                    dt = date.today() + timedelta(3)
                    print("Returning due date: {}\n".format(dt))
                elif(int(list_dict[key]["stock"]) == 0):
                    print("\n{} ---> Available Units = {}".format(list_dict[key]["name"],list_dict[key]["stock"]))
                    print("{} ---> On Loan = {}".format(list_dict[key]["name"],list_dict[key]["loan"]))
                    dt = date.today() + timedelta(3)
                    print("Returning due date: {}\n".format(dt))

class Video_Test(Customers):
    def __init__(self):
        pass
    
    choice=""
    while(choice!="Q"):    
        print("|-|-|-| ---- Welcome To Movie Store ---- |-|-|-|")
        print("\nChoice Menu: L-List, B-Borrow, A-Availability, Q-Quit\n")
        choice = input()

        if(choice=="L"):
            v=MovieStore("placeholder")
            v.list_all_movies()

        elif(choice=="B"):
            cust_name = input("\nEnter Customer Name: ")
            title_name = input("Enter the title of the video you want to borrow: ")
            amount_limit = input("Enter the amount of movies to borrow, max 2! ")
            c=Customers(title_name,cust_name,amount_limit)
            c.borrow_movies(title_name,amount_limit,cust_name)
            
        elif(choice=="A"):
            title_name = input("\nEnter the movie title, you want to check?: ")
            c=Videos(title_name)
            c.check_availablity(title_name)
        elif(choice=="Q"):
            print("QUITTED!")
