#Digite o numero para identificar se é positivo ou negativo
N = int(input())
for i in range(N):
    x = int(input())
    if x == 0:
        print("NULL")
    elif x > 0:
        if x % 2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif x < 0:
        if x % 2 == 0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
