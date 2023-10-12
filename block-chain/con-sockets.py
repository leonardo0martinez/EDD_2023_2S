import hashlib
import json
import socket
import select
import sys
import msvcrt
import subprocess
import os
from datetime import datetime
"""



                                        DOUBLY LINKED LIST



"""
class block_node:
    def __init__(self, index, time_stamp, class_name, data, previous_hash, current_hash):
        self.data = data
        self.index = index
        self.time_stamp = time_stamp
        self.class_name = class_name
        self.data = data
        self.previous_hash = previous_hash
        self.current_hash = current_hash
        self.next = None
        self.prev = None

class block_list:
    def __init__(self):
        self.head = None

    def add(self, block):
        current = block
        if(self.head == None):
            self.head = current
        else:
            temp = self.head
            self.head = current
            current.next = temp
            temp.prev = current
    
    def choose_block(self):
        i = 1
        answer = None
        if(self.head != None):
            print("SELECT A BLOCK")
            print("_______________________________________________")
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            while(temp != None):
                print(str(i)+". - ", temp.class_name)
                i = i + 1
                temp = temp.prev
            print("_______________________________________________")
            selected_block = int(input("Type an option: "))
            selected_block = selected_block - 1
            temp = self.head
            while(temp != None):
                if(temp.index == selected_block):
                    answer = temp
                temp = temp.next
            return answer
        else:
            return answer

    def get_size(self):
        size = 0
        if(self.head != None):
            temp = self.head
            while(temp != None):
                size = size + 1
                temp = temp.next
            return size
        else:
            return size

    def previous_hash_match(self, block):
        if(self.head == None):
            if(block.previous_hash == "0000"):
                return True
            else:
                return False
        else:
            if(self.head.current_hash == block.previous_hash):
                return True
            else:
                return False

    def get_last_index(self):
        if(self.head == None):
            return 0
        else:
            return (self.head.index + 1)

    def get_last_hash(self):
        if(self.head != None):
            return self.head.current_hash
        else:
            return "0000"
    
    def is_empty(self):
        if(self.head == None):
            return True
        else:
            return False

    def print_report(self):
        code = "digraph G {  \n  node[shape = rectangule, style = filled, color = lightsalmon]; \n"
        if(self.head != None):
            temp = self.head
            conections = ""
            while(temp != None):
                code = code + "S" + str(temp.index) + "[label = \"Class: "+temp.class_name+"\\n Time Stamp: "+temp.time_stamp+"\\n Previous Hash: "+temp.previous_hash[:10]+"\\n Current Hash:"+temp.current_hash[:10]+"\"]; \n"
                if(temp.next == None):
                    conections = conections + "S" + str(temp.index)
                else:
                    conections = conections + "S" + str(temp.index) + " -> "
                temp = temp.next
            code = code + "\n" + conections + "[dir = \"both\"];\n }"
            f = open("block_chain.dot","w+")
            f.write(code) 
            f.close()
            os.system("dot -Tpng \""+os.getcwd()+"\\block_chain.dot\" -o \""+os.getcwd()+"\\block_chain.png\"")
            os.system("explorer \""+os.getcwd()+"\\block_chain.png\"")
        else:
            print("No blocks has been added.")
            
#BLOCK LIST XD XD XD
block_chain = block_list()

"""



                                        BINARY SERACH TREE



"""

class tree_node():
    def __init__(self, id, carne, nombre):
        self.carne = carne
        self.nombre = nombre
        self.left = None
        self.right = None

