import os
INPUT_DIR = "data/inputs"
INTERMEDIATE_DIR = "data/intermediate"
OUTPUTS_DIR = "data/outputs"

def get_paths(vhdl_name, sim_name):
    return {
        "input_vhdl_file": f"{INPUT_DIR}/{vhdl_name}.vhdl",
        "input_simulation_vectors": f"{INPUT_DIR}/{sim_name}.txt",
        "json_file": f"{INTERMEDIATE_DIR}/{vhdl_name}.json",
        "slc_file": f"{INTERMEDIATE_DIR}/{vhdl_name}_slc.txt",
        "output_simulation_vectors": f"{OUTPUTS_DIR}/{vhdl_name}_outputs.txt",
    }
