def isSorted(ls, rev = False):
    length = len(ls)
    if length == 0:
        raise Exception('The list is empty!')
    if not rev:
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                return False
        return True
    else:
        for i in range(len(ls) - 1):
            if ls[i] < ls[i + 1]:
                return False
        return True

if __name__ == "__main__":
    print("Testing module...")
