
# Main program flow
def main():
    print("Welcome to the Hebrew Verb Conjugation Practice Tool!")
    
    # Load verbs from file
    load_verbs()

    # Get user-defined verbs
    get_verbs()

    # Run practice session with subtle pause between rounds
    while True:
        practice()
        input("\nPress Enter to continue...")

# Run the main function
main()