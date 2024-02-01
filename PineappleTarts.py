# Function to recursively determine the winner and best move
# 1 representing win, 0 representing invalid value, -1 representing lose
def recurse(box1, box2, memo):
    # Check memo
    if (box1, box2) in memo:
        return memo[(box1, box2)]
    
    # Base cases
    if box1 == 0 or box2 == 0 or box1 == box2:
        move = (box1, box2)
        willWin = 1 # Which means win after this move 
        memo[(box1, box2)] = (move, willWin)
        return memo[(box1, box2)]
    
    # Recursive case
    # Case 1: Take from box1
    for i in range(1, box1 + 1):
        # Consider all possible moves, what will be the result of your opponent
        result = recurse(box1 - i, box2, memo)

        # Your opponent will loss, take this move
        if result[1] == -1:
            move = (i, 0)
            willWin = 1
            memo[(box1, box2)] = (move, willWin)
            return memo[(box1, box2)]
        
        # For any other result, your opponent may win or it is uncertain, so dont take the move

    # Case 2: Take from box2
    for i in range(1, box2 + 1):
        # Consider all possible moves, what will be the result of your opponent
        result = recurse(box1, box2 - i, memo)

        # Your opponent will loss, take this move
        if result[1] == -1:
            move = (0, i)
            willWin = 1
            memo[(box1, box2)] = (move, willWin)
            return memo[(box1, box2)]
        
        # For any other result, your opponent may win or it is uncertain, so dont take the move   

    # Case 3: Take from both boxes
    for i in range(1, min(box1, box2) + 1):
        # Consider all possible moves, what will be the result of your opponent
        result = recurse(box1 - i, box2 - i, memo)

        # Your opponent will loss, take this move
        if result[1] == -1:
            move = (i, i)
            willWin = 1
            memo[(box1, box2)] = (move, willWin)
            return memo[(box1, box2)]
        
        # For any other result, your opponent may win or it is uncertain, so dont take the move   
    
    # If no winning move is found, return any move
    move = (0, 0)
    willWin = -1
    memo[(box1, box2)] = (move, willWin)
    return memo[(box1, box2)]

# Function to display the result and best first move
def pine(box1, box2, memo):
    ans = recurse(box1, box2, memo)
    print("You will win!" if ans[1] == 1 else "You will lose!")
    print("Your best first move is: Take ", ans[0][0], " tarts from box1. Take ", ans[0][1], " tarts from box2.")

def play(box1, box2):
    memo = {}
    while True:
        print(f"There is {box1} tarts in box1 and {box2} tarts in box2.")
        hint = int(input("Do you want hints for best move? 1 for yes, 0 for no. "))
        if hint == 1:
            pine(box1, box2, memo)
        take1 = int(input("How many tarts you want to take from box1? "))
        take2 = int(input("How many tarts you want to take from box2? "))
        box1 -= take1
        box2 -= take2

        if box1 == 0 and box2 == 0:
            print("Game over!")
            break


# Main function to take user input and call the main function
def main():
    box1 = int(input("Number of tarts in Box 1? "))
    box2 = int(input("Number of tarts in Box 2? "))
    play(box1, box2)

# Execute the main function
if __name__ == "__main__":
    main()
