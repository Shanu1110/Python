def calculate_angle(hour, minute):
    # Calculate the angle made by the hour hand
    hour_angle = 0.5 * (hour * 60 + minute)

    # Calculate the angle made by the minute hand
    minute_angle = 6 * minute

    # Calculate the difference between the two angles
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)

def calculate_cost(angle, A, B, P, Q, X, Y):
    # Calculate the cost of moving the hour hand clockwise and counterclockwise
    hour_clockwise_cost = min(angle, 90) * P + max(0, angle - 90) * Q
    hour_counterclockwise_cost = min(360 - angle, 90) * P + max(0, 360 - angle - 90) * Q

    # Calculate the cost of moving the minute hand clockwise and counterclockwise
    minute_clockwise_cost = min(angle, 90) * X + max(0, angle - 90) * Y
    minute_counterclockwise_cost = min(360 - angle, 90) * X + max(0, 360 - angle - 90) * Y

    # Calculate the total cost for both hands
    total_cost = min(hour_clockwise_cost, hour_counterclockwise_cost) + min(minute_clockwise_cost, minute_counterclockwise_cost)
    return total_cost

def main():
    # Read input
    time_str = input("Enter time in HH:MM format: ")
    target_angle = int(input("Enter target angle: "))
    A = int(input("Enter cost A: "))
    B = int(input("Enter cost B: "))
    P = int(input("Enter cost P: "))
    Q = int(input("Enter cost Q: "))
    X = int(input("Enter cost X: "))
    Y = int(input("Enter cost Y: "))

    # Parse time
    hour, minute = map(int, time_str.split(':'))

    # Calculate the current angle
    current_angle = calculate_angle(hour, minute)

    # Calculate the cost to reach the target angle
    cost = calculate_cost(current_angle, A, B, P, Q, X, Y)
    print(f"The minimum cost to reach the target angle is: {cost:.2f}")

if __name__ == "__main__":
    main()