class HashTable:
    def __init__(self):
        self.collection = dict()
    
    def hash(self, string):
        sum_of_codes = 0
        for x in string:
            sum_of_codes += ord(x)
        return sum_of_codes
    
    def add(self, key, value):
        hashing_value = self.hash(key)

        if hashing_value not in self.collection:
            self.collection[hashing_value] = {}

        self.collection[hashing_value][key] = value
    
    def remove(self, key):
        hashing_value = self.hash(key)
        if hashing_value not in self.collection:
            return
        
        inner_dict = self.collection[hashing_value]

        if key in inner_dict:
            del inner_dict[key]
        
    
    def lookup(self, key):
        hashing_value = self.hash(key)
        
        if hashing_value not in self.collection:
            return None
        
        inner_dict = self.collection[hashing_value]
        return inner_dict.get(key, None)