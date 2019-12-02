# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"({self.key}, {self.value})"

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def _hash(self, key):
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        index = self._hash_mod(key)
        current_node = self.storage[index]
        if current_node:
            while current_node:
                if current_node.key == key:
                    current_node.value == value
                    return;
                elif current_node.next:
                    current_node = current_node.next
                else:
                    current_node.next = LinkedPair(key, value)
                    return

        else:
            self.storage[index] = LinkedPair(key, value)




    def remove(self, key):
        index = self._hash_mod(key)
        current_node = self.storage[index]

        if current_node:
            prev_node = current_node.next
            while current_node:
                if current_node.key == key:
                    prev_node.next = current_node.next
                    return;
                prev_node = current_node
                current_node = current_node.next

        return "The key does not exist in the hash table."

    def retrieve(self, key):
        hash_key = self._hash(key) % self.capacity
        current_node = self.storage[hash_key]
        if current_node:
            while current_node:
                if current_node.key == key:
                    return current_node.value;
                current_node = current_node.next
            return "The key does not exist in the hash table..."

        else:
            return "The key does not exist in the hash table."

    def resize(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(len(self.storage)):
            if self.storage[i]:
                key = self.storage[i].key
                hash_key = self._hash(key) % self.capacity
                new_storage[hash_key] = self.storage[i]
        self.storage = new_storage



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
