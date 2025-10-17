# Program #2: Larger than n
# In a program, write a function (with NO output) that accepts two arguments: number n, and a list.
# Assume that the list contains numbers.
# The function shell has been written out on line 30, (def display_larger_than_n_list)
# and should display all of the numbers in the list that are greater than then number n.
def main():

    user_input = input("Enter a list of numbers separated by spaces: ")
 
    n_list = [float(x) for x in user_input.split()]

    n = float(input("Enter a number n: "))


    display_larger_than_n_list(n, n_list)

def display_larger_than_n_list(n, n_list):
    for number in n_list:
        if number > n:
            print(number)



if __name__ == '__main__':
    main()