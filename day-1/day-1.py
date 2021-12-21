from more_itertools import pairwise

def parse_input():
    return [int(line_to_int) for line_to_int in open('input.txt').read().rstrip().split()]

def first_part(receive_data):
    return [i < j for i, j in pairwise(receive_data)]

def second_part(receive_data):
    return [sum(receive_data[i-2:i+1]) for i in range(2, len(receive_data))]

if __name__ == "__main__":
    parsed_data = parse_input()
    
    print(f'first part result: {sum(first_part(parsed_data))}')

    print(f'second part result: {sum(first_part(second_part(parsed_data)))}')
