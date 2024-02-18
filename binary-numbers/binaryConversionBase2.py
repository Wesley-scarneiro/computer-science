
"""
    Versão iterativa
    'Number' deve ser um número inteiro positivo
    O resultado é uma string representando o número na base 2 com 
    a menor quantidade de bits necessários para representá-lo
"""
def binaryConversionV1(number):
    if number < 0:
        raise ValueError("Number cannot be negative")
    result = ""
    while True:
        result = f"{number % 2}{result}"
        number = number // 2
        if number == 0:
            break
    return result

"""
    Versão recursiva de binaryConversionV1
"""
def binaryConversionV2(number):
     if number < 0:
        raise ValueError("Number cannot be negative")
     return binaryConversionRecursive(number)
     
def binaryConversionRecursive(number, result=""):
    result = f"{number % 2}{result}"
    number = number // 2
    if number != 0:
        return binaryConversionRecursive(number, result)
    return result

def safely(function, number):
    try:
        function(number)
    except Exception as ex:
        print(f"Exception: {ex}")

def main():
    print("\tbinaryConversionV1")
    print(f"-1      --> {safely(binaryConversionV1, -1)}")
    print(f"0       --> {binaryConversionV1(0)}")
    print(f"1       --> {binaryConversionV1(1)}")
    print(f"10      --> {binaryConversionV1(10)}")
    print(f"100     --> {binaryConversionV1(100)}")
    print(f"1000    --> {binaryConversionV1(1000)}")

    print("\n\tbinaryConversionV2")
    print(f"-1      --> {safely(binaryConversionV2, -1)}")
    print(f"0       --> {binaryConversionV2(0)}")
    print(f"1       --> {binaryConversionV2(1)}")
    print(f"10      --> {binaryConversionV2(10)}")
    print(f"100     --> {binaryConversionV2(100)}")
    print(f"1000    --> {binaryConversionV2(1000)}")

if __name__ == "__main__":
    main()

"""
 binaryConversionV1
Exception: Number cannot be negative
-1      --> None
0       --> 0
1       --> 1
10      --> 1010
100     --> 1100100
1000    --> 1111101000

        binaryConversionV2
Exception: Number cannot be negative
-1      --> None
0       --> 0
1       --> 1
10      --> 1010
100     --> 1100100
1000    --> 1111101000
"""