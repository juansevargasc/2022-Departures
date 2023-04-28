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
