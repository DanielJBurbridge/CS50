from plates import is_valid

def test_isvalid_starts_with_two_letters():
    assert is_valid("AA2222") == True
    assert is_valid("2A9999") == False
    assert is_valid("A1BBBB") == False
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2AA") == False

def test_isvalid_contains_two_to_six_letters():
    assert is_valid("AAZZZZ") == True
    assert is_valid("BB") == True
    assert is_valid("X") == False
    assert is_valid("ZYFP801") == False

def test_isvalid_ends_with_numbersequence_without_leading_zero():
    assert is_valid("BBSE09") == False
    assert is_valid("BBS880") == True
    assert is_valid("YU92JK") == False
    assert is_valid("RFD987") == True

def test_isvalid_does_not_contain_punctuation():
    assert is_valid("DD3290") == True
    assert is_valid("DD9!.9") == False