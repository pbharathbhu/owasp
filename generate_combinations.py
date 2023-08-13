import sys
import itertools

def generate_combinations_to_file(n, filename):
    if n <= 0:
        print("Please provide a positive integer greater than 0.")
        return

    combinations = itertools.product(range(10), repeat=n)

    with open(filename, 'w') as f:
        for combo in combinations:
            f.write(''.join(map(str, combo)) + '\n')

if len(sys.argv) != 3:
    print("Usage: python script_name.py <number_of_digits> <output_filename>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    filename = sys.argv[2]
except ValueError:
    print("Please provide a valid number of digits.")
    sys.exit(1)

generate_combinations_to_file(n, filename)
