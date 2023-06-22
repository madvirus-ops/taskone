import re
import random
import psycopg2
from itertools import groupby

# HTML table data
table_data = """
<table>
	<thead>
		<th>DAY</th><th>COLOURS</th>
	</thead>
	<tbody>
	<tr>
		<td>MONDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>TUESDAY</td>
		<td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
	</tr>
	<tr>
		<td>WEDNESDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
	</tr>
	<tr>
		<td>THURSDAY</td>
		<td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>FRIDAY</td>
		<td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
	</tr>
	</tbody>
</table>
"""

# 1. Extract colors from HTML table using regular expression
colors = re.findall(r'([A-Z]+)', table_data)

# 2. Calculate the mean color
mean_color = max(set(colors), key=colors.count)
print("mean",mean_color)

# 3. Calculate the most worn color throughout the week
most_worn_color = max(colors, key=colors.count)
print("most worn",most_worn_color)
# 4. Calculate the median color
n = len(colors)
sorted_colors = sorted(colors)
if n % 2 == 0:
    median_color = sorted_colors[n // 2 - 1]
else:
    median_color = sorted_colors[n // 2]
print("median",median_color)
# 5. Calculate the variance of the colors
variance = sum((len(list(g)) - (len(colors) / len(set(colors))))**2 for _, g in groupby(sorted(colors))) / len(colors)

print("variance",variance)
# 6. Save the colors and their frequencies in PostgreSQL database
conn = psycopg2.connect(database="ntoju", user="root", password="root", host="localhost", port="5432")
cursor = conn.cursor()

# Create a table to store colors and their frequencies if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS dress_colors (
        color TEXT PRIMARY KEY,
        frequency INTEGER
    );
""")

# Insert or update color frequencies
for color in set(colors):
    frequency = colors.count(color)
    cursor.execute("""
        INSERT INTO dress_colors (color, frequency)
        VALUES (%s, %s)
        ON CONFLICT (color) DO UPDATE SET frequency = dress_colors.frequency + %s;
    """, (color, frequency, frequency))

conn.commit()
conn.close()
print("saved to db")

# 7. Recursive searching algorithm to search for a number in a list
def recursive_search(numbers, target, start=0, end=None):
    if end is None:
        end = len(numbers) - 1
    if start > end:
        return -1
    mid = (start + end) // 2
    if numbers[mid] == target:
        return mid
    elif numbers[mid] < target:
        return recursive_search(numbers, target, mid + 1, end)
    else:
        return recursive_search(numbers, target, start, mid - 1)

# Test recursive search
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_number = int(input("Enter a number to search: "))
result = recursive_search(numbers, target_number)
if result != -1:
    print(f"Number found at index {result}.")
else:
    print("Number not found.")

# 8. Generate random 4-digit number of 0s and 1s and convert it to base 10
random_number = random.randint(0, 2**4 - 1)
binary_number = f"{random_number:04b}"
decimal_number = int(binary_number, 2)
print(f"Random 4-digit binary number: {binary_number}")
print(f"Equivalent decimal number: {decimal_number}")

# 9. Calculate the sum of the first 50 Fibonacci sequence
fibonacci_sequence = [0, 1]
for i in range(2, 50):
    fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
sum_fibonacci = sum(fibonacci_sequence[:50])

print(f"Sum of the first 50 Fibonacci sequence: {sum_fibonacci}")

