import numpy as np
'''
Day 1: Calorie Counting

Each elf carries food with a certain number of calories. Each elf's entry in the log is separated by a newline
Find the elf with the most calories and calculate the value.

Part 2 is to find the calories of the top three elves
'''

with open('data/one.txt') as f:
    lines = f.read().split('\n\n') # splits entries into concatenated strings, separator \n\n is a newline
    elves = [[eval(cal) for cal in line.splitlines()] for line in lines] # takes concatenated strings and gives entry of each elf as an array
    calories = [np.sum(elf) for elf in elves] # array of total calories for each elf
    
print(np.max(calories)) # this is calories of the elf with the most calories
print(np.sum(sorted(calories)[-3:])) # this is the total calories of the three most calorific elves