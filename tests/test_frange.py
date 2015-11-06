#!/usr/bin/env python

from franges import frange


def test_basic_usage():
    expected = [0, 0.5]
    assert(expected == list(frange(0, 1, 0.5)))
    expected = [0, 0.5, 1]
    assert(expected == list(frange(0, 1.5, 0.5)))


def test_partial_args():
    expected = list(range(10))
    assert(expected == list(frange(10)))
