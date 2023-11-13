import argparse
import csv
from datetime import datetime
from tabulate import tabulate

# Parse command line arguments
parser = argparse.ArgumentParser(description='Generate report from trace file.')
parser.add_argument('trace_file', help='The trace file to generate report from.')
args = parser.parse_args()

# Read the trace file and aggregate data
trace_data = {}
with open(args.trace_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        call_id, func_name, event, timestamp = row
        timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
        
        if func_name not in trace_data:
            trace_data[func_name] = {'start': [], 'stop': [], 'total_time': 0}
        
        trace_data[func_name][event].append(timestamp)
        
        if event == 'stop':
            # Calculate the time difference between start and stop
            start_time = trace_data[func_name]['start'][-1]
            duration = (timestamp - start_time).total_seconds() * 1000  # Convert to milliseconds
            trace_data[func_name]['total_time'] += duration

# Calculate the number of calls and average time per function
report_data = []
for func_name, times in trace_data.items():
    num_calls = len(times['stop'])
    total_time = times['total_time']
    avg_time = total_time / num_calls if num_calls else 0
    report_data.append((func_name, num_calls, total_time, avg_time))

# Sort by function name for consistent reporting
report_data.sort(key=lambda x: x[0])

# Output the report
print(tabulate(report_data, headers=['Function Name', 'Num. of calls', 'Total Time (ms)', 'Average Time (ms)'], tablefmt='orgtbl'))