from ..test import check, connection_check, requests1, urls, log

"""TESTING FUNCTION"""

def test_check():
    assert check(urls) == None

def test_requests_GET():
    assert requests1(200, urls[1], "GET") == None

def test_requests_POST():
    assert requests1(200, urls[1], "POST") == None

def test_requests_GET_failed():
    assert requests1(405, urls[1], "GET") == None

def test_requests_POST_failed():
    assert requests1(405, urls[1], "POST") == None