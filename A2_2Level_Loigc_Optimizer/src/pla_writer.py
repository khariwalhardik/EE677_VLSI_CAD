from cube import Cube

def write_pla(filename: str, input_labels, output_labels, selected_cubes_per_output):
    """
    Write optimized cubes to a PLA file.

    Args:
        filename: path to output PLA file
        input_labels: list of input variable names
        output_labels: list of output variable names
        selected_cubes_per_output: list of sets of Cube objects for each output
    """
    num_inputs = len(input_labels)
    num_outputs = len(output_labels)

    with open(filename, "w") as f:
        # Write PLA headers
        f.write(f".i {num_inputs}\n")
        f.write(f".o {num_outputs}\n")
        f.write(".ilb " + " ".join(input_labels) + "\n")
        f.write(".ob " + " ".join(output_labels) + "\n")

        # Write cubes
        # For each output, create a line for each cube
        for out_idx, cubes in enumerate(selected_cubes_per_output):
            for cube in cubes:
                # Generate output pattern string
                output_pattern = ['0'] * num_outputs
                output_pattern[out_idx] = '1'
                line = cube.pattern + " " + "".join(output_pattern) + "\n"
                f.write(line)

        # End of PLA
        f.write(".e\n")


# --------------------------
# Quick Test
# --------------------------
if __name__ == "__main__":
    from cube import Cube

    # Example headers
    inputs = ['a', 'b', 'c']
    outputs = ['f']

    # Example selected prime cubes
    selected_cubes = [{Cube("11-"), Cube("1-1")}]

    # Write to output PLA
    write_pla("outputs/example1_optimized.pla", inputs, outputs, selected_cubes)
    print("Optimized PLA written to outputs/example1_optimized.pla")
