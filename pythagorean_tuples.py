from itertools import product, count
from math import log, isqrt, ceil, prod
from collections import Counter


def pythagorean_triples(a: int, primitive=False) -> set:
    """
    Return all pythagorean triples consisting 'a' as a leg (cathetus) of right triangle.

    This function is an implementation of Tanay Roy and Farjana Jaishmin Sonia's paper "A Direct Method To Generate
    Pythagorean Triples And Its Generalization To Pythagorean Quadruples And n-tuples".

    :param a: positive integer number
    :param primitive: True if triples should be primitive, False otherwise
    :return: set of all [primitive] pythagorean triples consisting a
    """

    if type(a) is not int:
        raise TypeError("a must be an integer")
    if a < 1:
        raise ValueError("a must be positive")
    if a in {1, 2}:
        return set()

    factors = Counter(_prime_factors(a))

    # Categorising process
    if 2 not in factors:
        return _pythagorean_triples_BP(a, factors) if primitive else _pythagorean_triples_B(a, factors)
    elif len(factors) == 1:
        return _pythagorean_triples_AP(a) if primitive else _pythagorean_triples_A(a, factors)
    else:
        return _pythagorean_triples_CP(a, factors) if primitive else _pythagorean_triples_C(a, factors)


def _TRIPLE(a: int, delta: int):
    b = (a ** 2 - delta ** 2) // (2 * delta)
    return a, b, b + delta


def _prime_factors(n: int) -> list:
    """
    Return ordered list of all prime factors of n.

    :param n: (int) natural number greater than 1
    :return: (list) ordered list of all prime factors of n
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in count(3, 2):
        if i ** 2 > n:
            break

        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors


def _pythagorean_triples_AP(a: int):
    return {_TRIPLE(a, 2)}


def _pythagorean_triples_A(a: int, factors: Counter):
    triples = set()
    m = factors[2]
    for r in range(1, m):
        d = 2 ** r
        triples.add(_TRIPLE(a, d))
    return triples


def _pythagorean_triples_BP(a: int, factors: Counter):
    triples = set()
    triples.add(_TRIPLE(a, 1))
    for p in factors:
        d = p ** (2 * factors[p])
        if a > d:
            triples.add(_TRIPLE(a, d))
    return triples


def _pythagorean_triples_B(a: int, factors: Counter):
    # TODO: minimise the number of possible deltas (without `itertools.product()`)
    triples = set()
    factors_list = list(factors)
    ranges = [range(0, min(ceil(log(a, factor)), 2 * factors[factor] + 1)) for factor in factors_list]
    for powers in product(*ranges):
        if (d := prod(factors_list[i] ** power for i, power in enumerate(powers))) < a:
            triples.add(_TRIPLE(a, d))
    return triples


def _pythagorean_triples_CP(a: int, factors: Counter):
    triples = set()
    m = factors[2]
    del factors[2]
    for p in factors:
        s = factors[p]
        for t in 0, 2 * s:
            for r in 1, 2 * m - 1:
                if a > (d := 2 ** r * p ** t) and r != m:
                    triples.add(_TRIPLE(a, d))
    return triples


def _pythagorean_triples_C(a: int, factors: Counter):
    # TODO: minimise the number of possibilities (without `itertools.product()`)
    triples = set()
    factors_list = list(factors)
    ranges = [range(0, min(ceil(log(a, factor)), 2 * factors[factor] + 1)) for factor in factors_list]
    ranges[0] = range(1, min(ceil(log(a, 2)), 2 * factors[2]))    # concerns the factor 2
    for powers in product(*ranges):
        if (d := prod(factors_list[i] ** power for i, power in enumerate(powers))) < a:
            triples.add(_TRIPLE(a, d))
    return triples
