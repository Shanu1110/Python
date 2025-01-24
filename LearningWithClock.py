def rotate_layer(layer, positions, direction, odd_layer):
    n = len(layer)
    rotated = [None] * n

    if direction == "clockwise":
        for i in range(n):
            rotated[(i + positions) % n] = layer[i]
    else:  # counterclockwise
        for i in range(n):
            rotated[(i - positions) % n] = layer[i]

    # Replace characters based on layer type
    for i in range(n):
        if odd_layer:
            rotated[i] = chr(((ord(rotated[i]) - ord('A') - 1) % 26) + ord('A'))
        else:
            rotated[i] = chr(((ord(rotated[i]) - ord('A') + 1) % 26) + ord('A'))

    return rotated


def apply_query(matrix, row, col, size):
    layers = []
    n = len(matrix)
    # Extract layers
    for layer in range(size // 2):
        current_layer = []
        # Top edge
        for j in range(col + layer, col + size - layer):
            current_layer.append(matrix[row + layer][j])
        # Right edge
        for i in range(row + layer + 1, row + size - layer - 1):
            current_layer.append(matrix[i][col + size - layer - 1])
        # Bottom edge
        for j in range(col + size - layer - 1, col + layer - 1, -1):
            current_layer.append(matrix[row + size - layer - 1][j])
        # Left edge
        for i in range(row + size - layer - 2, row + layer, -1):
            current_layer.append(matrix[i][col + layer])

        layers.append(current_layer)

    # Rotate layers and replace back
    for layer_idx, layer in enumerate(layers):
        odd_layer = (layer_idx + 1) % 2 == 1
        direction = "counterclockwise" if odd_layer else "clockwise"
        positions = layer_idx + 1
        rotated_layer = rotate_layer(layer, positions, direction, odd_layer)

        # Write back rotated layer
        idx = 0
        for j in range(col + layer_idx, col + size - layer_idx):
            matrix[row + layer_idx][j] = rotated_layer[idx]
            idx += 1
        for i in range(row + layer_idx + 1, row + size - layer_idx - 1):
            matrix[i][col + size - layer_idx - 1] = rotated_layer[idx]
            idx += 1
        for j in range(col + size - layer_idx - 1, col + layer_idx - 1, -1):
            matrix[row + size - layer_idx - 1][j] = rotated_layer[idx]
            idx += 1
        for i in range(row + size - layer_idx - 2, row + layer_idx, -1):
            matrix[i][col + layer_idx] = rotated_layer[idx]
            idx += 1


def process_matrix(n, matrix, queries):
    for row, col, size in queries:
        apply_query(matrix, row, col, size)
    # Construct the resulting string
    result = ''.join(''.join(row) for row in matrix)
    return result


# Input
n = int(input())
matrix = [list(input().strip().split()) for _ in range(n)]
q = int(input().strip())
queries = [tuple(map(int, input().strip().split())) for _ in range(q)]

# Process and output the result
result = process_matrix(n, matrix, queries)
print(result, end="")