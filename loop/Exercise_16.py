"""
    Exercise 16: Calculate the cube of all numbers from 1 to a given number
    Write a program to rint the cube of all numbers from 1 to a given number

    Given:

    input_number = 6

    Expected output:

    Current Number is : 1  and the cube is 1
    Current Number is : 2  and the cube is 8
    Current Number is : 3  and the cube is 27
    Current Number is : 4  and the cube is 64
    Current Number is : 5  and the cube is 125
    Current Number is : 6  and the cube is 216
"""

n = 6
for i in range(1,n):
    c = i * i * i
    print(c)