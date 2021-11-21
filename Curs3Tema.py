import funcMod

# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care
# reprezintă numere întregi sau reale.

def your_function(*args, **kwargs):
    s = 0
    for arg in args:
        if isinstance(arg, int):
            s += arg
    return s


a = your_function(1, 5, -3, "abc", [12, 56, "cad"])
print(a)

a = your_function()
print(a)

a = your_function(2, 4, "abc", param_1=2)
print(a)


# Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel
# returnează valoarea 0.

def get_intreg(*args):
    print("Dati un numar: ")
    numarul = input()
    try:
        int(numarul)
        print("Numarul intreg", numarul)
    except ValueError:
        print("0")


get_intreg()

# Să se scrie un modul care contine 3 funcții recursive care primesc ca parametru un număr întreg și returnează:
# ○ suma tuturor numerelor de la [0, n]
# ○ suma numerelor pare de la [0, n]
# ○ suma numerelor impare de la [0. n]

print("Suma nr",funcMod.get_suma(4))
print("Suma nr pare",funcMod.get_par(4))
print("Suma nr impare",funcMod.get_impar(4))