import os

# restaurants = ['Lunar Pizzeria', 'Atlantida Sushi'] # List of restaurants
restaurants = [
    {"name": "Lunar Pizzeria", "category": "Italian", "active": True},
    {"name": "Atlantida Sushi", "category": "Japanese", "active": False},
    {"name": "Gaucho Steakhouse", "category": "Brazilian", "active": True}
] # List of restaurants with dictionaries (JSON)

def example_pass():
    """
    Example function that does nothing.

    This function is a placeholder and is used to demonstrate the use of the `pass` keyword.
    The `pass` keyword is useful when a statement is syntactically required but no action is needed.
    """
    pass

def display_program_name():
    """ Function to display the program name """
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """) # Triple quotes can be used for multi-line strings.

def return_to_main_menu():
    """
    Prompts the user to return to the main menu.

    This function waits for the user to press Enter and then calls the `main` function.
    """
    input("Press Enter to return to the main menu")
    main()

def change_restaurant_status():
    """
    Toggles the activation status of a restaurant.

    This function allows the user to activate or deactivate a restaurant by entering its name. It searches
    for the restaurant in the `restaurants` list and updates its "active" status if found.

    Raises:
        ValueError: If the entered restaurant name is not found in the list.
    """
    display_subtitle("Activate/Deactivate restaurant...")
    restaurant_name = input("Enter the name of the restaurant to activate/deactivate: ")
    restaurant_found = False

    for restaurant in restaurants:
        if restaurant_name == restaurant["name"]:
            restaurant_found = True
            restaurant["active"] = not restaurant["active"] # Toggles the boolean value
            status = "activated" if restaurant["active"] else "deactivated"
            print(f"Restaurant {restaurant_name} was successfully {status}.\n")
        if not restaurant_found:
            print(f"Restaurant {restaurant_name} not found.\n")
    return_to_main_menu()

def display_subtitle(text):
    """
    Displays a formatted subtitle.

    Args:
        text (str): The subtitle text to display.

    This function clears the screen and displays the subtitle text surrounded by a border of asterisks.
    """
    clear_screen()
    # line = "-" * len(text)
    line = "*" * len(text)
    print(f"{line}\n{text}\n{line}\n")

def display_options():
    """
    Displays the main menu options.

    This function lists the available options for the user to interact with the program.
    """
    print("1. Register restaurant")
    print("2. List restaurants")
    print("3. Change restaurant status")
    print("4. Exit\n")

def register_restaurant():
    """
    Registers a new restaurant.

    This function prompts the user to input the restaurant's name and category, then adds the new restaurant
    as a dictionary to the `restaurants` list. The newly added restaurant is set to inactive by default.

    Inputs:
        name (str): Name of the restaurant.
        category (str): Category of the restaurant.

    Outputs:
        restaurant_data (dict): Dictionary with the restaurant data added to the restaurant list
    """
    display_subtitle("Register new restaurants...")
    name = input("Enter the restaurant name: ")
    category = input(f"Enter the category of the restaurant {name}: ")
    restaurant_data = {"name": name, "category": category, "active": False}
    restaurants.append(restaurant_data)
    print(f"Restaurant {name} was successfully registered under category {category} and is inactive.\n")
    return_to_main_menu()

def list_restaurants():
    """
    Lists all registered restaurants.

    This function iterates through the `restaurants` list and displays each restaurant's name, category,
    and status (active or inactive). If no restaurants are registered, it displays a corresponding message.
    """
    display_subtitle("Listing restaurants...")
    if len(restaurants) == 0:
        print("No restaurants registered.\n")
    else:
        print(f"{'Restaurant Name'.ljust(27)} | {'Category'.ljust(20)} | {'Status'}")
        for restaurant in restaurants:
            name = restaurant["name"]
            category = restaurant["category"]
            active = "Active" if restaurant["active"] else "Inactive"
            print(f"- {name.ljust(25)} | {category.ljust(20)} | {active.ljust(20)}")
            # print(f"- {name} | {restaurant['category']} | {'Active' if restaurant['active'] else 'Inactive'}") # No need to create variables
    print("\n")
    return_to_main_menu()

    """ With while
    counter = 0
    while counter < len(restaurants):
        print(f"{counter + 1}. {restaurants[counter]}")
        counter += 1
    """

def choose_option():
    """
    Processes the user's menu option selection.

    This function prompts the user to choose an option from the main menu and executes the corresponding function.
    If the input is invalid, it displays an error message and prompts the user again.

    Raises:
        ValueError: If the input is not a valid integer.
    """
    try: # Exception handling (It tries to execute the code; if an error occurs, it executes the except block)
        chosen_option = int(input("Choose an option: "))  # input always returns a string
        # chosen_option = int(chosen_option) # Converts a string to an integer
        # print(f"Chosen option: {chosen_option}\n") # f-string
        # print(type(chosen_option))
        # print(type(1))

        # with match
        match chosen_option:
            case 1:
                register_restaurant()
            case 2:
                list_restaurants()
            case 3:
                change_restaurant_status()
            case 4:
                finalize_app()
            case _:
                invalid_option()
        # Match is a new feature in Python 3.10 that allows for simpler and more readable comparisons; in other languages, it is known as switch case.

        """ With if, elif, and else 
            if chosen_option == 1:
                print("Register restaurant...")
            elif chosen_option == 2:
                print("List restaurants...")
            elif chosen_option == 3:
                print("Activate restaurant...")
            else:
                finalize_app()
        """
    except ValueError: # If the user enters a value that is not an integer, it falls into this exception block and executes the code below.
        invalid_option()

def invalid_option():
    """
    Handles invalid menu option selection.

    This function displays an error message and redirects the user back to the main menu.
    """
    print("Invalid option. Please try again.\n")
    return_to_main_menu()

def clear_screen():
    """
    Clears the terminal screen.

    This function executes the appropriate command to clear the terminal screen based on the operating system.
    """
    os.environ['TERM'] = 'xterm'  # Sets the terminal as xterm (Linux only)
    # os.system('clear')  # Clears the terminal screen on Linux and macOS
    os.system('cls')  # Clears the terminal screen on Windows

def finalize_app():
    """
    Terminates the application.

    This function displays a farewell message and exits the program.
    """
    display_subtitle("Terminating application...")
    exit() # The `exit()` function terminates the application.

def main():
    """"
    Main entry point for the program.

    This function initializes the program by clearing the screen, displaying the program name and menu options,
    and then processing the user's choice.
    """
    clear_screen()
    display_program_name()
    display_options()
    choose_option()

if __name__ == "__main__":
    main()