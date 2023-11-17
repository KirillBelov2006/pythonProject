def count_inside_list(data: list, num: int) -> int:
    count = 0

    for value in data:
        if value == num:
            count += 1
    return  count
