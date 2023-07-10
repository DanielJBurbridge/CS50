from twttr import shorten

def test_shorten_omits_uppervowels():
    assert shorten("HEYTHERE") == "HYTHR"
    # assert shorten("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "abcdefghijklmnopqrstuvwxyzBCDFGHJKLMNPQRSTVWXYZ"

def test_shorten_omits_lowervowels():
    assert shorten("heythere") == "hythr"
    # assert shorten("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "bcdfghjklmnpqrstvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def test_shorten_omits_allvowels():
    assert shorten("HeyThERE") == "HyThR"
    # assert shorten("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

def test_shorten_keeps_numbers():
    assert shorten("Heyheyhey123") == "Hyhyhy123"

def test_shorten_keeps_punctuation():
    assert shorten("Hey, how are you?") == "Hy, hw r y?"
