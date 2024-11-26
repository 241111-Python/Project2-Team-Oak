import controller
import view


if __name__ == "__main__":
    # Print menu options
    view.print_menu_options()
    while (userSelection := input("What would you like to do? ")):
        controller.handle_user_input(userSelection)
        view.print_menu_options()


