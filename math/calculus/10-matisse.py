#!/usr/bin/env python3
"""
Module that computes the derivative of a polynomial.
"""


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.

    Args:
        poly (list): list of coefficients

    Returns:
        list: derivative of the polynomial
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    for coef in poly:
        if not isinstance(coef, (int, float)):
            return None

    # Derivative of a constant polynomial
    if len(poly) == 1:
        return [0]

    derivative = []
    for power in range(1, len(poly)):
        derivative.append(poly[power] * power)

    # If derivative is all zeros
    if all(coef == 0 for coef in derivative):
        return [0]

    return derivative

