# Entity program in python
# This version is a test version
# Using functions to move elements of an existing ENtity
# Gwenole Capp
# Super Busy Daddy

import numpy as np

Source = ["toto","tata","titi"]
Destination =[]

def insert_to_left (index_source,index_destination):
    "This leaves current element at the same level"
#    to_append = Source[index_source]
    Destination.insert(index_destination,Source[index_source])
    del Source[index_source]
    return

def insert_to_right (index_source,index_destination):
    "This leaves current element at the same level"
#    to_append = Source[byIndex]
    Destination.insert(index_destination+1,Source[index_source])
    del Source[index_source]    
    return


def lower_level (index_source,index_destination):
    "This leaves an element from the source at a lower level than a chosen elementfrom destination"   
    element_at_source = Source[index_source]
    if len(Destination)>0:
        element_at_destination = Destination[index_destination]
        Destination[index_destination]=list([element_at_destination,list([element_at_source])])
    else:
        Destination.append(element_at_source)
    del Source[index_source] 



def upper_level (index_source,index_destination):
    "This leaves an element from the source at an upper level than a chosen elementfrom destination"    
    element_at_source = Source[index_source]
    if len(Destination)>0:
        element_at_destination = Destination[index_destination]
        Destination[index_destination]=list([element_at_source,list([element_at_destination])])
    else:
        Destination.append(element_at_source)
    del Source[index_source]

def Is_Index_in_range (byList,byIndex):
    "This is to check if the index is in range of the list"
    if byIndex<0:
        return 0
    elif byIndex > len(byList)-1:
        return 0
    else:
        return 1
    
def setAction ():
    "to input action to do"
    print ("Enter action to perform:")
    print ("Insert, Replace or Operation (I,R,O)?")
#    print ("SL: Same level to left")
#    print ("SR: Same level to right")
#    print ("LL: Lower level to left")
#    print ("LR: Lower than to right")
#    print ("UL: Upper than to left")
#    print ("UR: Upper than to right")
    print ("'x' to exit")           
    action = input()
    if action == "I" or action == "i":
        print ("Insert at what Level: lower, same, or upper level (-,=,+)?")
        action = input()
        if action == "=":
            print ("Insert to Left or Right(L,R)?")
            action = input()
            if action == "L" or action == "R" or action == "l" or action == "r":
                return action
            else:
                print ("Not a valid choice")
        elif action == "-" or action == "+":
            return action
        else:
            print ("Not a valid choice")
    elif action == "R" or action == "O" or action == "r" or action == "o":
        return action
    else:
        print ("Not a valid choice")
        
            
            

#    if askAction =="SL" or askAction =="SL" or askAction == "SR" or askAction == "LL" or askAction == "LR" or askAction == "UL" or askAction == "UR" or askAction == "x":           
#           return askAction

def display_transfer (listA, listB):
    "This is to display '<listA> -> <listB>'"
    print ("Source:", listA, " -> ", "Destination:", listB)

def setIndex (list_name):
    "to input index of a list"
    print ("Enter Index for list " , list_name)

def setLevel (list_name):
    "to input level of an index of a list"
    print ("Choose at what level to insert an element in ", list_name)
    
def Is_a_String (list_name):
    "To verify if it is a list or a string"
    if isinstance(list_name,str):
        return 1
    else:
        return 0
		
def getElementByIndex(list_name,index):
    "to get the content for a given index of a list"
    print (list_name[index])

def Is_basic_element (list_name,index):
	"True if the element is basic, false otherwise"
	if Is_a_String(list_name[index]):
		return 1
	else:
		return 0

def printAllElements (list_name):
	"print all elements of a list"
	for index in range(len(list_name)):
		print ("element ",index," of ",list_name," is ",list_name[index])

def getIndex (list_name):
        printAllElements (list_name)		
        setIndex(list_name)
        while True:
            try:
                index = np.uint8(input())
                list_name[index]
                break
            except ValueError:
                print("Please enter an integer")
            except IndexError:
                print ("Index out of range")
        return index
        
def main ():
    "This is the main program"

    action = ""
    while action != "x" and len(Source)>0:
        indexSource = getIndex(Source)
        print (indexSource)
        if len(Destination)>0:
            indexDestination = getIndex(Destination)
            print (indexDestination)
        else:
            indexDestination=0
        if Is_Index_in_range(Source,indexSource):			
            getElementByIndex(Source,indexSource)
            action=setAction()
            print (Is_Index_in_range(Source,indexSource))
            if action == "L" or action == "l":
                insert_to_left(indexSource,indexDestination)
            elif action == "R" or action == "r":
                insert_to_right(indexSource,indexDestination)
            elif action == "-":
                lower_level (indexSource,indexDestination)
            elif action == "+":
                upper_level (indexSource,indexDestination)
            else:
                print ("No comprendo")
            display_transfer(Source, Destination)
            printAllElements (Source)
            printAllElements (Destination)

			
main()




