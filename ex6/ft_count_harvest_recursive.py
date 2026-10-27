def ft_count_harvest_recursive() -> None:
    days = int(input('Days until harvest: '))
    print_days(days)
    print('Harvest time!')


def print_days(n: int) -> None:
    if n <= 0:
        return
    print_days(n - 1)
    print(f'Day {n}')
