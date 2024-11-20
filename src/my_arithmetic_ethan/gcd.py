def gcd(a, b):
    """
    Calcule le plus grand commun diviseur (PGCD) de deux entiers a et b.
    Utilise l'algorithme d'Euclide.
    """
    while b:
        a, b = b, a % b
    return abs(a)
