from collections import deque

# Goal state for the 8-puzzle
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Function to print the puzzle
def print_puzzle(state):
    for row in state:
        print(row)

# Function to find the position of the empty space (0)
def find_empty(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Function to check if a state is the goal state
def is_goal(state):
    return state == goal_state

# Function to swap two elements in a list
def swap(state, x1, y1, x2, y2):
    new_state = [row[:] for row in state]  # Create a copy of the state
    new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
    return new_state

# Function to perform BFS for the 8-puzzle
def bfs(start_state):
    visited = set()  # To track visited states
    queue = deque([(start_state, [])])  # Queue for BFS, stores (state, moves_list)
    
    while queue:
        state, path = queue.popleft()
        
        # If the current state is the goal state
        if is_goal(state):
            print("Solution found!")
            print("Moves to solve the puzzle:")
            for move in path:
                print(move)
            return
        
        visited.add(tuple(tuple(row) for row in state))  # Add to visited
        
        # Get the empty space's position
        x, y = find_empty(state)
        
        # Possible directions: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the move is within bounds
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = swap(state, x, y, nx, ny)
                if tuple(tuple(row) for row in new_state) not in visited:
                    queue.append((new_state, path + [f"Move empty space to ({nx},{ny})"]))
                    visited.add(tuple(tuple(row) for row in new_state))

    print("No solution found.")

# Starting state for the 8-puzzle (example)
start_state = [[1, 2, 3], [5, 6, 0], [4, 7, 8]]

# Print the initial state
print("Initial state:")
print_puzzle(start_state)

# Solve the puzzle using BFS
bfs(start_state)
