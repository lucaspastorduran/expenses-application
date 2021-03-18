import expenses_app
from pathlib import Path

FILE_NAME = "abanca_extracto.csv"

if __name__ == '__main__':
    print("Start main script.")

    # Get file path
    main_path = Path(__file__).parent.absolute()
    file_path = main_path / FILE_NAME

    # Read account data
    df = expenses_app.read_file(file_path, ";")

    # Print dataframe
    expenses_app.print_df(df)

    # Print Expenses App
    my_app_class = expenses_app.ExpensesApp()
    print(my_app_class)

    print("End main script.")