nodes = [""]
conections = ""
states = ""
class Tree():
    def __init__(self):
        self.root = None

    def load_tree(self, block):
        self.load_recursive(block.data)
        print("Data Readed")
        self.parse(nodes)

    def load_recursive(self, data_str):
        global nodes
        data = json.loads(data_str)
        nodes.append(data['value'])
        if(data['left'] != None or data['right'] != None):
            if(data['left'] != None):
                self.load_recursive(json.dumps(data['left']))
            if(data['right'] != None):
                self.load_recursive(json.dumps(data['right']))

    def parse(self, nodes):
        if(nodes != None):
            i = 0
            for element in nodes:
                arr = ["", ""]
                arr = element.split('-')
                if(len(arr) > 1):
                    temp = tree_node(i, arr[0], arr[1])
                    self.add(temp)
                i = i + 1
        else:
            print("Empty List XD")
        
    def add(self, node):
        if(self.root == None):
            self.root = node
        else:
            self.recursive(self.root, node)

    def recursive(self, current, temp):
        if (int(temp.carne) < int(current.carne) ):
            if (current.left != None):
                self.recursive(current.left, temp)
            else:
                current.left = temp
        elif (int(temp.carne) > int(current.carne) ):
            if (current.right != None):
                self.recursive(current.right, temp)
            else:
                current.right = temp

    def inOrder_report(self):
        global conections
        global states
        conections = ""
        states = ""
        self.inOrder_recursive(self.root)
        code = "digraph G {\n rankdir = LR \n node[shape=\"rectangule\", style = filled, color = burlywood1]" + states + conections + "\n }"
        f = open("inOrder_report.dot","w+")
        f.write(code) 
        f.close()
        os.system("dot -Tpng \""+os.getcwd()+"\\inOrder_report.dot\" -o \""+os.getcwd()+"\\inOrder_report.png\"")
        os.system("explorer \""+os.getcwd()+"\\inOrder_report.png\"")
    
    def preOrder_report(self):
        global conections
        global states
        conections = ""
        states = ""
        self.preOrder_recursive(self.root)
        code = "digraph G {\n rankdir = LR \n node[shape=\"rectangule\", style = filled, color = burlywood1]" + states + conections + "\n }"
        f = open("preOrder_report.dot","w+")
        f.write(code) 
        f.close()
        os.system("dot -Tpng \""+os.getcwd()+"\\preOrder_report.dot\" -o \""+os.getcwd()+"\\preOrder_report.png\"")
        os.system("explorer \""+os.getcwd()+"\\preOrder_report.png\"")

    def postOrder_report(self):
        global conections
        global states
        conections = ""
        states = ""
        self.postOrder_recursive(self.root)
        code = "digraph G {\n rankdir = LR \n node[shape=\"rectangule\", style = filled, color = burlywood1]" + states + conections + "\n }"
        f = open("postOrder_report.dot","w+")
        f.write(code) 
        f.close()
        os.system("dot -Tpng \""+os.getcwd()+"\\postOrder_report.dot\" -o \""+os.getcwd()+"\\postOrder_report.png\"")
        os.system("explorer \""+os.getcwd()+"\\postOrder_report.png\"")

    def tree_report(self):
        global conections
        global states
        conections = ""
        states = ""
        self.tree_recursive(self.root)
        code = "digraph G {\n node[shape=\"rectangule\", style = filled, color = lightsteelblue1]" + states + conections + "\n }"
        f = open("tree_report.dot","w+")
        f.write(code) 
        f.close()
        os.system("dot -Tpng \""+os.getcwd()+"\\tree_report.dot\" -o \""+os.getcwd()+"\\tree_report.png\"")
        os.system("explorer \""+os.getcwd()+"\\tree_report.png\"")

    def tree_recursive(self, current):
        global conections
        global states
        if(current.left != None):
            conections = conections + "S" + current.nombre + " -> "
            conections = conections + "S" + current.left.nombre + " \n"
            self.tree_recursive(current.left)
        states = states + "S" + current.nombre
        states = states + "[ label = \" Nombre: "+current.nombre+" \\n Carné: " + current.carne+"\" ];"
        states = states + "\n"
        if(current.right != None):
            conections = conections + "S" + current.nombre + " -> "
            conections = conections + "S" + current.right.nombre + " \n"
            self.tree_recursive(current.right)
            
    def inOrder_recursive(self, current):
        global conections
        global states
        if (current.left != None):
            self.inOrder_recursive(current.left)
            conections = conections + " -> "
        states = states + "S" + current.nombre
        states = states + "[ label = \" Nombre: "+current.nombre+" \\n Carné: " + current.carne+"\" ];"
        states = states + "\n"
        conections =  conections + "S" + current.nombre
        if (current.right != None):
            conections = conections + " -> "
            self.inOrder_recursive(current.right)
            
    def preOrder_recursive(self, current):
        global conections
        global states
        states = states + "S" + current.nombre
        states = states + "[ label = \" Nombre: "+current.nombre+" \\n Carné: " + current.carne+"\" ];"
        states = states + "\n"
        conections =  conections + "S" + current.nombre
        if (current.left != None):
            conections = conections + " -> "
            self.preOrder_recursive(current.left)
        if (current.right != None):
            conections = conections + " -> "
            self.preOrder_recursive(current.right)

    def postOrder_recursive(self, current):
        global conections
        global states
        if (current.left != None):
            self.postOrder_recursive(current.left)
            conections = conections + " -> "
        if (current.right != None):
            self.postOrder_recursive(current.right)
            conections = conections + " -> "
        states = states + "S" + current.nombre
        states = states + "[ label = \" Nombre: "+current.nombre+" \\n Carné: " + current.carne+"\" ];"
        states = states + "\n"
        conections =  conections + "S" + current.nombre

main_tree = Tree()
"""



                                        OTHERS METHODS



"""
def generate_hash(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode('ascii')).hexdigest()
    return sha_signature

def load_file(path):
    global block_chain
    arr = ["",""]
    csv_file = open(path, "r")
    temp = csv_file.read().split('\n')
    for i in range(len(temp)):
        line = temp[i].split(';')
        if(line[0] == 'class'):
            arr[0] = line[1]
        elif(line[0] == 'data'):
            arr[1] = line[1]
    csv_file.close()
    index = block_chain.get_last_index()
    class_name = arr[0]
    data = arr[1]
    now = datetime.now()
    time_stamp = now.strftime("%d-%m-%Y::%H:%M:%S")
    previous_hash = str(block_chain.get_last_hash())
    current_hash = generate_hash(str(index)+time_stamp+class_name+data+previous_hash)
    a_block = block_node(index, time_stamp, class_name, data, previous_hash, current_hash)
    return a_block

