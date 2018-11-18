#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

def tower_of_hanoi(n, fromPeg, toPeg, auxPeg):
    #if only 1 disk is present, move it straight from 'from' to 'to'.
    if n < 1:
        return

    if n == 1:
        x = fromPeg.pop()
        toPeg.append(x)
    else:
         # move n-1 disks to auxiliary peg
         tower_of_hanoi(n - 1, fromPeg, auxPeg, toPeg)

         # move 1 disk to 'to' peg
         tower_of_hanoi(1, fromPeg, toPeg, auxPeg)

         # move n-1 disks from auxiliary peg to 'to' peg.
         tower_of_hanoi(n - 1, auxPeg, toPeg, fromPeg)



if __name__ == '__main__':
    A = [5, 4, 3, 2, 1]
    B = []
    X = []

    print('Before:')
    print("From: ", A)
    print("To: ", B)
    print("Auxiliary: ", X)
    print('-------')


    tower_of_hanoi(len(A), A, B, X)

    print('After:')
    print("From: ", A)
    print("To: ", B)
    print("Auxiliary: ", X)








