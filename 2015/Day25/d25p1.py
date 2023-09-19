def main():
    solution_coordinates = (2981, 3075)
    solution_index = get_solution_index(*solution_coordinates)
    current = 20151125
    for _ in range(solution_index - 1):
        current = next_code(current)
    print(current)


def next_code(cur_code):
    return (cur_code * 252533) % 33554393


def get_solution_index(row, column):
    return sum(range(row + column - 1)) + column


if __name__ == "__main__":
    main()
