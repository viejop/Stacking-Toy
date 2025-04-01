from colorama import Fore, Style


#defines colors
colors = {
    'red':Fore.RED,
    'orange':Fore.YELLOW + Style.BRIGHT,
    'yellow':Fore.YELLOW,
    'green':Fore.GREEN,
    'blue':Fore.BLUE
}
#creates ascii art
ascii_art = {
    'red': """
 _____________________
|                     |
|         red         |
|_____________________|
    """,
    'orange': """
 _________________
|                 |
|     orange      |
|_________________|
    """,
    'yellow': """
  _______________
 |               |
 |     yellow    |
 |_______________|
    """,
    'green': """
   ____________
  |            |
  |   green    |
  |____________|
    """,
    'blue': """
    __________
   |          |
   |   blue   |
   |__________|
    """
}

#creates a stack list
stack = []
#function to print stack
def print_stack():
    """Print the stack of rings with color"""
    print("\nCurrent stack:")
    if not stack:
        print("The stack is empty")
    else:
        for ring in reversed(stack):
            print(f"{colors[ring]}{ascii_art[ring]}{Style.RESET_ALL}")
    print("\n")
#function to add rings
def add_ring(ring_color):
    """Add a colored ring"""
    if ring_color in colors:
        stack.append(ring_color)
        print(f"Added a {ring_color} ring to the stack.")
        print(f"{colors[ring_color]}{ascii_art[ring_color]}{Style.RESET_ALL}")  #displays the ascii art for the chosen ring
        
    else:
        print("Invalid color, please choose from red, orange, yellow, green, or blue.")
    print_stack()
    
def remove_ring():
    """Remove the top ring from the stack"""
    if stack:
        removed_ring = stack.pop()
        print(f"Removed the top ring: {removed_ring.capitalize()} ring.")
    else:
        print("The stack is already empty.")
    print_stack()
    
def bigbucks():
    while True:
        print("Options:")
        print("1. Add a ring")
        print("2. Remove the top ring")
        print("3. Quit")
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            ring_color = input("Enter the color of the ring (red, orange, yellow, green, blue)").lower()
            add_ring(ring_color)
        elif choice == '2':
            remove_ring()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose again.")
            
bigbucks()
