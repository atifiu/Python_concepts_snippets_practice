print("Inside test_main")
print("program_name ", __name__)
def sum(*args):
    result = 0
    for x in args :
        result = result +x
    return result
def main():
    result = sum(4, 5, 6)
    print("Total sum = ", result)
    print("End of main")

if __name__ == '__main__':
    main()