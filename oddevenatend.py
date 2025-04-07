class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_common_linked_list(list1, list2):
    # Find common elements
    set1 = set(list1)
    set2 = set(list2)
    common_elements = sorted(set1 & set2)  # Sorting to preserve order in input lists

    # Separate odd and even common elements
    odd_elements = [x for x in common_elements if x % 2 != 0]
    even_elements = [x for x in common_elements if x % 2 == 0]

    # Combine odd and even elements while maintaining order
    final_elements = odd_elements + even_elements

    # Create linked list from final elements
    dummy_head = Node(0)  # Temporary dummy head
    current = dummy_head
    for element in final_elements:
        current.next = Node(element)
        current = current.next

    return dummy_head.next  # Return the head of the new linked list

# Example usage
list1 = [1, 2, 3, 6, 7, 8]
list2 = [3, 4, 5, 6]

result_head = create_common_linked_list(list1, list2)

# Print the new linked list (optional, for testing purposes)
current = result_head
while current:
    print(current.data, end=" -> ")
    current = current.next
