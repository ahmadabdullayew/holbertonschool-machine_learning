#!/usr/bin/env python3
"""
Module that calculates the integral of a polynomial
"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial

    Args:
        poly (list): list of coefficients
        C (int): integration constant

    Returns:
        list: coefficients of the integral polynomial
    """
    if not isinstance(poly, list) or not isinstance(C, int):
        return None

    if len(poly) == 0:
        return None

    result = [C]

    for i in range(len(poly)):
        coef = poly[i]
        if not isinstance(coef, (int, float)):
            return None
        result.append(coef / (i + 1))

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result

