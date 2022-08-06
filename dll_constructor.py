class Node():
    def __init__(self, value):
        self.next = None
        self.value = value
        self.previous = None
        


class Doubley_Linked_lists():
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        if self.length == 0:
            print("You have no items in your list!")
        else:    
            while temp is not None:
                print(temp.value)
                temp = temp.next
            print(f"The current LENGTH of your list is: {self.length}")         
        return 

    def append_node(self, value):
        new_node = Node(value)

        #Check if the list is empty ( if they delete all nodes )
        if (self.head == None and self.tail == None):
            self.head == new_node
            self.tail == new_node
            return True

        #Grab a copy of the current position for tail
        temp_tail = self.tail        
        #Move the original tail to the new node
        self.tail = new_node
        #Link the last node (the new Node) to the previous one.
        self.tail.previous = temp_tail
        #Link the previous Node to the Last node
        temp_tail.next = self.tail

        #Increase the length of the double-linked list
        self.length += 1
        return True

    def pop_node(self):
        #User cannot pop and empty Node
        if self.length == 0: return None
        temp = self.tail        
        #If the user is removing the last node
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.previous
            self.tail.next = None
            temp.previous = None
        self.length -= 1
        return temp
    
    # def prepend_node_v1(self, value):
    #     #If adding to an empty list
    #     if self.length == 0:
    #         self.head = Node(value)
    #         self.tail = Node(value)
    #     else:
    #         temp = Node(value)
    #         #Place new node behind current head_node
    #         self.head.previous = temp
    #         #Add Link the new_node to the rest of the list.
    #         temp.next = self.head 
    #         #Make the new Node; the head.
    #         self.head = temp           
    #     self.length += 1
    #     return True

    def prepend_node_v2(self, value):
        '''This one is more efficient because we're already declaring the new_node (one-time)
            instead of calling it multiple times as "Node(value)"
        '''
        new_node = Node(value)
        #If adding to an empty list
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = new_node
            #Place new node behind current head_node
            self.head.previous = temp
            #Add Link the new_node to the rest of the list.
            temp.next = self.head 
            #Make the new Node; the head.
            self.head = temp           
        self.length += 1
        return True

    def pop_first_node(self):
        # Users who try to pop from an empty list
        if self.length == 0: return None

        #grab copy of first node
        temp = self.head

        # Users who pop off the last node
        if self.length == 1:
            self.head = None
            self.tail = None
        else:         
            #Pop off the first node
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    # 
    # def get_node_v1(self, index):
    #     if index < 0 or index >= self.length:
    #         return None
    #     temp = self.head
    #     if index < self.length/2:
    #         for _ in range(index):
    #             temp = temp.next
    #     else:
    #         temp = self.tail
    #         for _ in range(self.length - 1, index, -1):
    #             temp = temp.prev  
    #     return temp.next
    
    def get_node_v2(self, index):
        '''Version 2 for GET method has only one Looper'''
        # User must enter a valid index
        if ( index < 0 ) or ( index > self.length - 1 ):
            return None
        counter = 1
        node_index = None
        temp = self.head

        #If 
        while temp.next:
            if node_index == index:
                break
            else:
                temp = temp.next
                counter += 1
                node_index = counter - 1              
        return temp
    # @TODO  Complete Set Method
    def set_node(self, index):
        return


dll_1 = Doubley_Linked_lists("A")
dll_1.append_node("B")
dll_1.append_node("C")
dll_1.append_node("D")
dll_1.append_node("E")
dll_1.append_node("F")
dll_1.append_node("G")
dll_1.append_node("H")
dll_1.append_node("I")

print(f"GET {dll_1.get_node_v2(5).value}")

dll_1.print_list()


        
        
