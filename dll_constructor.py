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
    
    # @TODO - Finish get_node method
    def get_node(self, index):
        if self.length == 0: return None
        temp = self.head
        counter = 1
        node_index = counter - 1

        while temp.next:
            if node_index == index:
                temp = temp.next
                temp.next.prev

        return


dll_1 = Doubley_Linked_lists(133)
dll_1.append_node(399)
dll_1.append_node(800)
dll_1.append_node(84400)





dll_1.print_list()


        
        
