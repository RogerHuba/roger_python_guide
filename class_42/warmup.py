
def test_sum_values():
    ll_values = LinkedList((10,20,30))
    ll_total = 0
    for i in ll_values:
        ll_total += i
    assert ll_total == 60