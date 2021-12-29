# for match/case instructions https://docs.python.org/3/whatsnew/3.10.html

def parse_input(file_name):
    for line in open(file_name, "r"):
        direction, value = line.split()
        yield direction, int(value)

def solution(part_2 = False):
    horizontal, depth, aim = 0, 0, 0
    for direction , value in parse_input("input.txt"):
        match direction:
            case 'forward':
                horizontal += value
                if part_2:
                    depth += aim * value
            case 'down':
                if part_2:
                    aim += value
                else:
                    depth += value
            case 'up':
                if part_2:
                    aim -= value
                else:
                    depth -= value
    return horizontal * depth

if __name__ == "__main__":
    print(f"First part result {solution()}")
    print(f"Second part result {solution(True)}")
