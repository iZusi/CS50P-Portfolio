from numb3rs import validate


# test cases for validate function
def test_valid_ip():
    valid_ips = ["192.168.1.1", "10.0.0.1", "255.255.255.255", "127.0.0.1"]
    for ip in valid_ips:
        assert validate(ip) == True

def test_invalid_ip():
    invalid_ips = ["256.0.0.1", "192.168.1.256", "abc.def.ghi.jkl", "192.168.1"]
    for ip in invalid_ips:
        assert validate(ip) == False
