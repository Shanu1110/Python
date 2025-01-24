def find_intersection(wire1, wire2):
    # ... (Implementation for finding intersection point)

def calculate_voltage(wires_at_point):
    min_cells = min(min(abs(x1 - x2), abs(y1 - y2)) for wire in wires_at_point for x1, y1, x2, y2 in wire) // 2)
    return len(wires_at_point) * min_cells

def main():
    N = int(input("Enter the number of wires: "))
    wires = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input("Enter wire coordinates (x1 y1 x2 y2): ").split())
        wires.append((x1, y1, x2, y2))

    animal_data = input("Enter animal data (animal:threshold): ")
    animal_thresholds = {k: int(v) for k, v in (item.split(':') for item in animal_data.split())}

    touched_animal = input("Enter the name of the touched animal: ")

    intersections = defaultdict(list)
    for i in range(N):
        for j in range(i + 1, N):
            if find_intersection(wires[i], wires[j]):
                x, y = find_intersection_point(wires[i], wires[j])
                intersections[(x, y)].append(wires[i])
                intersections[(x, y)].append(wires[j])

    total_voltage = sum(calculate_voltage(wires_at_point) for wires_at_point in intersections.values())

    touched_animal_voltage = animal_thresholds[touched_animal.lower()]
    died = total_voltage > touched_animal_voltage
    result = "Yes" if died else "No"

    vulnerable_animals = sum(1 for threshold in animal_thresholds.values() if total_voltage > threshold)
    probability = round(vulnerable_animals / len(animal_thresholds), 2)

    print(result)
    print(probability)