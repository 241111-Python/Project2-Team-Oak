import controller
import view
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Big Mac Data Analyzer",
        description="This program is intended to allow users to analyze big mac data. User are able to view various subsets of the data by choosing custom filters. They are also able to output reports for later use."
    )

    parser.add_argument("--filename", "-f",
                        type=str,
                        help="Select a different file to be processed instead of the default: bigmac.csv"
                        )


    parser.add_argument("--reports", "-r",
                        type=str,
                        nargs="+",
                        help="Select one or more reports from \"standard\", \"ppp-<date>\", or \"ppp-<country>\" where date or country must be specified. Separate reports with spaces. Select \"all\" for all reports."
                        )
    
    args = parser.parse_args()

    if args.filename:
        print(f"Processing file: {args.filename}")
        controller.handle_upload_data()

    if args.reports:
        for report in args.reports:
            print(report)


    # Print menu options
    view.print_menu_options()
    while (userSelection := input("What would you like to do? ")):
        controller.handle_user_input(userSelection)


