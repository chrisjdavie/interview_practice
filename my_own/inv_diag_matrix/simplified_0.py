"""
So, I think the trick I missed here is wrt diagonals - the problem can be
solved, as I have in try_*.py, thinking about the inner and outer loops, but
you can also think about it in terms of finding the initial coords, and then
adding and subtracting one.

This is a baaad interview question because of that, cos it's easy to hone in
on one solution, as it will work, and do it at the cost of all 20 mins, cos
it's not the easy one.

I like "magic squares" a lot better, cos it tests similar things but I don't
think that there's such an obvious hole to fall into.

a
b d
c e g
f h j
i k m
n l
o

0 0
0 1, 1 0
0 2, 1 1, 2 0
1 2, 2 1, 3 0
2 2, 3 1, 4 0
3 2, 4 1
4 2
"""
matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"],
    ["m", "n", "o"]
]

def gen_indicies(I_max, J_max):

    for j_col in range(J_max):
        for delta in range(j_col + 1):
            yield 0 + delta, j_col - delta
    
    for i_row in range(1, I_max):
        for delta in range(J_max):
            if i_row + delta >= I_max:
                break
            yield i_row + delta, 2 - delta
  

def print_diags(matrix):

    prev_j_col = 0
    for i_row, j_col in gen_indicies(len(matrix), len(matrix[0])):
        if prev_j_col < j_col:
            print()
        print(matrix[i_row][j_col], end=" ")
        prev_j_col = j_col
    print()


print_diags(matrix)
