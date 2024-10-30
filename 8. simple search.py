# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Function to search for a specific name in the list
def search_name(name_to_search, names_list):
    if name_to_search in names_list:
        return f"{name_to_search} is found in the list."
    else:
        return f"{name_to_search} is not found in the list."

# Main program
if __name__ == "__main__":
    # Optional: Allow user input for the search term
    user_input = input("Enter a name to search for (or press Enter to search for 'Sam'): ")
    
    # Default to 'Sam' if no input is given
    search_term = user_input if user_input else "Sam"
    
    # Search for the name and print the result
    result = search_name(search_term, names)
    print(result)