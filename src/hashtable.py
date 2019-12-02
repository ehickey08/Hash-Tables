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
        self.count = 0
        self.resized = False

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
        LF = self.count/self.capacity
        if LF >= 0.7:
            self.resize()

        self.count += 1
        index = self._hash_mod(key)
        current_node = self.storage[index]

        while current_node:
            if current_node.key == key:
                current_node.value = value
                return;
            elif current_node.next:
                current_node = current_node.next
            else:
                current_node.next = LinkedPair(key, value)
                return

        self.storage[index] = LinkedPair(key, value)


    def remove(self, key):
        LF = self.count/self.capacity
        if LF <= 0.2 and self.resized:
            self.resize(factor = 0.5)

        self.count -= 1
        index = self._hash_mod(key)
        current_node = self.storage[index]

        if current_node:
            if current_node.key == key:
                self.storage[index] = current_node.next
                return

            while current_node.next:
                prev_node = current_node
                current_node = current_node.next
                if current_node.key == key:
                    prev_node.next = current_node.next
                    return;

        return None

    def retrieve(self, key):
        index = self._hash_mod(key)
        current_node = self.storage[index]
        if current_node:
            while current_node:
                if current_node.key == key:
                    return current_node.value;
                current_node = current_node.next
            return None

        else:
            return None

    def resize(self, factor =  2):
        self.resized = True
        self.capacity = self.capacity * 2 if factor is 2 else self.capacity // 2
        old_storage = self.storage
        old_count = self.count
        new_storage = [None] * self.capacity
        self.storage = new_storage
        for node in old_storage:
            if node:
                while node:
                    self.insert(node.key, node.value)
                    node = node.next
        self.count = old_count



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
