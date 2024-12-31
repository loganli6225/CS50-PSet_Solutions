from um import count

def test_spaces():
    assert count(" um ") == 1
    assert count(" um um um ") == 3

def test_special_characters():
    assert count(".um.") == 1
    assert count(".um,um!") == 2

def test_start_and_end():
    assert count("um") == 1

def test_start():
    assert count("um ") == 1
    assert count("um?") == 1
    assert count("um um, um?") == 3

def test_end():
    assert count(" um") == 1
    assert count("?um") == 1
    assert count("?um um, um") == 3

def test_part_of_word():
    assert count("yummy") == 0
    assert count("Um, thanks for the album.") == 1
