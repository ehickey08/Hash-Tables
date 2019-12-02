# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        if self.count >= self.capacity:
            self.resize()

        self.count += 1
        hash_key = self._hash(key) % self.capacity
        current_node = self.storage[hash_key]
        if current_node:
            while current_node.next:
                current_node = current_node.next
            current_node.next = LinkedPair(key, value)
        else:
            self.storage[hash_key] = LinkedPair(key, value)




    def remove(self, key):
        self.count -= 1
        hash_key = self._hash(key) % self.capacity
        current_node = self.storage[hash_key]

        if current_node:
            if current_node.key == key:
                self.stroage[hash] = current_node.next
            else:
                while current_node:
                    prev_node = current_node
                    current_node = current_node.next
                    if current_node.key == key:
                        prev_node.next = current_node.next
                        return;
                print("The key does not exist in the hash table.")

        else:
            print("The key does not exist in the hash table.")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        pass


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



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

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
