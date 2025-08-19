from src import config, parse_gate_level, generate_slc, compiled_code_simulation

if __name__ == "__main__":
    vhdl_name = input("Enter the name of your VHDL file (without vhdl extension): ")
    sim_name = input("Enter the name of your simulation vectors file (without txt extension): ")

    # Get all paths from config
    paths = config.get_paths(vhdl_name, sim_name)
    
    # Parse the VHDL netlist to JSON
    parse_gate_level.parse_vhdl_netlist(paths["input_vhdl_file"], paths["json_file"])

    # Generate the simplified logic expression from the JSON netlist
    generate_slc.generate_expression(paths["json_file"], paths["slc_file"])

    # Process the files to simulate the logic circuit
    compiled_code_simulation.process_files(
        paths["slc_file"],
        paths["input_simulation_vectors"],
        paths["output_simulation_vectors"]
    )

    print("✅ Simulation completed successfully.")
    print(f"Results saved in {paths['output_simulation_vectors']}")
