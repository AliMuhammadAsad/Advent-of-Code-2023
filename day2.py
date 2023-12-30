MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def load(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def solve_part1(input_str):
    total = 0
    lines = input_str.split('\n')
    
    for line in lines:
        parts = line.strip().split(':')
        id = int(parts[0].split()[1])
        total += id
        
        parts = parts[1].strip().split(';')
        impossible = False
        
        for part in parts:
            colors = part.strip().split(',')
            
            for color in colors:
                count, color_name = color.strip().split()
                count = int(count)
                
                if (color_name == "red" and count > MAX_RED) or \
                   (color_name == "green" and count > MAX_GREEN) or \
                   (color_name == "blue" and count > MAX_BLUE):
                    total -= id
                    impossible = True
                    break
                
            if impossible:
                break
    
    return total

def solve_part2(input_str):
    power = 0
    lines = input_str.split('\n')
    
    for line in lines:
        parts = line.strip().split(':')
        parts = parts[1].strip().split(';')
        red = float('-inf')
        green = float('-inf')
        blue = float('-inf')
        
        for part in parts:
            colors = part.strip().split(',')
            
            for color in colors:
                count, color_name = color.strip().split()
                count = int(count)
                if color_name == "red":
                    red = max(red, count)
                elif color_name == "green":
                    green = max(green, count)
                else:
                    blue = max(blue, count)
        power += red * green * blue
    return int(power)

print("Part 1:", solve_part1(load("inp2.txt")))
print("Part 2:", solve_part2(load("inp2.txt")))
