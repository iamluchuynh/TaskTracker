# Project TaskTracker

Project TaskTracker is a Python-based tool designed to manage and analyze tasks within a project. It offers functionalities to calculate completion rates, analyze task distributions, and determine average completion times.

## Features

- **Completion Rate Calculation**: Determines the percentage of completed tasks.
- **Task Distribution Analysis**: Provides insights into the number of tasks per category.
- **Average Completion Time Calculation**: Computes the average time taken to complete tasks.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/project-tasktracker.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd project-tasktracker
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Your Task Data**: Ensure your tasks are structured in a JSON format as follows:
   ```json
   [
       {
           "name": "Task 1",
           "category": "Development",
           "completed": true,
           "completion_time": 5
       },
       {
           "name": "Task 2",
           "category": "Testing",
           "completed": false,
           "completion_time": null
       }
       // Add more tasks as needed
   ]
   ```
2. **Run the Analysis**:
   ```bash
   python tracker.py path_to_your_task_data.json
   ```
3. **View Results**: The tool will output the completion rate, task distribution by category, and average completion time.

## Functions Overview

- `calculate_completion_rate(tasks)`: Calculates the percentage of completed tasks.
- `analyze_task_distribution(tasks)`: Analyzes and returns the number of tasks per category.
- `calculate_average_completion_time(tasks)`: Computes the average time taken to complete tasks.

## Contributing

We welcome contributions! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the contributors and the open-source community for their support.
