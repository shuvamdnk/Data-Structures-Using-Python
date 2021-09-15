class Node:
    def __init__(self,data,prev = None,next = None):
        self.prev = prev
        self.data = data
        self.next = next

class DL:
    def __init__(self):
        self.head = None

    def insert_beg(self,data):
        if self.head == None:
            p = Node(data)
            p.prev = None
            p.next = None
            self.head = p
        else:
            r = self.head
            p = Node(data)
            r.prev = p
            p.next = r
            self.head = p


    def insert_end(self,data):
        "This is the function for insert the data in the end of the linked list"
        p = Node(data)
        r = self.head
        while r.next:
            r = r.next
        p.prev = r
        r.next = p
        p.next = None


    def insert_mid(self,data,index):
        r = self.head
        p = Node(data)
        if index == 0:
            self.insert_beg(data)
        count = 0
        while count < index-1:
            r = r.next
            count += 1
        temp = r.next
        r.next = p
        p.prev = r
        p.next = temp
        temp = p

    def delete_beg(self):
        if self.head != None:
            r = self.head
            self.head = r.next
            del r
        else:
            print("Empty")

    def length(self):
        r = self.head
        count = 0
        while r.next != None:
            r = r.next
            count += 1
        return count+1


    def delete_end(self):
        if self.head != None:
            r = self.head
            while r.next.next != None:
                r = r.next
            del r.next.next
            r.next = None
        else:
            print("Empty")


    def print(self):
        p = self.head
        while p.next:
            print(p.data,end=" | ")
            p = p.next
        print(p.data)

dl = DL()
dl.insert_beg(12)
dl.insert_beg(45)
dl.insert_end(55)
dl.insert_end(22)
dl.insert_mid(80,0)
dl.print()

dl.delete_beg()
dl.print()

dl.delete_end()
dl.print()
# print(0<0)