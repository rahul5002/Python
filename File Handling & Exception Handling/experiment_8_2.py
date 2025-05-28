#Store integers in a file. 
#a. Find the max number 
#b. Find average of all numbers 
#c. Count number of numbers greater than 100 
def analyze_numbers(numbers):
    return (
        max(numbers),
        sum(numbers) / len(numbers),
        sum(1 for num in numbers if num > 100)
    )
with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]
max_num, avg, count_gt_100 = analyze_numbers(numbers)
print(f"Maximum number: {max_num}")
print(f"Average: {avg:.2f}")
print(f"Numbers greater than 100: {count_gt_100}")