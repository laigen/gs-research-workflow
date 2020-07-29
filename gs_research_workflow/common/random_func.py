# -*- coding: utf-8 -*-

"""提供带分布的 random funcion"""
from random import gauss


def random_gauss(min_v: float, max_v: float, mu:float, sigma: float = 1.) -> float:
    v = gauss(mu, sigma)
    if v < min_v:
        return min_v
    if v > max_v:
        return max_v
    return v
