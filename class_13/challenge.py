def reverse_ll(list):

       previous = None
       current = list.head

  
       while current:
           current.next = previous   
           previous = current
           current = next
           if next:
               next = currnet.next

       list.head = current

# https://realpython.com/python-reverse-list/

def reverse_list(list):
    for i in range(len(liost) // 2):
        list[i], list[-1 - i] = list[-1 - i], list[i]