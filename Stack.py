class Stack:
    stack = []
    def __init__(self,size):
        self.size = size

    def isFull(self):
        if self.size == len(Stack.stack):
            return True
        else:
            return False

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False        
                    
    def push(self,data):
        if self.isFull():
            print("Stack OverFlow !")
        else:
            Stack.stack.append(data)
            print("Data Inserted ...")            

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow !")        
        else:
            s = Stack.stack.pop()
            print(f"{s} Deleted ...") 

    def display(self):
        if self.isEmpty():
            print("Stack is Empty !") 
        else:
            for i in Stack.stack:
                print(i , end=" ")
            print()    


if __name__ == '__main__':
    size = int(input("Enter the Stack Size > "))
    stack = Stack(size)
    try:
        while True:
            print("===================")
            print("1 : Push")
            print("2 : Pop")
            print("3 : Display")
            print("0 : Exit")
            
            opt = int(input("Enter Option > "))
            if opt == 1:
                ele = int(input("Enter Element > "))
                stack.push(ele)

            if opt == 2:
                stack.pop()

            if opt == 3:
                stack.display()

            if opt == 0:
                break

    except Exception as e:
        print(e)


    

