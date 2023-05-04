# Description: Utility functions for the project.


def read_schema_column_datatypes(filepath: str) -> None:
    """
    Reads a file containing the column names and data types, and outputs a file with the desired format.

    Arguments:
        filepath -- Path to the file containing the column names and data types.
    """

    # Open File to read, and open another to wirte output
    with open(filepath, "r") as input_file, open(
        "formatted_schema.txt", "w+"
    ) as output_file:
        for line in input_file:
            if line.startswith("df"):
                name_dataframe = line.split(sep="\n")[
                    0
                ]  # It comes with an \n at the end.
                output_file.write(
                    f"{name_dataframe} = {{ \n"
                )  # {{ allows to print '{' symbol in the output file.

            elif line.isspace():
                # print('Line contains only whitespace', end='')
                output_file.write("}")
                output_file.write(line)
                output_file.write("\n")
            else:
                # Get the line in a list form, to get the desired values.
                list_of_line_inputs = line.split(sep="\t")
                # Fetching values
                column_name = list_of_line_inputs[0]
                data_type = list_of_line_inputs[1].split("\n")[0]
                # Writing
                output_file.write(f"    '{column_name}': '{data_type}',\n")


def characterize_dfs(*list_dfs) -> None:
    """
    Showing df characteristics.

    Arguments:
        list_dfs -- list of Pandas df objects.
    """
    print("--" * 40, "\nINFORMATION ABOUT ALL DATAFRAMES", "\n")
    for df in list_dfs:
        print("-" * 5, "NAME OF DF ", df.name, "-" * 5, "\n")
        print(df.info())
    print("\n", "TOTAL DATAFRAMES: ", len(list_dfs))


def create_df_dictionary_using_name(*listdfs) -> dict:
    """
    Create a dictionary of dataframes using the name of the dataframe as key.

    Returns:
        Dictionary object.
    """
    df_dictionary = {df.name: df for df in listdfs}
    return df_dictionary


def cast_to_int(number) -> int:
    try:
        result = float(number)
        result = int(result)
        # print(result)
    except Exception:
        print(f"This value {number} cannot be casted to int. Continue...")
        logging.debug("Value cannot be casted")
        return number
    return result
