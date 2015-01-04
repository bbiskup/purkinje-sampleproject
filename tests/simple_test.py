import pytest
import random

rand_sep = random.randint(0, 10)


def test_1():
    assert True


def test_2():
    assert False


# @pytest.mark.parametrize('arg', range(5000))
# def test_3(arg):
#     assert arg % 2 == 0

@pytest.mark.parametrize('arg', range(500))
def test_3(arg):
    assert random.randint(0, 10) > rand_sep
