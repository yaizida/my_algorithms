class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        if not temp:
            print('List is empty.')
            return
        else:
            print('Start:', end=' ')
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('end.')

    def insert(self, data):
        new_node = Node(data)

        # If the linked list is empty
        if self.head is None:
            self.head = new_node

        # If the data is smaller than the head
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node

        else:
            # Locate the node before the insertion point
            current = self.head
            while current.next and new_node.data > current.next.data:
                current = current.next

            # Insertion
            new_node.next = current.next
            current.next = new_node

    def delete(self, key):
        # If the list is empty
        if self.head is None:
            print('Deletion Error: The list is empty.')
            return

        # If the key is in head
        if self.head.data == key:
            self.head = self.head.next
            return

        # Find position of first occurrence of the key
        current = self.head
        while current:
            if current.data == key:
                break
            previous = current
            current = current.next

        # If the key was not found
        if current is None:
            print('Deletion Error: Key not found.')
        else:
            previous.next = current.next


if __name__ == '__main__':
    # Create an object
    LL = LinkedList()
    print('')

    # Insert some nodes
    LL.insert(10)
    LL.insert(12)
    LL.insert(8)
    LL.insert(11)
    LL.insert(10)

    LL.printList()
    LL.delete(7)
    LL.delete(8)
    LL.delete(13)
    LL.printList()
