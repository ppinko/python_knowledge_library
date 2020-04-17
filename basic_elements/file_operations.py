"""
Task 1

Write a Python program to read last n lines of a file.
"""

file_name = "Harry_Potter_und_der_Stein_der_Weisen.txt"

def read_n_last_lines(file, n):
    try:
        with open("Harry_Potter_und_der_Stein_der_Weisen.txt", "r") as f:
            all = f.readlines()
            # print(len(all))
            print(all[(n*(-1)-1):-1])
    except:
        print("File cannot be found")

read_n_last_lines(file_name, 5)

