from itertools import count


def get_prime(seq=None):
    if seq:
        sequence = seq
    else:
        sequence = count(2)

    domain = {}

    for number in sequence:
        factor = domain.pop(number, None)

        if not factor:
            yield number

            domain[number**2] = number
        else:
            composite = factor + number
            while composite in domain:
                composite += factor

            domain[composite] = factor
