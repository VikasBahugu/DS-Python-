class HashFun:
    def __init__(self,a):
        self.a = a
        self.hash_list = [None] * self.a

    def hash_fun(self,elem):
        self.elem = elem
        for i in range(0, a):
            self.hash_ind = self.elem[i] % self.a
            if self.hash_list[self.hash_ind] == None:
                self.hash_list[self.hash_ind] = self.elem[i]
                print("Added   : ",self.hash_list)
            else:
                self.hash_list.append(self.elem[i])
                print("Appended: ",self.hash_list)
        return self.hash_list

    def print(self):
        print("Elements are:>")
        for i in range(0,self.a):
            if self.hash_list[i] == None:
                pass
            else:
                print(self.hash_list[i],end=", ")

    def find_elem(self,n,a):
        self.hash_ind = n % a
        if n ==self.hash_list[self.hash_ind]:
            print("Element ",n," is present.")
        else:
            print("Element does not exist.")


a = int(input("Enter length: "))
elem = list(map(int,input("Enter Elements: ").split()))[:a]

val = HashFun(a)
val.hash_fun(elem)
val.print()
# find = int(input("Enter the element to find: "))
# val.find_elem(find,a)