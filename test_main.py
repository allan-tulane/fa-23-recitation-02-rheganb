from main import *


def test_simple_work():
  """ done. """
  assert simple_work_calc(10, 2, 2) == 56  #TODO
  assert simple_work_calc(20, 3, 2) == 506.75 #TODO
  assert simple_work_calc(30, 4, 2) == 1954 #TODO
  assert simple_work_calc(8, 2, 2) == 32
  assert simple_work_calc(10, 3 , 2) == 162.25
  assert simple_work_calc(20, 2, 2) == 132


def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(10, 3, 2,lambda n: 1) == 40
  assert work_calc(20, 2, 2, lambda n: n*n) == 748
  assert work_calc(20, 3, 2, lambda n: n) == 230
