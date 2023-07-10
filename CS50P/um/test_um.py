# PYTEST written with assistance from CHATGPT
import pytest
from um import count


@pytest.mark.parametrize("text, expected_count", [
    ("um", 1),  # Single occurrence of 'um'
    ("um um", 2),  # Multiple occurrences of 'um'
    ("UM UM", 2),  # Case-insensitive counting
    ("umbrella", 0),  # 'um' within a word
    ("The quick brown fox jumps over the lazy um.", 1),  # 'um' at the end of a sentence
    ("umbrage", 0),  # 'um' within a longer word
    ("", 0),  # Empty string
    ("um, um, um!", 3),  # 'um' with punctuation
    ("Humpty Dumpty sat on a wall.", 0),  # 'um' not present
    ("Gumby and his friends were having fun.", 0),  # 'um' not present
    ("The umpire made a controversial call.", 0),  # 'um' as part of another word
    ("Umm... I'm not sure.", 0),  # 'um' with extra characters
    ("    um     um     ", 2),  # 'um' surrounded by whitespace
    ("Multiple ums in a row: um um um", 3),  # 'um' with adjacent occurrences
    ("The Umayyad dynasty ruled during the 7th century.", 0),  # 'um' not present
    ("The movie was humdrum and uninspiring.", 0),  # 'um' not present
])

def test_count(text, expected_count):
    assert count(text) == expected_count