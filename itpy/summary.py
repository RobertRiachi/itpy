# -*- coding: utf-8 -*-

"""
itpy.summary
~~~~~~~~~~~~

This module contains functions that compute summaries over the iterable.

"""
from __future__ import division
from collections import Counter
from functools import reduce as rd


def for_each(iterable, function):
    """
    Evaluate the function for every value of the iterable. This is used inplace of map when we do not care about keeping
    the results. Unlike transform.intercept, this returns nothing.

    :param iterable:
    :param function:
    """
    for item in iterable:
        function(item)
    return None


def size(iterable):
    """
    Obtain the size of the iterable

    :param iterable:
    """
    counter = 0
    for i in iterable:
        counter += 1
    return counter


# noinspection PyShadowingBuiltins
def reduce(iterable, reducer):
    """
    Get a merged value using an associative reduce function,
    so as to reduce the iterable to a single value from left to right.

    :param iterable:
    :param reducer:
    """

    value = rd(reducer, iterable)

    return value


def frequency(iterable):
    """
    Obtain the frequency of every item in the iterable.
    It is important to note that it is currently implemented as a counter
    so we must assume this counter fits into memory.

    :rtype : Counter
    :param iterable:
    """

    freq = Counter()
    freq.update(iterable)

    return freq


def mean(iterable):
    """
    Computes the mean with a single pass of the iterable.

    :param iterable:
    """
    size_accumilator = 0
    sum_of_values = 0

    for x in iterable:
        sum_of_values += x
        size_accumilator += 1

    # Practice safe division.
    if size_accumilator < 2:
        return 0

    ret_result = sum_of_values / size_accumilator
    return ret_result


def twopass_variance(iterable):
    """
    Computes the variance with two passes of the iterable,
    once to calculate the mean, next to calculate the sum of squares.

    :param iterable:
    """
    size_accumilator = 0
    sum_of_squares = 0

    mean_result = mean(iterable)

    for x in iterable:
        size_accumilator += 1
        difference = (x - mean_result)
        sum_of_squares += difference * difference

    # Practice safe division.
    if (size_accumilator < 2):
        return 0

    ret_result = sum_of_squares / (size_accumilator - 1)
    return ret_result


def online_variance(iterable):
    """
    Computes the variance with one pass of the iterable.
    This method allows for partial answers up to the procced value.

    Note, unless your are are certain that your data is shuffled,
    you will not get meaningful partial results.

    :param iterable:
    """
    size_accumilator = 0
    current_mean = 0
    m2 = 0

    try:
        for x in iterable:
            size_accumilator += 1
            difference = x - current_mean
            current_mean += difference / size_accumilator
            m2 += difference * (x - current_mean)
    except KeyboardInterrupt:
        pass

    # Practice safe division.
    if (size_accumilator < 2):
        return 0

    variance = m2 / (size_accumilator - 1)
    return variance
