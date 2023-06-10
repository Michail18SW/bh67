def generate_tree(depth):
    if depth == 1:
        return []
    else:
        return [generate_tree(depth-1), generate_tree(depth - 1)]


print(generate_tree(3))
