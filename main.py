def print_board():
  #Initiation of section a, c and d 
  section_a = "+---+---+---+---+---+---+---+"
  
  section_d = "+---+---+---+---+---+---+---+"
  
  # Print the first line of numbers
  print("  1   2   3   4   5   6   7  ")
  for row in range(6):
    print(section_a)
    #resets section_b to an empty string for each row
    section_b = ""
    for col in range(7):
      section_b += ("| " + str(board[row][col]) + " ")
     
    # Prints row B the last line on the right of each B row
    print(section_b + "|")
   
  #After the loops iterate, print the final section d once to close the board off
  print(section_d)



def left(array, row, col, x_or_o):
  counter = 0
  while col >= 0:
    if array[row][col] == x_or_o:
      counter+=1
    if array[row][col] != x_or_o:
      break
    col-=1
  #print("left counter" + str(counter))
  return counter  



def right(array, row, col, x_or_o):
  counter = 0
  while col < 6:
    if array[row][col] == x_or_o:
      counter+=1
    if array[row][col] != x_or_o:
      break
    col+=1
  #print("right counter" + str(counter))
  return counter-1  



def up(array, row, col, x_or_o):
  counter = 0
  while row >= 0:
    if array[row][col] == x_or_o:
      counter+=1
    if array[row][col] != x_or_o:
      break
    row-=1
 
  return counter  



def down(array, row, col, x_or_o):
  counter = 0
  while row <= 5:
    if array[row][col] == x_or_o:
      counter+=1
    if array[row][col] != x_or_o:
      break
    row+=1

  return counter 



def top_left(array, row, col, x_or_o):
  counter = 0
  while row >= 0 and col >= 0:
    if array[row][col] == x_or_o:
      counter+=1
    if array[row][col] != x_or_o:
      break
    row-=1
    col-=1
 
  return counter  



def top_right(array, row, col, x_or_o):
  counter = 0
  while row >= 0 and col <= 6:
    if array[row][col] == x_or_o:
      counter+=1
    if array[row][col] != x_or_o:
      break
    row-=1
    col+=1
 
  return counter  


  
def win(array, x_or_o):
  # Initiate the win state as false to begin
  win = False

  # Traverses through the board array and looks for X or O depending on its argument then initiates a score keeping counter to 1
  for row in range(5, -1, -1):
    for col in range(0,7,1):
      
      if array[row][col] == x_or_o:
        counter =1
        
        if counter - 1  + left(array, row, col, x_or_o) >= 4:
          win = True

        if counter - 1 + up(array, row, col, x_or_o)  >= 4:
          win = True

        if counter - 1 + top_left(array, row, col, x_or_o) >= 4 or counter - 1 + top_right(array, row, col, x_or_o) >= 4:
          win = True

  return win            



# Make an empty 6 by 7 list that acts as a base for the board

#main code

#Initiation of board 
board = [
[' ', ' ',' ', ' ', ' ', ' ', ' '], 
[' ', ' ',' ', ' ', ' ', ' ', ' '], 
[' ', ' ',' ', ' ', ' ', ' ', ' '], 
[' ', ' ',' ', ' ', ' ', ' ', ' '], 
[' ', ' ',' ', ' ', ' ', ' ', ' '], 
[' ', ' ',' ', ' ', ' ', ' ', ' '], 
[' ', ' ',' ', ' ', ' ', ' ', ' ']]

#Initiates the round counter to 1
counter = 1
game_won = False
welcome_message = """Welcome to Helen's custom made connect 4 game! 

Connect 4 in a row before your opponent to win the game!

"""
# Starts the game off by printing a welcome message and the board by calling the print board function
print(welcome_message)
print_board()

# Continues iterating through the game until there is a winner or the entire board is filled after 42 turns
while(not game_won and counter <= 42):
  # Alternates between player O and player X's turns depending on the turn number
  if counter % 2 == 1:
    turn = 'O'
  else:
    turn = 'X'
  
  #scan col input from user
  user_input = input("Enter a column number: ")

  # Finds the index that corresponds to the input
  col = int(user_input) - 1

  for row in range(5,-1,-1):
    if board[row][col] == ' ':
      board[row][col] = turn
      break
  
  
  #Prints the board so the user can see what they inputted
  print_board()
  
  # Check for a winner
  game_won = win(board, turn)
  
  # If no winner, at the end of each turn, inrease the counter by one 
  counter+=1

print("Game over! Player " + turn + " is the winner!")