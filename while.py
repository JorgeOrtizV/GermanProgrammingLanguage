import sys
def run_script(input_data):
    # Check if the input data format is correct
    if len(input_data) < 5:
        print("Invalid input: Not enough arguments provided.")
        return
    
    # Unpack the input data, allowing for an optional list of libraries at the end
    loop_type, var_names, initial_state, condition_str, body_str, *libs = input_data

    # Import required libraries
    for lib in libs:
        try:
            globals()[lib] = __import__(lib)
        except ImportError as e:
            print(f"Error importing {lib}: {e}. Make sure the library exists and is spelled correctly.")
            return

    # Split the variable names and initial states into lists and convert states to integers
    try:
        variables = var_names.split(',')
        states = list(map(int, initial_state.split(',')))
    except ValueError as e:
        print(f"Invalid input: Error converting initial states to integers. {e}")
        return

    # Create a dictionary to hold the variables and their states
    state_dict = dict(zip(variables, states))

    # Define the condition function that can evaluate the condition string
    def condition(state_dict):
        try:
            return eval(condition_str, globals(), state_dict)
        except Exception as e:
            print(f"Error evaluating condition '{condition_str}': {e}")
            return False

    # Define the body function that can execute the body string
    def body(state_dict, body_str):
        try:
            exec(body_str, globals(), state_dict)
        except Exception as e:
            print(f"Error executing body '{body_str}': {e}")
            sys.exit("Terminating due to body execution error.")
        return state_dict

    # Recursive evaluate_while function
    def evaluate_while(condition, body, state_dict, body_str):
        try:
            if condition(state_dict):
                print(f"Current state: {state_dict}")
                new_state_dict = body(state_dict, body_str)
                evaluate_while(condition, body, new_state_dict, body_str)
            else:
                print("Exiting the while loop")
        except Exception as e:
            print(f"Error during loop execution: {e}")
            sys.exit("Terminating due to an error during loop execution.")

    # Start the evaluate_while loop
    evaluate_while(condition, body, state_dict, body_str)

# Example input with corrected initial values
#input_data = ["evaluate_while", "x,y", "10,0", "x>y", "x-=1; y+=1"]
#run_script(input_data)