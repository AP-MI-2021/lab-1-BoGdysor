'''
Returneaza true daca n este prim si false daca nu.
'''


def is_prime(n):
    d = 0
    for i in range(1, n + 1):
        if n % i == 0:
            d += 1
    if d == 2:
        return True
    return False


"""
Returneaza produsul numerelor din lista lst.
"""


def get_product(lst):
    product = 1
    list_lenght = len(lst)
    for i in range(list_lenght):
        product = product * lst[i]
    return product


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''


def get_cmmdc_v1(x, y):
    while x != y:
        if x > y:
            x = x - y
        elif y > x:
            y = y - x
    return x


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''


def get_cmmdc_v2(x, y):
    while y:
        r = x % y
        x = y
        y = r
    return x


def main():
    while True:
        print("\nAlegeti o optiunde din urmatoarele:")
        print("1.Verificati daca numarul este prim.")
        print("2.Calculeaza produsul a n numere naturale.")
        print("3.Calculeaza CMMDC a 2 numere naturale utilizand prima metoda.")
        print("4.Calculeaza CMMDC a 2 numere naturale utilizand a doua metoda.")
        print("5.Iesire din program.\n")
        option = int(input("Alegeti o optiunde din urmatoarele:"))
        if option == 1:
            number = int(input("\nIntroduceti numarul: "))
            if is_prime(number):
                print("\nNumarul {} este prim".format(number))
            else:
                print("\nNumarul {} nu este prim".format(number))
        elif option == 2:
            n = int(input("\nIntroduceti numarul de elemente: "))

            numbers_str = input("\nIntoduceti numerele: ")
            numbers_str = numbers_str.split(' ')
            list_of_numbers = []
            for nr_str in numbers_str:
                list_of_numbers.append(int(nr_str))
            if len(list_of_numbers) > n:
                print("\nAti depasit limita introdusa de numere")
            elif len(list_of_numbers) < n:
                print("\nNu ati introdus destule numere")
            else:
                product = get_product(list_of_numbers)
                print(f"Produsul numerelor introduse este {product}")
        elif option == 3:
            number_1 = int(input("Introduceti primul numar: "))
            number_2 = int(input("Introduceti al doilea numar: "))
            cmmdc = get_cmmdc_v1(number_1, number_2)
            print(f"\nCMMDC  lui {number_1} si {number_2} este {cmmdc}")
        elif option == 4:
            number_1 = int(input("Introduceti primul numar: "))
            number_2 = int(input("Introduceti al doilea numar: "))
            cmmdc = get_cmmdc_v2(number_1, number_2)
            print(f"\nCMMDC al lui {number_1} si {number_2} este {cmmdc}")
        elif option == 5:
            break
        else:
            print("Optiune invalida")


if __name__ == '__main__':
    main()
