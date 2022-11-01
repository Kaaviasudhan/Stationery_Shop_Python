from datetime import datetime
from datetime import date
import numpy as np

items = [
          ["Pencil",  7],
          ["Eraser", 5],
          ["Fountain Pen", 45],
          ["Ballpoint Pen",  10]
]    
# Create a node
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def printList(self):
        temp_node = self.head
        j = 1
        while (temp_node):
            print("\nBill no:",j, "\nDate   :", temp_node.item[0], "\nTime   :", temp_node.item[1], "\nAmount :",temp_node.item[2], "\n")
            j = j + 1
            temp_node = temp_node.next

stack = []
store = []
llist = LinkedList()
print("Welcome to Stationery Shop")
while (1):    
    print("\n\tMenu")
    choice = int(input("\n1.Add Product details \n2.Edit Product details \n3.Delete Product details \n4.Display all items\n5.Purchase Items \n6.View Purchase details \n7.Display all Bill details\n8.Exit\nEnter one option\n"))
    if (choice == 1):
        temp = []
        temp.append(input("Enter Product Name :"))
        temp.append(int(input("Enter Price :")))
        items.append(temp)
    
    elif (choice ==2):
        print("Choose from the Available Items to Edit.")
        print("\n   S.No\t Item Name \tPrice")
        for a in range(len(items)):
            print("\n\t", a + 1, " .", end="  ")
            for b in range(2):
                print(items[a][b], " ", end="  ")
    
        o = int(input("\n\nEnter S.No"))
        o1 = int(1)
        while (o1>=1 and o1<=2):
            print("Choose the Detail to be Edited.")
            print("\n1. Name :", items[o - 1][0], "\n2. Price :", items[o - 1][1],"\nPress any other key to stop Editing ")
            o1 = int(input("\nEnter the No to edit"))
            if (o1>=1 and o1<=2):
                items[o-1][o1-1] = input("Enter the Changed Detail :")
            else:
                print("Editing has been Terminated.....")
                break

    elif (choice==3):
            print("Choose from the Available Items to Edit.")
            print("\n   S.No\t Product Name\t\tPrice")
            for a in range(len(items)):
                print("\n  ", a + 1, " .", end="  ")
                for b in range(2):
                    print(items[a][b], "\t", end="  ")
            o = int(input("\nEnter S.No"))    
            temp = np.delete(items,o-1,0)
            items = temp
            print(items)

    elif (choice==4):
        for x in items:
            print(x)

    elif (choice == 5):
        i = 1
        count = 0
        total = 0
        now = datetime.now()
        today = date.today()
        current_time = now.strftime("%H:%M:%S")
        
        while(1):            
            print("\nFor Item No",i,"Choose an Item")            
            print("\nS.No\t Product Name\tPrice ")
            for a in range(len(items)):
                print("\n  ", a + 1, " .", end="  ")
                count+=1
                for b in range(2):
                    if(b==1):
                        print("Rs.",items[a][b],"\t", end="  ")
                    else:
                        print(items[a][b],"\t", end="  ")
                    

            print("\n\nEnter ",a+2," to Proceed to payment")
            h = int(a+2)
            o = int(input("\nEnter an Item No"))
            if(o==h):
                print("\nTotal Amount : Rs. ",total)  
                break              
            else:
                price = items[o-1][1]
                total += price            
            i+=1
        z= today
        store.append(z)
        z = current_time
        store.append(z)
        z = total   
        store.append(z)        
        llist.insertAtEnd(store)   
        stack.append(["Purchasing"," was"," done"," at", current_time])
        store = []

    elif (choice == 6):
        j = 1
        for x in range(len(stack) - 1, -1, -1):
            y = stack[x]
            print(j, ".", y[0], y[1], y[2],y[3],y[4])
            y = []
            j = j + 1
            
    elif (choice == 7):
        if llist.head == None:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            stack.append(["All ", "Purchase details", "were attempted to display","(nothing was found) at", current_time])
            print("No Purchase records to display")
        else:
            llist.printList()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            stack.append(["All ", "Purchase Records", "were","displayed at", current_time])

    else:
            print("Thank You !!")
            exit()
