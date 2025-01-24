def parse_input():
    """Reads input for the problem."""
    n = int(input())  # Number of wires
    wires = [tuple(map(int, input().split())) for _ in range(n)]
    thresholds = input().split()  # Animal thresholds
    animal_thresholds = {}
    for pair in thresholds:
        animal, threshold = pair.split(';')
        animal_thresholds[animal] = int(threshold)
    touched_animal = input().strip()
    return n, wires, animal_thresholds, touched_animal


def calculate_voltage(wires):
    """Calculates the total voltage from wire intersections efficiently."""
    from collections import defaultdict

    horizontal_wires = []  # (y, x_start, x_end)
    vertical_wires = []  # (x, y_start, y_end)

    # Separate wires by orientation
    for x1, y1, x2, y2 in wires:
        if x1 == x2:  # Vertical wire
            vertical_wires.append((x1, min(y1, y2), max(y1, y2)))
        elif y1 == y2:  # Horizontal wire
            horizontal_wires.append((y1, min(x1, x2), max(x1, x2)))

    intersections = defaultdict(int)

    # Check intersections between horizontal and vertical wires
    for y, x_start, x_end in horizontal_wires:
        for x, y_start, y_end in vertical_wires:
            if x_start <= x <= x_end and y_start <= y <= y_end:
                intersections[(x, y)] += 1

    total_voltage = sum(intersections.values())  # Sum of all intersection voltages
    return total_voltage


def main():
    """Main function to determine if the animal dies and calculate probability."""
    n, wires, animal_thresholds, touched_animal = parse_input()
    total_voltage = calculate_voltage(wires)

    # Determine if the animal dies
    if total_voltage >= animal_thresholds[touched_animal]:
        print("Yes")
    else:
        print("No")

    # Calculate death probability
    death_count = sum(1 for threshold in animal_thresholds.values() if total_voltage >= threshold)
    probability = death_count / len(animal_thresholds)
    print(f"{probability:.2f}")