def block_to_json(block):
    output = "{\"INDEX\":\""+str(block.index)+"\", \"TIMESTAMP\":\""+block.time_stamp+"\", \"CLASS\":\""+block.class_name+"\", \"DATA\":"+block.data+", \"PREVIOUSHASH\":\""+block.previous_hash+"\", \"HASH\":\""+block.current_hash+"\"}"
    return output

def json_to_block(json_string):
    data = json.loads(json_string)
    index = int(data['INDEX'])
    time_stamp = data['TIMESTAMP']
    data2 = str(data['DATA']).replace("None", "null")
    class_name = data['CLASS']
    previous_hash = data['PREVIOUSHASH']
    current_hash = data['HASH']
    blck = block_node(index, time_stamp, class_name, data2, previous_hash, current_hash)
    return blck

"""                                                                                     



                                        APP MAIN MENU



"""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

recieve_block = None
def wait_block():
    global server
    global block_chain
    global block_node
    while True:
        data = server.recv(1024).decode('utf-8')
        if("INDEX" in data):
            recieve_block = json_to_block(data)
            if(block_chain.previous_hash_match(recieve_block)):
                block_chain.add(recieve_block)
                print("Received block has been added :)")
                server.sendall('true'.encode('utf-8'))
            else:
                print("Received block has been ignored :v")
                server.sendall('false'.encode('utf-8'))
        else:
            print("Recived: ", data)


def main_menu():
    global server
    global block_chain
    global main_tree
    menu = 0
    block_reports = None
    while(True):
        #--------------------------------------------------------------------------------------------------------MAIN MENU
        print("MAIN MENU")
        print("_______________________________________________")
        print("1. - Insert Block")
        print("2. - Select Block")
        print("3. - Reports")
        print("4. - Exit")
        print("_______________________________________________")
        menu = int(input("Type an option: "))
        if(menu == 1):
            #---------------------------------------------------------------------------------------------------INSERT BLOCK
            print("INSERT BLOCK")
            print("_______________________________________________")
            path = input("Type a CSV file path:  ")
            new_block = load_file(path)
            print("New block sended: ", new_block.class_name)
            temp = block_to_json(new_block)
            server.sendall(temp.encode('utf-8'))
            if(block_chain.previous_hash_match(new_block)):
                block_chain.add(new_block)
                print("New block added :)")
            else:
                print("Block has been ignored.")
            print("_______________________________________________")
            print("0. - Main Menu")
            menu = int(input("Type an option: "))
        elif(menu == 2):
            #---------------------------------------------------------------------------------------------------SELECT BLOCK
            print("SELECT BLOCK") 
            print("_______________________________________________")
            block_reports = block_chain.choose_block()
            if(block_reports != None):
                print("Selected block: ", block_reports.class_name)
            else:
                print("Selected block:  None")
            print("_______________________________________________")
            print("0. - Main Menu")
            menu = int(input("Type an option: "))
        elif(menu == 3):
            #---------------------------------------------------------------------------------------------------REPORTS
            print("REPORTS")
            if(block_chain.is_empty()):
                print("The block chain list is empty.")
                print("_______________________________________________")
                print("0. - Main Menu")
                menu = int(input("Type an option: "))
            else:
                if(block_reports != None):
                    print("1. - Block Chain Report")
                    print("2. - " + block_reports.class_name + " Tree Report")
                    print("_______________________________________________")
                    menu = int(input("Type an option: "))
                    if(menu == 1):                        
                        block_chain.print_report()
                        print("_______________________________________________")
                        print("0. - Main Menu")
                        menu = int(input("Type an option: "))
                    elif(menu == 2):
                        tree = Tree()
                        tree.load_tree(block_reports)
                        print("SELECT TREE REPORT")
                        print("_______________________________________________")
                        print("1. - Tree Report")
                        print("2. - In-Order")
                        print("3. - Pre-Order")
                        print("4. - Post-Order")
                        print("_______________________________________________")
                        menu = int(input("Type an option: "))
                        if(menu == 1):
                            tree.tree_report()
                            print("Done! :v")
                        elif(menu == 2):
                            tree.inOrder_report()
                            print("Done! :v")
                        elif(menu == 3):
                            tree.preOrder_report()
                            print("Done! :v")
                        elif(menu == 4):
                            tree.postOrder_report()
                            print("Done! :v")
                        print("_______________________________________________")
                        print("0. - Main Menu")
                        menu = int(input("Type an option: "))
                else:
                    print("1. - Block Chain Report")
                    print("_______________________________________________")
                    menu = int(input("Type an option: "))
                    if(menu == 1):
                        block_chain.print_report()
                        print("_______________________________________________")
                        print("0. - Main Menu")
                        menu = int(input("Type an option: "))
        elif(menu == 4):
            server.close()
            exit()
            break

import threading
t2 = threading.Thread(target= wait_block)
t1 = threading.Thread(target= main_menu)
t2.start()
t1.start()
t1.join()
t2.join()