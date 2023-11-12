# README
## Overview
This Python script, named 'lgl_interpreter.py', encompasses all the essential functions required for constructing our interpreter. The file 'example_operations.gsc' includes a straightforward program designed to demonstrate the exercise's functionalities. Additionally, 'example_class.gsc' provides a detailed implementation of our classes. The 'example_trace.gsc' file is dedicated to outlining the functions we aim to trace. Lastly, 'reporting.py' is tasked with collecting tracer results and presenting them in an organized, tabular format.

## Features

-Arithmetic Operations: Supports multiplication, division, and power operations.

-Control Structures: Includes print statements and while loops for flow control.

-Data Structures: Allows creation and manipulation of arrays and dictionaries, including array -value retrieval and assignment, dictionary creation and merging.

-Object-Oriented Programming: Supports class definition, object instantiation, single inheritance, and polymorphism.

-Tracing: Implements basic tracing functionalities for debugging and performance analysis.

## How to Run

### Running the Interpreter
To run the LGL interpreter with a specific .gsc file, use the following command:

python lgl_interpreter.py [filename].gsc

Example Files

example_operations.gsc: Demonstrates arithmetic operations, control structures, and data structures.

example_class.gsc: Showcases object-oriented features with a UML class diagram implementation.

example_trace.gsc: Used for tracing function calls.

### Tracing
To enable tracing, use the --trace argument:

python lgl_interpreter.py example_trace.gsc --trace trace_file.log

### Reporting
Run the reporting.py script to display tracing results in an aggregated format:

python reporting.py trace_file.log

## Description of the files
### 1. lgl_interpreter.py
Decorators and Tracing: The trace decorator function is used for logging the start and stop times of function calls into a CSV file.

Argument Parsing: Uses argparse to handle command-line arguments for running the interpreter.

JSON File Processing: Reads a JSON file representing a program and executes it.

Environment Handling: Manages variable scopes using a list of dictionaries (envs).

Function Definitions: Functions like do_funktion, do_method, do_aufrufen, etc., represent different operations in the language.

Operations Mapping: The OPERATIONS dictionary maps string operation names to their corresponding functions.

### 2. Example-Operation.gsc
Demonstrates a sequence of operations ("abfolge") including arithmetic operations, array and dictionary manipulations, and function calls.

### 3. Example-Class.gsc
Illustrates object-oriented programming features with classes like Shape, Square, Circle, and their methods for calculating areas and densities.

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

