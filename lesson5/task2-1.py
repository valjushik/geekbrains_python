import random

def play_game(n, m, players):
    count = 0
    while n > 0:
        move = int(input(f"Ходит {players[count % 2]}. Введите количество конфет: "))
        while move > n or move > m:
            move = int(input(f"Это слишком много конфет, можно взять не более {m}, осталось конфет: {n} \nХодит {players[count % 2]}. Введите количество конфет: "))
        n = n - move
        if n > 0:
            print(f"Осталось конфет: {n}")
        else:
            print("Все конфеты разобраны.")
        count += 1
    return players[not count % 2]


print("Игра в конфеты на столе\n")

player1 = "ПЕРВЫЙ игрок"
player2 = "ВТОРОЙ игрок"
players = [player1, player2]

n = int(input("Введите количество конфет: "))
m = int(input("Сколько можно брать конфет за ход?: "))

winer = play_game(n, m, players)
if not winer:
    print("Ничья")
else:
    print(f"Победил {winer}!")

