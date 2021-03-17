import pytest
from _pytest import unittest

from battleships import *

b1 = (4, 5, True, 4, {(4,5), (4,6), (4,7)})
c1 = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
c2 = (7, 5, False, 3, set())
d1 = (1, 1, False, 2, {(2,1)})
d2 = (1, 7, True, 2, set())
d3 = (0, 4, True, 2, set())
s1 = (9, 9, False, 1, {(9,9)})
s2 = (8, 7, False, 1, set())
s3 = (6, 3, True, 1, set())
s4 = (7, 1, True, 1, set())
f = [b1, c1, c2, d1, d2, d3, s1, s2, s3, s4]
#is_sunk tests
# add at least four more tests for is_sunk by the project submission deadline
def test_is_sunk1():
    assert is_sunk(b1) == False

def test_is_sunk2():
    assert is_sunk(c1) == True

def test_is_sunk3():
    assert is_sunk(d1) == False

def test_is_sunk4():
    assert is_sunk(s1) == True

def test_is_sunk5():
    assert is_sunk(s2) == False

#ship_type tests
#add at least one test for ship_type by the deadline of session 7 assignment
#provide at least five tests in total for ship_type by the project submission deadline
def test_ship_type1():
    assert ship_type(c1) == "cruiser"

def test_ship_type2():
    assert ship_type(b1) == "battleship"

def test_ship_type3():
    assert ship_type(d1) == "destroyer"

def test_ship_type4():
    assert ship_type(s1) == "submarine"

def test_ship_type5():
    assert ship_type(s4) == "submarine"

# is_open_sea tests
#add at least one test for open_sea by the deadline of session 7 assignment
#provide at least five tests in total for open_sea by the project submission deadline
def test_is_open_sea1():
    # os = (1, 2, f)
    assert is_open_sea(1, 2, f) == False

def test_is_open_sea2():
    # os = (9, 9, f)
    assert is_open_sea(9, 9, f) == False

def test_is_open_sea3():
    # os = (4, 0, f)
    assert is_open_sea(4, 0, f) == True

def test_is_open_sea4():
    # os = (0, 2, f)
    assert is_open_sea(0, 2, f) == False

def test_is_open_sea5():
    # os = (0, 0, f)
    assert is_open_sea(0, 0, f) == False

#ok_to_place_ship tests
#add at least one test for ok_to_place_ship_at by the deadline of session 7 assignment
#provide at least five tests in total for ok_to_place_ship_at by the project submission deadline
def test_ok_to_place_ship_at1():
    f1 = [b1, c1, d1, d2, d3, s1, s2, s3, s4]
    # ps = (2, 4, True, 3, f1)
    assert ok_to_place_ship_at(2, 4, True, 3, f1) == False

def test_ok_to_place_ship_at2():
    f1 = [c1, c2, d1, d2, d3, s1, s2, s3, s4]
    # ps = (8, 3, False, 4, f1)
    assert ok_to_place_ship_at(8, 3, False, 4, f1) == False

def test_ok_to_place_ship_at3():
    f1 = [c1, c2, d1, d2, d3, s1, s2, s3, s4]
    # ps = (2, 5, True, 4, f1)
    assert ok_to_place_ship_at(3, 5, True, 4, f1) == True

def test_ok_to_place_ship_at4():
    f1 = [b1, c1, c2, d1, d2, d3, s2, s3, s4]
    # ps = (6, 9, True, 1, f)
    assert ok_to_place_ship_at(6, 9, True, 1, f) == True

def test_ok_to_place_ship_at5():
    f1 = [c1, c2, d1, d2, d3, s1, s2, s3, s4]
    # ps = (6, 7, False, 4, f)
    assert ok_to_place_ship_at(6, 7, False, 4, f) == False

# place_ship_at tests
#add at least one test for place_ship_at by the deadline of session 7 assignment
#provide at least five tests in total for place_ship_at by the project submission deadline
def test_place_ship_at1():
    f1 = [b1, c1, d1, d2, d3, s1, s2, s3, s4]
    place_ship_at(7, 5, False, 3, f1)
    assert sorted(f) == sorted(f1)


def test_place_ship_at2():
    f1 = [b1, c1, c2, d1, d3, s1, s2, s3, s4]
    place_ship_at(1, 7, True, 2, f1)
    assert sorted(f) == sorted(f1)

def test_place_ship_at3():
    f1 = [b1, c1, c2, d1, d2, d3, s1, s3, s4]
    place_ship_at(8, 7, False, 1, f1)
    assert sorted(f) == sorted(f1)

def test_place_ship_at4():
    f1 = [c1, c2, d1, d2, d3, s1, s2, s3, s4]
    ns = (4, 5, True, 4, set())
    nf = [ns, c1, c2, d1, d2, d3, s1, s2, s3, s4]
    place_ship_at(4, 5, True, 4, f1)
    assert sorted(nf) == sorted(f1)

def test_place_ship_at5():
    f1 = [c1, c2, d1, d2, d3, s1, s2, s3, s4]
    ns = (2, 5, False, 4, set())
    nf = [ns, c1, c2, d1, d2, d3, s1, s2, s3, s4]
    place_ship_at(2, 5, False, 4, f1)
    assert sorted(nf) == sorted(f1)

#check_if_hits tests
#add at least one test for check_if_hits by the deadline of session 7 assignment
#provide at least five tests in total for check_if_hits by the project submission deadline
def test_check_if_hits1():
    assert check_if_hits(4, 7, f) == False

