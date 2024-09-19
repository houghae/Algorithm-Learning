def reverse_string(string):
    # base case
    if string == "":
        return ""
    
    # smallest amount of work to do in each iteration
    else:
        char0 = string[0]
        string_shortened = string[1:]
        return reverse_string(string_shortened) + char0

def main():
    string = input("What would you like spelled backward? ")
    print(reverse_string(string))



main()

