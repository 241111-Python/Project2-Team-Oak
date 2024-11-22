import controller
import view

if __name__ == "__main__":
    # Print menu options
    view.print_menu_options()
    while (user_selection := input("What would you like to do? ")):
        controller.handle_user_input(user_selection)