def test_check_if_hits2():
    assert check_if_hits(0, 9, f) == False

def test_check_if_hits3():
    assert check_if_hits(1, 1, f) == True

def test_check_if_hits4():
    assert check_if_hits(9, 0, f) == False

def test_check_if_hits5():
    assert check_if_hits(4, 4, f) == False

#hit tests
#add at least one test for hit by the deadline of session 7 assignment
#provide at least five tests in total for hit by the project submission deadline
def test_hit1():
    # ship after being hit
    b1h = (4, 5, True, 4, {(4,5), (4,6), (4,7), (4,8)})
    # updated fleet
    f1 = [b1h, c1, c2, d1, d2, d3, s1, s2, s3, s4]
    assert hit(4, 8, f) == (sorted(f1),b1h)

def test_hit2():
    # ship after being hit
    c2h = (7, 5, False, 3, {(7,5)})
    # updated fleet
    f1 = [b1, c1, c2h, d1, d2, d3, s1, s2, s3, s4]
    assert hit(7, 5, f) == (sorted(f1),c2h)

def test_hit3():
    # ship after being hit
    d1h = (1, 1, False, 2, {(1,1), (2,1)})
    # updated fleet
    f1 = [b1, c1, c2, d1h, d2, d3, s1, s2, s3, s4]

    assert hit(1, 1, f) == (sorted(f1),d1h)

def test_hit4():
    # ship after being hit
    s2h = (8, 7, False, 1, {(8,7)})
    # updated fleet
    f1 = [b1, c1, c2, d1, d2, d3, s1, s2h, s3, s4]
    assert hit(8, 7, f) == (sorted(f1),s2h)

def test_hit5():
    # ship after being hit
    s4h = (7, 1, True, 1, {(7,1)})
    # updated fleet
    f1 = [b1, c1, c2, d1, d2, d3, s1, s2, s3, s4h]
    assert hit(7, 1, f) == (sorted(f1),s4h)

#are_unsunk_ships_left tests
#add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
#provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
def test_are_unsunk_ships_left1():
    assert are_unsunk_ships_left(f) == True

def test_are_unsunk_ships_left2():
    b1 = (4, 5, True, 4, {(4,5), (4,6), (4,7), (4,8)})
    c1 = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    c2 = (7, 5, False, 3, {(7,5), (8,5), (9,5)})
    d1 = (1, 1, False, 2, {(1,1),(2,1)})
    d2 = (1, 7, True, 2, {(1,7), (1,8)})
    d3 = (0, 4, True, 2, {(0,4), (0,5)})
    s1 = (9, 9, False, 1, {(9,9)})
    s2 = (8, 7, False, 1, {(8,7)})
    s3 = (6, 3, True, 1, {(6,3)})
    s4 = (7, 1, True, 1, {(7,1)})
    f = [b1, c1, c2, d1, d2, d3, s1, s2, s3, s4]
    assert are_unsunk_ships_left(f) == False

def test_are_unsunk_ships_left3():
    b1 = (4, 5, True, 4, {(4,5), (4,7), (4,8)})
    c1 = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    c2 = (7, 5, False, 3, {(7,5), (8,5), (9,5)})
    d1 = (1, 1, False, 2, {(1,1),(2,1)})
    d2 = (1, 7, True, 2, {(1,7), (1,8)})
    d3 = (0, 4, True, 2, {(0,4), (0,5)})
    s1 = (9, 9, False, 1, {(9,9)})
    s2 = (8, 7, False, 1, {(8,7)})
    s3 = (6, 3, True, 1, {(6,3)})
    s4 = (7, 1, True, 1, {(7,1)})
    f = [b1, c1, c2, d1, d2, d3, s1, s2, s3, s4]
    assert are_unsunk_ships_left(f) == True

def test_are_unsunk_ships_left4():
    b1 = (2, 5, False, 4, {(2,5), (3,5), (4,5)})
    c1 = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    c2 = (7, 5, False, 3, {(7,5), (8,5), (9,5)})
    d1 = (1, 1, False, 2, {(1,1),(2,1)})
    d2 = (1, 7, True, 2, {(1,7), (1,8)})
    d3 = (0, 4, True, 2, {(0,4), (0,5)})
    s1 = (9, 9, False, 1, {(9,9)})
    s2 = (8, 7, False, 1, {(8,7)})
    s3 = (6, 3, True, 1, {(6,3)})
    s4 = (7, 1, True, 1, {(7,1)})
    f = [b1, c1, c2, d1, d2, d3, s1, s2, s3, s4]
    assert are_unsunk_ships_left(f) == True

def test_are_unsunk_ships_left4():
    b1 = (2, 5, False, 4, {(2,5), (3,5), (4,5), (5,5)})
    c1 = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    c2 = (7, 5, False, 3, {(7,5), (8,5), (9,5)})
    d1 = (1, 1, False, 2, {(1,1),(2,1)})
    d2 = (1, 7, True, 2, {(1,7), (1,8)})
    d3 = (0, 4, True, 2, {(0,4), (0,5)})
    s1 = (9, 9, False, 1, {(9,9)})
    s2 = (8, 7, False, 1, {(8,7)})
    s3 = (6, 3, True, 1, {(6,3)})
    s4 = (7, 1, True, 1, {(7,1)})
    f = [b1, c1, c2, d1, d2, d3, s1, s2, s3, s4]
    assert are_unsunk_ships_left(f) == False
