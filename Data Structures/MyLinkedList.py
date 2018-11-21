from LinkedList import LinkedList


class MySinglyLinkedList(LinkedList):

    def __init__(self):
        self.head = None

    def append(self, data):
        # O(N) Time Complexity
        node = Node(data)
        if not self.head:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def prepend(self, data):
        # O(1) Time Complexity
        node = Node(data)
        if not self.head:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def delete(self, data):
        # O(N) Time Complexity
        last = self.head

        # Empty head
        if not last:
            return

        # Data located in head
        if last:
            if last.data == data:
                self.head = last.next
                return

        # Search for data
        prev = None
        while last:
            if last.data == data:
                prev.next = last.next
                break
            prev = last
            last = last.next

    def get_nodes(self):
        node_data = []
        last = self.head
        while last:
            node_data.append(last.data)
            last = last.next
        return node_data

    def get_count_elements(self):
        count = 0
        last = self.head
        while last:
            count += 1
            last = last.next
        return count


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    ###########
    # Testing #
    ###########

    linkedlist = MySinglyLinkedList()

    # Append
    linkedlist.append('b')
    linkedlist.append('c')
    linkedlist.append('d')
    linkedlist.append('e')
    linkedlist.append('f')
    linkedlist.append('g')
    linkedlist.append('h')

    # Prepend
    linkedlist.prepend('a')

    # Delete - item not on list
    linkedlist.delete('not_here')

    # Delete - head
    linkedlist.delete('a')

    # Delete - middle
    linkedlist.delete('e')

    # Delete - last
    linkedlist.delete('h')

    # Get of each node element
    # output: ['b', 'c', 'd', 'f', 'g']
    print linkedlist.get_nodes()

    # Count of Node Elements
    # output: 5
    print linkedlist.get_count_elements()
