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
                        choices=["standard", "ppp"],
                        type=str,
                        nargs="+",
                        help="Select one or more reports from \"standard\", \"ppp-<date>\", or \"ppp-<country>\" where date or country must be specified. Separate reports with spaces. Select \"all\" for all reports."
                        )
    
    parser.add_argument("--country", "-c",
                        type=str,
                        help="Specify the country for the PPP reports. Required if using \"ppp\" with \"-r\"."
                        )
    
    parser.add_argument("--date", "-d",
                    type=str,
                    help="Specify the date (yyyy-mm-dd) for the PPP reports. Required if using \"ppp\" with \"-r\" for a country report."
                    )

    args = parser.parse_args()

    if args.filename:
        print(f"Processing file: {args.filename}")
        controller.handle_upload_data()

    if args.reports:
        additional_arguments = {"country": args.country, "date": args.date}
        for report in args.reports:
            report = report.strip().lower()
            generated_report = controller.handle_generate_reports(report, additional_arguments)

    # Print menu options
    view.print_menu_options()
    while (userSelection := input("What would you like to do? ")):
        controller.handle_user_input(userSelection)


