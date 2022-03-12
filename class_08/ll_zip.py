def zip_ll_new(ll1, ll2):
    ll3 = LinkedList()
    current1 = ll1.head
    current2 - ll2.head

    # This solution assumes append handles assigning head if there is none

    while current1 or current2:
        if current1 is not None:
            ll3.append(current1value)
            current1 = current1.next
        if current2 is not none:
            ll3.append(current2.next)
            current2 = current2.next
    
    return ll3

def zip_ll_inplace(ll1, ll2):
    current1 = ll1.head
    current2 = ll1.head

    while current1 and current2:
        temp1 = current1.next
        temp2 = current2.next
        current1.next = current2
        if temp1.next :
            current2.next = temp1
        else:
            break
        current1 = temp1
        current2 = temp2

    return ll1
   
