'''
🎯 Goal

Write a program that asks the user for integers and produces clean stats, but ignores invalid entries.

You’ll track:

how many valid numbers were entered

total of valid numbers

min and max of valid numbers

Invalid entries should be rejected with a message and not affect the stats.

This builds real fluency: control flow, validation, and state updates.

📥 Inputs

The user repeatedly enters text.

Rules:

Input ends when the user enters: q (lowercase only)

A valid number is an integer between -100 and 100 inclusive

Anything else is invalid (including blanks, words, 101, -999, Q, quit, etc.)

⚠️ Constraints

❌ Do NOT use lists/tuples/sets/dicts to store values

❌ Do NOT use continue

❌ Do NOT use break (except the loop condition itself — you should structure the loop to end naturally)

❌ No libraries

✅ Use a while loop

✅ Use try/except for conversion

✅ Use the “first valid value sets baseline” pattern for min/max
'''

count = 0
total = 0
min_value = None
max_value = None

user_input = input("Enter a number: ")

while user_input != "q":
    try:
        number = int(user_input)

        if number < -100 or number > 100:
            print("Invalid input")
        else:
            count += 1
            total += number

            if min_value is None:
                min_value = number
                max_value = number
            else:
                if number < min_value:
                    min_value = number
                if number > max_value:
                    max_value = number

    except ValueError:
        print("Invalid input")

    user_input = input("Enter a number: ")

print(f"Count: {count}")
print(f"Total: {total}")
print(f"Min: {min_value}")
print(f"Max: {max_value}")


