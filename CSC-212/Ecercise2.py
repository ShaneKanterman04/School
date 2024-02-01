#Shane Kanterman

def histogram(s):
    char_frequency = {}

    # Iterate through each character in the input string
    for char in s:
        # Use the get method to either increment the existing count or set it to 1
        char_frequency[char] = char_frequency.get(char, 0) + 1

    return char_frequency

def main():
    # Example usage
    input_string = input()
    result = histogram(input_string)

    # Print the result
    print("Character frequencies in '{}': {}".format(input_string, result))

if __name__ == "__main__":
    main()
