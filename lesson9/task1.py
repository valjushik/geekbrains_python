import emoji

print("🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾🖐🏾")

print(emoji.emojize("    :anger_symbol::anger_symbol::anger_symbol:"), "Игра Крестики-нолики", emoji.emojize(":anger_symbol::anger_symbol::anger_symbol:"), "\nЧтобы сделать ход выберите номер ячейки \n")

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("\nХод " + player_token+": ")
      try:
         player_answer = int(player_answer)
      except:
         print("\nНекорректный ввод. Ведите число.")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("\nЭта клетка уже занята")
      else:
        print("\nНекорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0

    while True:
        draw_board(board)
        if counter % 2 == 0:
           take_input(emoji.emojize(":cross_mark:"))
        else:
           take_input(emoji.emojize(":hollow_red_circle:"))
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print("\n", emoji.emojize(":1st_place_medal:"), tmp, "выиграл!")

              break
        if counter == 9:
            print("\n", emoji.emojize(":handshake:"), "Ничья")
            break
    draw_board(board)
main(board)
