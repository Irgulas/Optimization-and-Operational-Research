##Library
import csv
import numpy as np


##Function
def read_csv(file_path):
    revenues = []
    days = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            revenue, day = map(int, row)
            revenues.append(revenue)
            days.append(day)
    return revenues, days

revenues, days = read_csv(r"D:\Uvic\Cours\Optimization\Ex8.csv")

def optimize_schedule(revenues, days, max_days):
    num_projects = len(revenues)
    best_solution = [0] * num_projects
    best_value = 0

    def calculate_upper_bound(solution, current_index, current_days, current_value):
        if current_days > max_days:
            return -np.inf
        for i in range(current_index + 1, num_projects):
            if solution[i] == 0 and current_days + days[i] > max_days:
                return current_value + (revenues[i] / days[i]) * (max_days - current_days)
        return current_value

    def explore_solution_space(solution, current_index, current_days, current_value):
        nonlocal best_solution, best_value

        if current_index == num_projects:
            if current_value > best_value:
                best_solution = solution.copy()
                best_value = current_value
        else:
            # Explore the branch with the project included
            solution[current_index] = 1
            new_days = current_days + days[current_index]
            new_value = current_value + revenues[current_index]
            if new_days <= max_days and calculate_upper_bound(solution, current_index, new_days, new_value) > best_value:
                explore_solution_space(solution, current_index + 1, new_days, new_value)

            # Explore the branch with the project excluded
            solution[current_index] = 0
            new_days = current_days
            new_value = current_value
            if calculate_upper_bound(solution, current_index, new_days, new_value) > best_value:
                explore_solution_space(solution, current_index + 1, new_days, new_value)

    def recursively_explore_solution_space(solution, current_index, current_days, current_value):
        if current_index == num_projects:
            return

        # Explore the branch with the project included
        solution[current_index] = 1
        new_days = current_days + days[current_index]
        new_value = current_value + revenues[current_index]
        if new_days <= max_days and calculate_upper_bound(solution, current_index, new_days, new_value) > best_value:
            explore_solution_space(solution, current_index + 1, new_days, new_value)

        # Explore the branch with the project excluded
        solution[current_index] = 0
        new_days = current_days
        new_value = current_value
        if calculate_upper_bound(solution, current_index, new_days, new_value) > best_value:
            explore_solution_space(solution, current_index + 1, new_days, new_value)

        recursively_explore_solution_space(solution, current_index + 1, current_days, current_value)

    solution = [0] * num_projects
    recursively_explore_solution_space(solution, 0, 0, 0)
    return best_solution, best_value
##
# Problem data
max_days = 345

# Solve the problem
best_solution, best_value = branch_and_bound(revenues, days, max_days)

# Print the results
print("Best solution:", best_solution)
print("Best value:", best_value)

