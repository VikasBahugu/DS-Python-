class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def hash_fun(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size

    def add(self,key,value):
        get_hash = self.hash_fun(key)
        key_value = [key,value]
        if self.map[get_hash] is None:
            self.map[get_hash] = key_value
        else:
            i = get_hash + 1
            j = i
            while(j<self.size):
                if self.map[i] is None:
                    self.map[i] = key_value
                    return True
                elif i == self.size + 1:
                    i = 0
                    j += 1
                else:
                    i += 1
                    j += 1
        if None not in self.map:
            print("---------------")
            print("Hash map full. Unable to add: ",key_value)

    def get(self):
        pass

    def delete(self,key):

        def deletes_node(actual_key):
            print("---------------")
            # print("Deleting: ", self.map[get_hash])
            self.map[get_hash] = None
            # self.map.remove(self.map[get_hash])

        get_hash = self.hash_fun(key)
        print("Index should have been:",get_hash)
        if self.map[get_hash][0] == key:
            print(self.map[get_hash][0],key)
            print("To delete:", self.map[get_hash])
            deletes_node(get_hash)
        else:
            i = get_hash
            j = 0

            while(j!=self.size):
                j += 1
                if self.map[i][0] == key:
                    deletes_node(i)
                    return True
                elif i == self.size:
                    i = 0
                else:
                    i += 1


    def prints(self):
        print("---------------")
        for item in self.map:
            print(item)

has1 = HashMap()
has1.add("Vivek",122)
has1.add("Swetank",24)
has1.add("Vikas",23)
has1.add("Anupam",232)
has1.add("Shivani",32)
has1.add("Raju",62)
# has1.add("Ramesh",623) #It will make hash full as max elements are already inserted.
has1.prints()
has1.delete("Vikas")
has1.prints()
has1.delete("Swetank")
has1.prints()

has1.delete("Anupam")
has1.prints()
