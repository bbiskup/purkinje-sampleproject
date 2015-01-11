import pytest
import random
import time

rand_sep = 8


def test_1():
    assert True


def test_2():
    assert False


@pytest.mark.skipif('True')
def test_3():
    assert False


# @pytest.mark.parametrize('arg', range(5000))
# def test_3(arg):
#     assert arg % 2 == 0

# @pytest.mark.parametrize('arg', range(3))
# def test_3(arg):
#     time.sleep(0)
#     assert random.randint(0, 10) > rand_sep


# @pytest.mark.slow
# def test_4():
#     time.sleep(5)
#     assert True


@pytest.mark.slow
@pytest.mark.parametrize('arg', range(30))
def test_5(arg):
    time.sleep(random.random())
    assert random.randint(0, 10) < rand_sep
