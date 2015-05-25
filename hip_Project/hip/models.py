from django.db import models
from itertools import combinations
import math
import copy
import sys

class board(models.Model):
	img1 = models.IntegerField(max_length=1, default="0")
	img2 = models.IntegerField(max_length=1, default="0")
	img3 = models.IntegerField(max_length=1, default="0")
	img4 = models.IntegerField(max_length=1, default="0")
	img5 = models.IntegerField(max_length=1, default="0")
	img6 = models.IntegerField(max_length=1, default="0")
	img7 = models.IntegerField(max_length=1, default="0")
	img8 = models.IntegerField(max_length=1, default="0")
	img9 = models.IntegerField(max_length=1, default="0")	

	player = models.CharField(max_length=128, default="none")

	game_over = models.IntegerField(max_length=1, default="0")

	def __unicode__(self):
		return self.player

	def root_Board(self):

		data = []
		board = [] 

		data.append(str(self.img1))
		data.append(str(self.img2))
		data.append(str(self.img3))
		board.append(data)
		data = []
		data.append(str(self.img4))
		data.append(str(self.img5))
		data.append(str(self.img6))
		board.append(data)
		data = []
		data.append(str(self.img7))
		data.append(str(self.img8))
		data.append(str(self.img9))
		board.append(data)

		print board

		self.AlphaBetaMinimax(board)

	def AlphaBetaMinimax(self, board):
		print "Inside Minimax!-----"
		player = False
		free_positions = self.populate_positions(board, '0')
		
		if(self.game_over == 0 and len(free_positions) != 0):
			
			print "\n\nComputer's turn"
			board = self.firstBestMove(board, 0)

			self.img1 = int(board[0][0])
			self.img2 = int(board[0][1])
			self.img3 = int(board[0][2])
			self.img4 = int(board[1][0])
			self.img5 = int(board[1][1])
			self.img6 = int(board[1][2])
			self.img7 = int(board[2][0])
			self.img8 = int(board[2][1])
			self.img9 = int(board[2][2])

			self.player = "Human"
			self.save()

			print "\nUpdated board", board

			player = True

			free_positions = self.populate_positions(board, '0')
			result = self.evaluate_game(board)
			if(result == 1):
				print "\nYou lose!"
				self.game_over = 1
			elif(result == 2):
				print "\nYou won!"
				self.game_over = 2

	def populate_positions(self, board, player):
		""" 
			Populate the player positions on the board
		"""
		print "Inside populate_positions!-----"
		positions = []
		for i in range(0,3):
			for j in range(0,3):
				if(board[i][j] == player):
					positions.append([i,j])
		return positions

	def check_square(self, player_positions):
		"""
			Function returns a true or false depending on whether a square exists or not
		"""
		print "Inside check square!-----"
		length = len(player_positions)
		sides = []

		for item in combinations(player_positions,4):
			"""
				populating the sides using three points of the combination
			"""
			sides = []
			sides.append(self.distance(item[0],item[1]));
			sides.append(self.distance(item[0],item[2]));
			sides.append(self.distance(item[0],item[3]));
			result = self.isSquare(sides,item)
			if(result == True):
				return result
		return False

	def isSquare(self, sides, player_positions):

		"""
			function to check the presence of square using the 4 points given
		"""
		print "Inside isSquare!-----"
		equalSide1 = -1
		equalSide2 = -1
		unequalSide = -1
		if(sides[0] == sides[1]):
			if(sides[0] != sides[2]):
				equalSide1 = 0
				equalSide2 = 1
				unequalSide = 2
		elif(sides[1] == sides[2]):
			if(sides[1] != sides[0]):
				equalSide1 = 1
				equalSide2 = 2
				unequalSide = 0        
		elif(sides[0] == sides[2]):
			if(sides[0] != sides[1]):
				equalSide1 = 0
				equalSide2 = 2
				unequalSide = 1

		"""
			If failed to satisfy the above condition, the points doesn't form a square
    		Otherwise check for the square distance conditions
    	"""
		if(equalSide1 != -1):
			opposing = 0
			if(unequalSide == 0):
				opposing = self.distance(player_positions[2], player_positions[3]);
			elif(unequalSide == 1):
				opposing = self.distance(player_positions[1], player_positions[3]);
			elif(unequalSide == 2):
				opposing = self.distance(player_positions[1], player_positions[2]);

			if(opposing == sides[unequalSide]):
				diagonal = opposing
				adjacent = sides[equalSide1]
				is_Square = True
				for a in range(0,4):
					diagonalCount = 0
					adjacentCount = 0 
					for b in range(0,4):
						if(a != b):
							distance1 = self.distance(player_positions[a], player_positions[b]);
							if(distance1 == diagonal):
								diagonalCount += 1
							elif(distance1 == adjacent):
								adjacentCount += 1
	
					if((diagonalCount == 1 and adjacentCount == 2) != True): #If there is one diagonal and two adjacents
						is_Square = False
						break;
				if(is_Square == True): #There is a square
					return True
		return False

	def distance(self, point1, point2):
		"""
			Function to find the distance between any two tokens on the baord
		"""

		print "Inside Distance!-----"
		dist = math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2);
		return dist


	"""
		Functions for the Implementation of Minimax Algorithm
	"""
	

	def firstBestMove(self, board, depth):

		print "Inside firstbest move!-----"

		free_positions = self.populate_positions(board, '0')
		previous = -sys.maxint - 1
		depth += 1

		for position in free_positions:
			child = copy.deepcopy(board)
			child[int(position[0])][int(position[1])] = '2'
			current = self.min(child, depth, -sys.maxint - 1, sys.maxint)
			if(current > previous):
				bestChild = child
				previous = current
		return bestChild

	def max(self, board, depth, alpha, beta):

		print "Inside max!-----"

		free_positions = self.populate_positions(board, '0')
		result = self.evaluate_game(board)

		if(result == 1):
			return 10000-depth
		elif(result == 2):
			return depth-10000
		elif(result == 0 and len(free_positions) == 0):
			return 0

		depth += 1
		for position in free_positions:
			new_board = copy.deepcopy(board)
			new_board[int(position[0])][int(position[1])] = '2'
			move = self.min(new_board, depth, alpha, beta)
			if(move > alpha): #Find max and store in alpha
				alpha = move
			if(alpha >= beta): #Beta cut-off
				break
		return alpha

	def min(self, board, depth, alpha, beta):

		print "Inside Min!-----"

		free_positions = self.populate_positions(board, '0')
		result = self.evaluate_game(board)

		if(result == 1):
			return 10000-depth
		elif(result == 2):
			return depth-10000
		elif(result == 0 and len(free_positions) == 0):
			return 0

		depth += 1
		for position in free_positions:
			new_board = copy.deepcopy(board)
			new_board[int(position[0])][int(position[1])] = '1'
			move = self.max(new_board, depth, alpha, beta)
			if(move < beta): #Find min and store in beta
				beta = move
			if(alpha >= beta): #alpha cut-off
				break
		return beta

	def evaluate_game(self, board):
		print "Inside evaluate board!-----"
		player_positions = self.populate_positions(board, '1')
		player_result = self.check_square(player_positions)
		computer_positions = self.populate_positions(board, '2')
		computer_result = self.check_square(computer_positions)
		if(player_result == True):
			return 1
		elif(computer_result == True):
			return 2
		else:
			return 0


