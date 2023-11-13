# README
## Overview
This Python script, named `lgl_interpreter.py`, encompasses all the essential functions required for constructing our interpreter. The file `example_operations.gsc` includes a straightforward program designed to demonstrate the Task 1 functionalities, which cover basic arithmetic operations and creation of data structures as arraýs and dictionaries. Additionally, `example-class.gsc` provides a detailed program to implement clases and create instances, which support inheritance and polymorphism. The `example-trace.gsc` file is a sample program used to test the logging capabilites. Lastly, `reporting.py` is tasked with collecting tracer results and presenting them in an organized, tabular format.

## Features

-Arithmetic Operations: Supports multiplication, division, and power operations.

-Control Structures: Includes print statements and while loops for flow control.

-Data Structures: Allows creation and manipulation of arrays and dictionaries, including array value retrieval and assignment, dictionary creation and merging.

-Object-Oriented Programming: Supports class definition, object instantiation, single inheritance, and polymorphism.

-Tracing: Implements basic tracing functionalities for debugging and performance analysis.

## How to Run

### Running the Interpreter
To run the LGL interpreter with a specific .gsc file, use the following command:

```bash
python lgl_interpreter.py [filename].gsc
```
Example Files

example_operations.gsc: Demonstrates arithmetic operations, control structures, and data structures.

example-class.gsc: Showcases object-oriented features with a UML class diagram implementation.

example-trace.gsc: Used for tracing function calls.

### Tracing
To enable tracing, use the --trace argument:

```bash
python lgl_interpreter.py example_trace.gsc --trace trace_file.log
```

### Extended output
The user will only see as a feedback what he/she asks the interpreter to print, as it works in python, so if the instruction file (.gsc file) doesn't have any prints, the user won't see any output value
To see a detailed information of the program flow, the user can give the optional --verbose flag.

```bash
python lgl_interpreter.py example_trace.gsc --verbose
```

Sample output without verbose:
```bash
PS C:\UZH\SoftwareConstruction\GermanProgrammingLanguage> python .\lgl_interpreter.py .\example_operations.gsc --verbose
Operation 1 -> 4
Operation 2 -> 4.0
Operation 3 -> 9
30.0
Operation 4 -> None
Created instance myarray with value [None, None, None, None, None]
Operation 5 -> [None, None, None, None, None]
Operation 6 -> None
Operation 7 -> None
[None, None, None, 5, None]
Operation 8 -> None
Created instance mydict with value {'key1': 1, 'key2': 2}
Operation 9 -> {'key1': 1, 'key2': 2}
Operation 10 -> 1
Operation 11 -> None
{'key1': 1, 'key2': 20}
Operation 12 -> None
Created instance mydict2 with value {'key3': 5, 'key4': 6}
Operation 13 -> {'key3': 5, 'key4': 6}
Operation 14 -> {'key1': 1, 'key2': 20, 'key3': 5, 'key4': 6}
Created instance increase with value ['funktion', ['num'], ['addieren', ['abrufen', 'num'], 1]]
Operation 15 -> ['funktion', ['num'], ['addieren', ['abrufen', 'num'], 1]]
Created instance a with value 0
Operation 16 -> 0
Created instance a with value 1
Created instance a with value 2
Created instance a with value 3
Created instance a with value 4
Created instance a with value 5
Created instance a with value 6
Created instance a with value 7
Created instance a with value 8
Created instance a with value 9
Created instance a with value 10
Operation 17 -> None
Last result => None
```

Sample output without verbose:
```bash
PS C:\UZH\SoftwareConstruction\GermanProgrammingLanguage> python .\lgl_interpreter.py .\example_operations.gsc
30.0
[None, None, None, 5, None]
{'key1': 1, 'key2': 20}
```


### Reporting
Run the reporting.py script to display tracing results in an aggregated format:

```bash
python reporting.py trace_file.log
```

## Description of the files
### 1. lgl_interpreter.py
Decorators and Tracing: The trace decorator function is used for logging the start and stop times of function calls into a CSV file.
Argument Parsing: Uses argparse to handle command-line arguments for running the interpreter.
JSON File Processing: Reads a JSON file representing a program and executes it.
Environment Handling: Manages variable scopes using a list of dictionaries (envs).
Function Definitions: Functions like do_funktion, do_method, do_aufrufen, etc., represent different operations in the language.
Operations Mapping: The OPERATIONS dictionary maps string operation names to their corresponding functions.

### 2. example_operations.gsc
Demonstrates a sequence of operations `abfolge` including arithmetic operations, array and dictionary manipulations, and function calls.

### 3. example-Class.gsc
Illustrates object-oriented programming features with classes like `Shape, Square, Circle,` and their methods for calculating areas and densities.

### 4. example-trace.gsc
Contains a simple program using functions for calculating the sum of cubes.

### 5. reporting.py
A script for generating a report from a trace file.

Reads the trace file, calculates execution times, and prints a summary report.

## Highlighted Components:
Decorator for Tracing: A key feature for performance analysis.
JSON as Program Input: Unconventional choice, allowing for a structured yet flexible program definition.
Dynamic Environment Management: Enables scoping and variable tracking.
Extensive Set of Operations: Covers basic arithmetic, array and dictionary operations, and control structures like loops.
Object-Oriented Constructs: Demonstrates a basic form of object-oriented programming in a JSON-based language.
Performance Reporting: The reporting script is crucial for understanding the performance characteristics of the interpreter.

## Outputs

Sample output of reproting.py 
• The first column contains the name of the function
• The second column contains the number of calls of the function
• The third column contains the total execution time of the function, summed across all the executions
• The fourth column contains the average execution time, which is obtained by dividing the Total Time
with the Num. of calls

```bash
| Function Name | Num. of calls | Total Time (ms) | Average Time (ms) |
|---------------|---------------|-----------------|-------------------|
| do_addieren   | 39            | 38.219          | 0.980             |
| do_power      | 11            | 6.933           | 0.630             |
```

Sample output of trace.log

• The first column has a unique ID for distinguishing separate calls of the same function. 
• The second column shows the name of the function that was called. 
• The third column indicates the event type, specifying if the function has started (‘start’) or ended
(‘stop’). 
• The fourth column logs the timestamp of the event.

```bash
5549701017536,add_cubes,start,2023-11-13 22:50:21.605683
5549701291584,get_cube_power,start,2023-11-13 22:50:21.605683
5549701291584,get_cube_power,stop,2023-11-13 22:50:21.606683
5549701345280,get_cube_power,start,2023-11-13 22:50:21.606683
5549701345280,get_cube_power,stop,2023-11-13 22:50:21.606683
5549701017536,add_cubes,stop,2023-11-13 22:50:21.607682
```




