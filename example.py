from cstack import CyStack

cst = CyStack()

def main():
    for i in range(10):
        cst.push(i)
    print("The size of the stack is", cst.size())
    print("  stack:", cst.take(cst.size()))


    print("The last/top item of the stack is", cst.top())
    print("  stack:", cst.take(cst.size()))


    print("The top 5 items of the stack are", cst.take(5))
    print("  stack:", cst.take(cst.size()))


    print("The 4th item of the stack is", cst.nth(3))
    print("  stack:", cst.take(cst.size()))


    cst.set_nth(3, 30)
    print("The 4th item of the stack, after setting, is", cst.nth(3))
    print("  stack:", cst.take(cst.size()))


    cst.insert(3, 40)
    print("The size of the stack, after insertion, is", cst.size())
    print("The 4th item of the stack, after insertion, is", cst.nth(3))
    print("  stack:", cst.take(cst.size()))


    cst.pop()
    print("The last/top item of the stack is", cst.top())
    print("  stack:", cst.take(cst.size()))

if __name__ == "__main__":
    main()