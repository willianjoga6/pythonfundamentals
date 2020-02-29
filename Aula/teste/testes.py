from unittest import TestCase, main

def validar_par(num: int) -> bool:
    if isinstance(num,int):
        return True if num % 2 == 0 else False
    elif isisnstance(num, str):
        if num.isnumeric():
            return True if int(num) % 2 == 0 else False
        else:
            return None




# def somar(x, y):
#     return x + y

# def subtrair(x, y):
#     return x - y

# class Teste(TestCase):
#     def test_soma(self):
#         self.assertEqual(somar(5,5),10)
#         self.assertLess(somar(5,5),11)

#     def test_sub(self):
#         self.assertEqual(subtrair(5,5),0)
#         self.assertLessEqual(subtrair(15,5),10)

    

if __name__ == "__main__":
    main()



















# def multiplicar(x, y):
#     return x * y

# def divir(x, y):
#     return x / y


# assert somar(2, 2) == 4, "Obtido: {}, Esperado: 4. format(somar(2,2))"
# assert somar(3, 3) == 6, "Obtido: {}, Esperado: 6. format(somar(3,3))"

# assert subtrair(2,2) == 0, "Obtido: {}, Esperado: 0. format(subtrair(2,2))"
# assert subtrair(5,3) == 2, "Obtido: {}, Esperado: 2. format(subtrair(5,3))"

# assert multiplicar(10,2) == 20, "Obtido: {}, Esperado: 20. format(multiplicar(10,2))"
# assert multiplicar(1,3) == 3, "Obtido: {}, Esperado: 3. format(multiplicar(1,3))"

# assert divir(4,2) == 2, "Obtido: {}, Esperado: 2. format(divir(4,2))"
# assert divir(10,3) == 3, "Obtido: {}, Esperado: 3. format(divir(9,3))"