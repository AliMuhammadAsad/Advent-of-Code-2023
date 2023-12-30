import re

def count_possible_regex(input_str: str, pattern: str) -> int:
    new_pattern = r"(\.|\?)+".join([r"(#|\?)" * int(i) for i in pattern.split(",")])
    new_pattern = r"^(\.|\?)*" + new_pattern + r"(\.|\?)*$"
    if re.match(new_pattern, input_str):
        if "?" in input_str:
            return count_possible_regex(input_str.replace("?", ".", 1), pattern) + count_possible_regex(input_str.replace("?", "#", 1), pattern)
        else:
            return 1
    return 0

def read_input(input_filename):
    with open(input_filename, "r") as input_file:
        return [tuple(line.strip().split(" ")) for line in input_file]

def part_1(input_filename):
    data = read_input(input_filename)
    return sum(count_possible_part2(springs_to_tuple(d[0], False), size_to_tuple(d[1], False)) for d in data)

def unfold(input_str, separator, times=5):
    return separator.join([input_str] * times)

def springs_to_tuple(sequence, apply_unfold=False):
    if apply_unfold:
        sequence = unfold(sequence, "?")
    return tuple(elem for elem in sequence.split(".") if elem)

def size_to_tuple(sequence, apply_unfold=False):
    if apply_unfold:
        sequence = unfold(sequence, ",")
    return tuple(int(elem) for elem in sequence.split(",") if elem)

is_possible_cache = {}
def is_possible(spring, size):
    key = (spring, size)
    if key not in is_possible_cache:
        pattern = r"^[#|\?]{" + str(size) + "}" + r"(\?|$)"
        is_possible_cache[key] = re.match(pattern, spring) is not None
    return is_possible_cache[key]

count_possible_part2_cache = {}
def count_possible_part2(springs, sizes):
    key = (springs, sizes)
    if key in count_possible_part2_cache:
        return count_possible_part2_cache[key]

    if not sizes:
        result = 1 if all(spring.replace("?", "") == "" for spring in springs) else 0
    elif not springs:
        result = 0
    else:
        first_spring = springs[0]
        if not first_spring:
            result = count_possible_part2(springs[1:], sizes)
        elif first_spring[0] == "#":
            result = count_possible_part2((first_spring[sizes[0] + 1:],) + springs[1:], sizes[1:]) if is_possible(first_spring, sizes[0]) else 0
        else:
            res_when_empty = count_possible_part2((first_spring[1:],) + springs[1:], sizes)
            res_when_broken = count_possible_part2((f"#{first_spring[1:]}",) + springs[1:], sizes)
            result = res_when_empty + res_when_broken
    
    count_possible_part2_cache[key] = result
    return result

def part_2(input_filename):
    data = read_input(input_filename)
    return sum(count_possible_part2(springs_to_tuple(d[0], True), size_to_tuple(d[1], True)) for d in data)

def main():
    input_filename = "inp12.txt"
    answer = part_1(input_filename)
    print(f"Part 1: {answer}")

    answer = part_2(input_filename)
    print(f"Part 2: {answer}")

if __name__ == "__main__":
    main()
