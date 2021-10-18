from cstack import CyStack
from stack import PyStack
import time

cst = CyStack()
pst = PyStack()
n = 1000000

def main():
    ts = time.time()
    for i in range(n):
        cst.push(i)
    print("Push in CyStack costs", time.time()-ts)

    ts = time.time()
    for i in range(n):
        pst.push(i)
    print("Push in PyStack costs", time.time()-ts)

    ts = time.time()
    for i in range(n):
        cst.pop()
    print("Pop in CyStack costs", time.time()-ts)

    ts = time.time()
    for i in range(n):
        pst.pop()
    print("Pop in PyStack costs", time.time()-ts)

if __name__ == "__main__":
    main()
