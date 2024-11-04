import numpy as np
import re
"""
Day 10: CRT

I need to fix the communication device screen, some sort of CRT and simple CPU driven by a clock circuit.
The CPU has a simple regester X, which starts with 1:
- addx V takes two cycles, after which the X register is increased by V. No change in the intermediate cycle.
- noop takes one cycle to complete

The signal strength is the cycle number multiplied by the value of X during the 20th cycle, and every 40 cycles after.

What is the sum of the first 6 signal strengths?
"""
def crt():
    with open('data/ten.txt') as f:
        # import data
        lines = f.read().splitlines()

        X = 1
        clock = 0
        cycles = [(1,0)]
        for line in lines:
            if line == "noop":
                clock += 1
                cycles.append((X,clock))
            else:
                add = int(re.findall(r'addx (-?\d+)', line)[0])
                X += add
                clock += 2
                cycles.append((X, clock))

        data = create_data(cycles)
        return data



def create_data(cycles):
    """
    the CRT draws the pixel *during* a cycle
    the register finishes *after* a cycle

    input (register, clock) gives us the cycle for which the register is added at the end

    e.g. (13,3) says that at the end of the 3rd cycle, the register read 13 and the sprite is centred at pixel 13
    it is only for the 4th cycle where the sprite is centred at pixel 13
    also, during the cycle i, the pixel is drawn as position i-1
    """
    data = np.zeros(240)
    for idx in range(240):
        data[idx] = int(next(x[0] for x in reversed(cycles) if x[1]<=idx))
    return data


def create_array(data):
    rows = [(0,39), (40,79), (80,119), (120,159), (160,199), (200,239)]
    data_array = []
    for idx in rows:
        row = ''
        for i in range(idx[0], idx[1]+1):
            # i is the position of the pixel 
            # data[i] is the centre of the sprite 
            if (i-idx[0]) in (data[i]-1,data[i], data[i]+1):
                row += '#'
            else:
                row += '.'
        data_array.append(row)
    return data_array

def visualise(data_array):
    for row in data_array:
        print(row)

data = crt()
data_array = create_array(data)
visualise(data_array)