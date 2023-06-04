# def tic_tac_toe(inputs):
#     players = {
#         'X': 'Player 1',
#         'O': 'Player 2'
#     }
#     for i in range(3):
#         if inputs[i][0] == inputs[i][1] and inputs[i][1] == inputs[i][2]:
#             # return f'{players[inputs[i][0]]} wins'
#             return '{player} wins'.format(player = players[inputs[i][0]])

#         if inputs[0][i] == inputs[1][i] and inputs[1][i] == inputs[2][i]:
#             # return f'{players[inputs[0][i]]} wins'
#             return '{player} wins'.format(player = players[inputs[0][i]])

#     if inputs[0][0] == inputs[1][1] and inputs[1][1] == inputs[2][2] or inputs[2][0] == inputs[1][1] and inputs[1][1] == inputs[0][2]: 
#         # return f'{players[inputs[1][1]]} wins'
#         return '{player} wins'.format(player = players[inputs[1][1]])

#     return 'It\'s a Tie'

def tic_tac_toe(board):
	cols = list(map(list, zip(*board)))
	diag1 = [[board[i][i] for i in range(3)]]
	diag2 = [[board[i][-i-1] for i in range(3)]]
	
	combs = board + cols + diag1 + diag2
	if ['X', 'X', 'X'] in combs:
		return 'Player 1 wins'
	elif ['O', 'O', 'O'] in combs:
		return 'Player 2 wins'
	else:
		return "It's a Tie"
	
print(tic_tac_toe([
  ["X", "O", "O"],
  ["O", "X", "O"],
  ["O", "#", "X"]
])) 


print(tic_tac_toe([
  ["X", "O", "O"],
  ["O", "X", "O"],
  ["X", "#", "O"]
])) 


print(tic_tac_toe([
  ["X", "X", "O"],
  ["O", "X", "O"],
  ["X", "O", "#"]
])) 