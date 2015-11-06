#!/usr/bin/env python

from franges import drange


def test_basic_usage():
    expected = [0, 0.1, 0.2, 0.3]
    assert(expected == list(drange(0, 0.4, 0.1, 6)))
    expected = [0, 0.5, 1.0, 1.5]
    assert(expected == list(drange(0, 2, 0.5, 2)))


def test_partial_args():
    expected = list(range(10))
    assert(expected == list(drange(10)))
