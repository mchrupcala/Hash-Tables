# '''
# Linked List hash table key/value pair
# '''

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return self.key + ' ' + self.value + '  ' + str(self.next)

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # def hash_djb2(s):   
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # print(self.storage, len(self.storage))
        index = self._hash_mod(key)
        node = self.storage[index]
        if node is None:
            self.storage[index] = LinkedPair(key, value)
        else:
            print("Collision!", node, key)
            if (node.key == key):
                node.value = value
                return
            else:
                # print("Searching...node.next is: ", node.next)
                while node.next is not None:
                    if (node.key == key):
                        node.value = value
                        break
                    else:
                        node = node.next
                if (node.key == key):
                        node.value = value
                        return
                node.next = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        if (self.retrieve(key) is not None):
            index = self._hash_mod(key)
            node = self.storage[index]
            while node.key != key:
                if node.next is not None:
                    node = node.next
            if (node.key == key):
                node.value = None
        else:
            print("Key was not found...")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        if node is not None:
            while node.key != key and node.next is not None:
                node = node.next
            if (node.key == key):
                return node.value
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity * 2
        old_storage = self.storage
        self.storage = self.capacity * [None]
        print(old_storage)
        for i in old_storage:
            if i is not None:
                while i.next is not None:
                    self.insert(i.key, i.value)
                    i = i.next
                self.insert(i.key, i.value)



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
