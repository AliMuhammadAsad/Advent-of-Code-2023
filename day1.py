def load(filename):
    with open(filename, 'r') as file:
        return file.read().strip().split('\n')

def rnd(text):
    return ''.join(filter(str.isdigit, text))

def pl1(line):
    line = rnd(line)
    line = '0' if line == '' else line[0] + line[-1]
    return int(line)

def rwnums(line):
    word_to_digit = {
        'one': 'on1ne', 'two': 'tw2wo', 'three': 'thre3hree',
        'four': 'fou4our', 'five': 'fiv5ive', 'six': 'si6ix', 
        'seven': 'seve7even', 'eight': 'eigh8ight', 'nine': 'nin9ine'
    }
    for word, digit_code in word_to_digit.items():
        line = line.lower().replace(word, digit_code)
    return line

def pl2(line):
    line = rwnums(line)
    line = rnd(line)
    line = '0' if line == '' else line[0] + line[-1]
    return int(line)

def solve_part1(filename):
    data = load(filename)
    total = sum(pl1(line) for line in data)
    return total

def solve_part2(filename):
    data = load(filename)
    total = sum(pl2(line) for line in data)
    return total

print("Part 1:", solve_part1("inp1.txt"))
print("Part 2:", solve_part2("inp1.txt"))