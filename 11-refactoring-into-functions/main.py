stats = {
    "count": 0,
    "min": None,
    "max": None,
    "total": 0,
}

def is_valid_number(user_input: str) -> bool:

        try:
            number = int(user_input)

            if number < -100 or number > 100:
                return False
            else:
                return True


        except ValueError:
                    return False


def update_stats(number: int, stats: dict) -> None:
    stats["count"] += 1
    stats["total"] += number
    if stats["min"] is None or stats["max"] is None:
        stats["min"] = number
        stats["max"] = number
        return
    if number < stats["min"]:
        stats["min"] = number
    if number > stats["max"]:
        stats["max"] = number


def main():
    user_input = input("Enter a number: ")

    while user_input != "q":

        if is_valid_number(user_input):
            number = int(user_input)
            update_stats(number, stats)
        else:
            print("Invalid input")

        user_input = input("Enter a number: ")

    print(f"Count: {stats['count']}")
    print(f"Total: {stats['total']}")
    print(f"Min: {stats['min']}")
    print(f"Max: {stats['max']}")




if __name__ == '__main__':
    main()

