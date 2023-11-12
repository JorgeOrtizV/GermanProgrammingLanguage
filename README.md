# README
## Overview
This Python script, named `lgl_interpreter.py`, encompasses all the essential functions required for constructing our interpreter. The file `example_operations.gsc` includes a straightforward program designed to demonstrate the exercise's functionalities. Additionally, `example_class.gsc` provides a detailed implementation of our classes. The `example_trace.gsc` file is dedicated to outlining the functions we aim to trace. Lastly, `reporting.py` is tasked with collecting tracer results and presenting them in an organized, tabular format.

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

example_class.gsc: Showcases object-oriented features with a UML class diagram implementation.

example_trace.gsc: Used for tracing function calls.

### Tracing
To enable tracing, use the --trace argument:

```bash
python lgl_interpreter.py example_trace.gsc --trace trace_file.log
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

### 2. Example-Operation.gsc
Demonstrates a sequence of operations `abfolge` including arithmetic operations, array and dictionary manipulations, and function calls.

### 3. Example-Class.gsc
Illustrates object-oriented programming features with classes like `Shape, Square, Circle,` and their methods for calculating areas and densities.

### 4. Example-trace.gsc
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
4759150059520,do_power,start,2023-11-09 17:33:56.001394
4759150059520,do_power,stop,2023-11-09 17:33:56.002439
4759150572416,do_addieren,start,2023-11-09 17:33:56.003744
4759150572416,do_addieren,stop,2023-11-09 17:33:56.004753
3723568417920,do_power,start,2023-11-09 17:34:02.661994
3723568417920,do_power,stop,2023-11-09 17:34:02.661994
3723568695616,do_addieren,start,2023-11-09 17:34:02.661994

```




