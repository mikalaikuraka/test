from test import check, connection_check, requests1, urls

"""TESTING FUNCTION"""

# def test_check():
#     assert check(3) == 5
#     pass

def test_requests1():
    assert requests1(200, urls[1]) == None


# def test_connection_check():
#     assert connection_check(url) == 5

