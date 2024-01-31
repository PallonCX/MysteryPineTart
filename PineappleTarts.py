# Function to recursively determine the winner and best move
# 1 representing win, 0 representing invalid value, -1 representing lose
def recurse(box1, box2, dp):
    # Check memo
    if dp[box1][box2] != 0:
        return dp[box1][box2], "Memoed."
    
    # Base cases
    if box1 == 0 or box2 == 0:
        dp[box1][box2] = 1
        winner = "Box 2" if box1 == 0 else "Box 1"
        return dp[box1][box2], f"Take all tarts from {winner}."
    
    if box1 == box2:
        dp[box1][box2] = 1
        return dp[box1][box2], f"Take {box1} tarts from Box 1 and Box 2 each."
    
    # Recursive case
    for i in range(1, min(box1, box2) + 1):
        # Check moves where taking an amount from one box leads to a win
        ans, _ = recurse(box1 - i, box2, dp)
        if ans == -1:
            dp[box1][box2] = 1
            return dp[box1][box2], f"Take {i} tarts from Box 1."
        
        ans, _ = recurse(box1, box2 - i, dp)
        if ans == -1:
            dp[box1][box2] = 1
            return dp[box1][box2], f"Take {i} tarts from Box 2."

        ans, _ = recurse(box1 - i, box2 - i, dp)
        if ans == -1:
            dp[box1][box2] = 1
            return dp[box1][box2], f"Take {i} tarts from Box 1 and Box 2 each."
    
    # If no winning move is found
    dp[box1][box2] = -1
    return dp[box1][box2], "No way to win"  

# Function to display the result and best first move
def pine(box1, box2):
    dp = [[0 for _ in range(box2 + 1)] for _ in range(box1 + 1)]
    ans, best_move = recurse(box1, box2, dp)
    print("You will win!" if ans == 1 else "You will lose!")
    print("Your best first move is:", best_move)

# Main function to take user input and call the main function
def main():
    box1 = int(input("Number of tarts in Box 1? "))
    box2 = int(input("Number of tarts in Box 2? "))
    pine(box1, box2)

# Execute the main function
if __name__ == "__main__":
    main()
