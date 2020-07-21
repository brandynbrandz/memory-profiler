@profile
def my_func():
    a = [7] * (64 ** 7)
    b = [9] * (6 * 100 ** 26)
    del b
    return a

if __name__ == '__main__':
    my_func()
