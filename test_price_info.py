import price_info as pi

def test_total_shipping_cost():
    result = pi.total_cost_shopping()
    assert (result == 46.75)

def test_cost_of_fruits():
    result = pi.cost_of_fruits('apple', 10)
    assert (result == 12.0)