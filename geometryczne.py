def wzor_rek(n, q):
    an = n * q
    return an


def ogolny(a1, n, q):
    an = a1 * pow(q,(n-1))
    return an


def srodkowy(a1, a2):
    an = pow(a1 * a2,(1/2))
    return an


def suma(a1, n, q):
    if q != 1:
        sn = (a1 * (1-pow(q,n)))/(1-q)
    else:
        sn = n * a1
    return sn



