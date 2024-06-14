# Aucun n'import ne doit être fait dans ce fichier


def nombre_entier(n: int) -> str:
    debut = "S" * n 
    fin = debut + "0"
    return fin


def S(n: str) -> str:
    if n=="0":
        return "S0"
    else:
        result = n[:-1]
        result += "S0"
    return result


def addition(a: str, b: str) -> str:
    count = len(a) - 1
    count2 = len(b) - 1

    return ("S" * (count + count2)) + "0" 
            


def multiplication(a: str, b: str) -> str:
    count = len(a) - 1
    count2 = len(b) - 1

    return ("S" * (count * count2)) + "0"


def facto_ite(n: int) -> int:
    if n==1 or n==0:
        return 1
    else:
        fact=1
        for i in range(1,n+1):
            fact *= i
    return fact


def facto_rec(n: int) -> int:
    if (n <= 1):
            return 1
    return n * facto_rec(n-1)


def fibo_rec(n: int) -> int:
    if (n < 1):
        return 0
    if (n < 2):
        return 1
    return fibo_rec(n-1) + fibo_rec(n-2)

def fibo_ite(n: int) -> int:
    if (n < 1):
        return 0
    if (n < 2):
        return 1
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return a


def golden_phi(n: int) -> int:
    phi = (1 + 5 ** 0.5) / 2
    return int(phi ** n)


def sqrt5(n: int) -> int:
    sqrt_5 = 5 ** 0.5
    return int(sqrt_5 ** n)


def pow(a: float, n: int) -> float:
    return a ** n
