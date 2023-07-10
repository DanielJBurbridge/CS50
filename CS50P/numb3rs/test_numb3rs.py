from numb3rs import validate

def test_validate_cs50():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("140.247.235.144") == True
    assert validate("256.255.255.255") == False
    assert validate("64.128.256.512") == False
    assert validate("8.8.8") == False
    assert validate("10.10.10.10.10") == False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert validate("cat") == False

# def test_format():
#     assert Validate_Format('1.23.34.999') == True
#     assert Validate_Format('1:23:34:999') == False
#     assert Validate_Format('1.23:34.999') == False
#     assert Validate_Format('1.23.34.99.222') == False
#     assert Validate_Format('1.23.34.254') == True

# def test_range():
#     assert Validate_Range('10.20.30.40.50.60.70.80.90.100.110.120') == True
#     assert Validate_Range('100.120.130.240.250.160.170.80.190.100.110.120') == True
#     assert Validate_Range('0.133.244.255') == True
#     assert Validate_Range('-23.120.180.200') == False
#     assert Validate_Range('0.120.180.299') == False
#     assert Validate_Range('122.299.270.400') == False
#     assert Validate_Range('299.122.200.100') == False


# def test_length():
#     assert Validate_Length('10.20.30.40.50.60.70.80.90.100.110.120') == False
#     assert Validate_Length('100.120.130.240.250.160.170.80.190.100.110.120') == False
#     assert Validate_Length('0.133.244.255') == True
#     assert Validate_Length('-23.120.180.200') == True
#     assert Validate_Length('0.120.180.299') == True
#     assert Validate_Length('122.233.89') == False

def test_validate():
    assert validate('10.20.30.40.50.60.70.80.90.100.110.120') == False
    assert validate('100.120.130.240.250.160.170.80.190.100.110.120') == False
    assert validate('0.133.244.255') == True
    assert validate('-23.120.180.200') == False
    assert validate('0.120.180.299') == False
    assert validate('122.233.89') == False
    assert validate('122.299.270.400') == False
    assert validate('299.122.200.100') == False