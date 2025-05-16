#1.Search an element in a linked list

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def search(head,key):
    
    curr = head
    while curr is not None:
        if curr.data == key:
            return True
        curr = curr.next
    return False

if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    key = 56

    if search(head, key):
        print('Yes')
    else:
        print('No')

#2. Insert a node at the end of a linked list

class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    last = head
    while last.next:
        last = last.next
    last.next = new_node
    return head
def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original linked list:")
    print_list(head)

    new_data = 6
    head = insert_at_end(head, new_data)

    print("Linked list after inserting at the end:")
    print_list(head)

#3.Length of singly linked list
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def count_nodes(head):

    count = 0
    curr = head

    while curr is not None:

        count += 1
        curr = curr.next

    return count
    
if __name__ == "__main__":

    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(1)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)

    print('Count the number of nodes',count_nodes(head))

# Reverse a linked list 

class Node:

    def __init__(self, newData):
        self.data = newData
        self.next = None
    
def reverseList(head):
    curr = head
    prev = None

    while curr is not None:

        nextNode = curr.next
        curr.next = prev

        prev = curr
        curr = nextNode
    
    return prev 

def printList(node):
    while node is not None:
        print(f"{node.data}")
        node = node.next

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    printList(head)
    head = reverseList(head)

    print("Reversed linked list:")
    printList(head)

