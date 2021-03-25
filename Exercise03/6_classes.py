'''
6. Create classes from the following class diagrams:
'''
import pycountry
import random

class Circle:
    def __init__(self,radius:float):
        self.radius=radius
    def get_Area(self):
        Area=(self.radius**2)*3.14159
        return Area
    def get_Circumeference(self):
        Circumference=self.radius*2
        return Circumference

class Rectangle:
    def __init__(self,length:float,height:float):
        self.length=length
        self.height=height
    def get_arearect(self):
        Arearect=self.length*self.height
        return Arearect
    def get_perimeterrect(self):
        perimeterrect=2*(self.length+self.height)
        return perimeterrect

class Address:
    def __init__(self,street:str,city:str,state:str,postalcode:int,country:str):
        self.street=street
        self.city=city
        self.state=state
        self.postalcode=postalcode
        self.country=country
    def __validate(self):
        if self.country in pycountry.countries:
            return "validated"
        else:
            return "wrong planet"
    def print_full_address(self):
        print(f"{self.street}, {self.city}, {self.state}, {self.postalcode}, {self.country}.")

class Student:
    def __init__(self,first_name:str,last_name:str,gender:str,email:str):
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.email=email
    def getName(self):
        name=self.first_name+self.last_name
        return name
    def getEmail(self):
        return self.email
    def getGender(self):
        return self.gender

class Invoice:
    def __init__(self,order_id:int,product_name:str,product_quantity:float,product_price_per_quantity:float):
        self.order_id=order_id
        self.product_name=product_name
        self.product_quantity=product_quantity
        self.product_price_per_quantity=product_price_per_quantity
    def __generate_id(self):
        return self.order_id
    def make_Total(self):
        total=self.product_quantity*self.product_price_per_quantity
        return total
    def printbill(self):
        print(f"Order ID: {self.order_id}, Product Name: {self.product_name}, Product Quantity: {self.product_quantity}, Product price per quantity: {self.product_price_per_quantity} Total: {self.product_quantity*self.product_price_per_quantity}")
    
class Account:
    def __init__(self,account_number:int,name:str,balance:float):
        self.account_number=account_number
        self.name=name
        self.balance=balance
    def generate_unique_account_number(self):
        self.account_number=random.randint(0,10000)
        return self.account_number
    def get_account_number(self, name:str):
        if self.account_number:
            return self.account_number
        else:
            self.generate_unique_account_number()
    def getName(self,account_number:int):
        return self.name
    def getBalance(self):
        return self.balance
    def credit(self,amount:float):
        self.balance+=amount
    def debit(self,amount:float):
        self.balance-=amount

class Book:
    def __init__(self,title:str,authors:list,publication:str,isbn:str,language:str,ebook:bool):
        self.title=title
        self.authors=authors
        self.publication=publication
        self.isbn=isbn
        self.language=language
        self.ebook=ebook
    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.authors
    def getPublication(self):
        return self.publication

class Library:
    def __init__(self,inventory:list):
        self.inventory=inventory
    def serveBook(self,title:str):
        self.inventory-=title
    def recieveBook(self,title:str):
        self.inventory+=title
    def list_available_books(self):
        return self.inventory
    def search_book(self, title:str):
        if title in self.inventory:
            return True
        else:
            return False

class Point:
    def __init__(self,x_pos:float,y_pos:float):
        self.x_pos=x_pos
        self.y_pos=y_pos
    def getCoordinate(self):
        coords=(self.x_pos,self.y_pos)
        return coords
    def move_up(self,value:float):
        self.y_pos+=value
    def move_down(self,value:float):
        self.y_pos-=value
    def move_right(self,value:float):
        self.x_pos+=value
    def move_left(self,value:float):
        self.x_pos-=value
