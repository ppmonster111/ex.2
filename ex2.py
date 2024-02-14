class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def count_plates(head, eaten):

    current = head
    count = 0
    while current is not None:
        if eaten >= current.value:
            eaten -= current.value
            count += 1
        else:
            break
        current = current.next
    return count

head = Node(2)
head.next = Node(5)
head.next.next = Node(2)
head.next.next.next = Node(1)
head.next.next.next.next = Node(10)

eaten = 10
print(f"กบจะกินแมลงหมดที่จานที่ {count_plates(head, eaten)}")