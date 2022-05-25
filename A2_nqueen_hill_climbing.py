# -*- coding: utf-8 -*-
"""TI47_NQueen-hill-climbing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gWSjxO-EOsY6beLE5oNM6zVBc0duWLKR
"""

import random
from pprint import pprint

def input_size_board():
	n = input("Enter the size of the board : ")
	return int(n)

def print_board(board, n):
	print('Board:')
	for i in range(len(board)):
		print(str(board[i]) + ' ', end='')
		if (i + 1) % n == 0:
			print()
	print('H value: ', determine_h_cost(board, n))
	print('---------------------')


def generate_random_board(n):
	generated_board = []
	for i in range(n):
		j = random.randint(0, n-1)
		row = [0]*n
		row[j] = 1
		generated_board.extend(row)
	return generated_board


def find_collisions(board, n):
	collisions = 0
	occurences = []
	max_index = len(board)
	for i in range(max_index):
		if board[i] == 1:
			for x in range(1, n):
				# top
				if (i - n*x >= 0):
					north = i - n*x
					# north
					if (board[north] == 1):
						collisions += 1
						occurences.append('north: '+str(i)+' and '+str(north))
					# northwest
					if (int((north - x)/n) == int(north/n)) and (north - x) >= 0:
						northwest = north - x
						if (board[northwest] == 1):
							collisions += 1
							occurences.append('northwest: '+str(i)+' and '+str(northwest))
					# northeast
					if (int((north + x)/n) == int(north/n)):
						northeast = north + x
						if (board[northeast] == 1):
							collisions += 1
							occurences.append('northeast: '+str(i)+' and '+str(northeast))
       
				if (i + n*x < max_index):
					south = i + n*x
					# south
					if (board[south] == 1):
						collisions += 1
						occurences.append('south: '+str(i)+' and '+str(south))
					# southwest
					if (int((south - x)/n) == int(south/n)):
						southwest = south - x
						if (board[southwest] == 1):
							collisions += 1
							occurences.append('southwest: '+str(i)+' and '+str(southwest))
					# southeast
					if (int((south + x)/n) == int(south/n)) and ((south + x) < max_index):
						southeast = south + x
						if (board[southeast] == 1):
							collisions += 1
							occurences.append('southeast: '+str(i)+' and '+str(southeast))
				# west 
				if (int((i - x)/n) == int(i/n)) and (i - x >= 0):
					west = i - x
					if (board[west] == 1):
						collisions += 1
						occurences.append('west: '+str(i)+' and '+str(west))
				# east
				if (int((i + x)/n) == int(i/n)) and (i + x < max_index):
					east = i + x
					if (board[east] == 1):
						collisions += 1
						occurences.append('east: '+str(i)+' and '+str(east))
	return [collisions, occurences]

def determine_h_cost(board, n, verbose=False):
	collisions, occurences = find_collisions(board, n)
	if verbose:
		pprint(occurences)
	return int(collisions/2)
 
def find_child(board, n, sideways_move=False):
	count = 0
	child = []
	current_h_cost = determine_h_cost(board, n)
	same_cost_children = []

	for row in range(n):
		for col in range(n):
			temp_board = []
			temp_board.extend(board[:row*n])
			new_row = [0]*n
			new_row[col] = 1
			temp_board.extend(new_row)
			temp_board.extend(board[(row+1)*n:])
			temp_h_cost = determine_h_cost(temp_board, n)
	 
			if (sideways_move):
				if (temp_board != board):
					if (temp_h_cost < current_h_cost):
						child = temp_board.copy()
						current_h_cost = temp_h_cost
					elif (temp_h_cost == current_h_cost):
						same_cost_children.append(temp_board)
						x = random.randint(0, len(same_cost_children)-1)
						child = same_cost_children[x]
			else:
				if (temp_board != board) and (temp_h_cost < current_h_cost):
					child = temp_board.copy()
					current_h_cost = temp_h_cost
	return child


def hill_climbing(board, n, max_iterations=200, verbose=False):
	steps = 0
	success = False
	current_board = board.copy()
	
	if (verbose):
		print_board(current_board, n)
	
	for i in range(max_iterations):
		next_node = find_child(current_board, n, sideways_move=True).copy()
		
		if (verbose and len(next_node) != 0):
			print_board(next_node, n)
		
		steps += 1
		if (len(next_node) != 0) and (determine_h_cost(next_node, n) == 0):
			success = True
			break
		if (len(next_node) == 0):
			break
		current_board = next_node.copy()
	return steps, success

n = input_size_board()
iterations = 200

print('NQueen using Hill Climbing :')
success_rate = False
step_count_rate_success = 0
step_count_rate_failure = 0
for i in range(3):
	print('Run ' + str(i + 1) + ':')
	step_count, success = hill_climbing(generate_random_board(n), n, verbose=True)
	if (success):
		print('Success.')
		print('Step count ' + str(step_count))
		step_count_rate_success += step_count
	else:
		print('Failure.')
		step_count_rate_failure += step_count
	success_rate += success
for i in range(3, iterations):
	step_count, success = hill_climbing(generate_random_board(n), n)
	if (success):
		step_count_rate_success += step_count
	else:
		step_count_rate_failure += step_count
	success_rate += success
print('Success rate: ' + str(success_rate/iterations))
print('Failure rate: ' + str(1-(success_rate/iterations)))
print('Average steps until success: ' + str(step_count_rate_success/success_rate))
print('Average steps until failure: ' + str(step_count_rate_failure/(iterations - success_rate)))

from collections import defaultdict
import math
jug1=int(input("Enter maximum capacity of jug1:"))
jug2=int(input("Enter maximum capacity of jug2:"))
aim=int(input("Enter amount of water to be measured:"))
visited = defaultdict(lambda: False)

def waterJugSolver(amt1, amt2): 
    global nsteps
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        nsteps+=1
        return True
    visited[(0,0)]=True
    if visited[(amt1, amt2)] == False:
        print(amt1, amt2)
        nsteps+=1
        visited[(amt1, amt2)] = True

        visited[(jug1,jug2)]= True
        if amt2==0:
          visited[(0,jug2)]= True
        else:
          visited[(jug1,0)]= True      
        return (waterJugSolver(0, amt2) or
                waterJugSolver(amt1, 0) or
                waterJugSolver(jug1, amt2) or
                waterJugSolver(amt1, jug2) or
                waterJugSolver(amt1 + min(amt2, (jug1-amt1)), amt2 - min(amt2, (jug1-amt1))) or
                waterJugSolver(amt1 - min(amt1, (jug2-amt2)), amt2 + min(amt1, (jug2-amt2))))
  
    else:
      return False

if (aim%(math.gcd(jug1,jug2)) is not 0):
    print("no solution")
else:
    print("Steps: ")
    nsteps=0  
    print("solution1")
    waterJugSolver(0, jug2)
    print(f"solution 1 has {nsteps} steps \n")
    nsteps1=nsteps
    nsteps=0
    visited = defaultdict(lambda: False)
    print("solution2")
    waterJugSolver(jug1,0)
    print(f"solution 2 has {nsteps} steps\n")
    nsteps2=nsteps
    if nsteps1 < nsteps2:
        print("solution1 is optimal")
    else:
        print("solution2 is optimal")