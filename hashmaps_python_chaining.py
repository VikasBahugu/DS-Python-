class Hash():
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size

    def add(self,key,value):
        key_value = [key,value]
        key_hash = self.get_hash(key)
        if self.map[key_hash] == None:
            self.map[key_hash] = list([key_value])

        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self,key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    print("Value for key '",key,"' is: ",pair[1])

    def delete(self,key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for i in range(0,len(self.map[key_hash])):
                if self.map[key_hash][i][0] == key:
                    print("Deleted value-pair: ", self.map[key_hash][i])
                    self.map[key_hash].pop(i)


    def print(self):
        for item in self.map:
            if item != None:
                print(item)

has1 = Hash()
has1.add("Vivek",23)
has1.add("Apporva",12)
has1.add("Swetank",22)
has1.add("Vikas",29)
has1.add("Anupam",45)
has1.add("Gaurav",25)
has1.print()
has1.get("Swetank")
has1.delete("Anupam")
has1.print()
# key_hash
# key_value
# hash
