# Training Data Analysis Application

This is a small console application written in Python that reads data from a JSON file (`trainings.txt`) and generates three JSON outputs based on different requirements related to training completions. The application processes information about trainings completed by various people, considering details such as the most recent completion date, fiscal year, and training expiration.

## How It Works

### Input
The application reads data from a file named `trainings.txt`, which contains a JSON object representing a list of individuals and the trainings they have completed. Each person has multiple trainings, each with a name, a completion date, and an expiration date.

### Outputs
The application generates the following three JSON outputs:

1. **Output 1 (`output_requirement_1.json`)**:
   - Lists each unique training and the count of people who have completed it.
   - **Logic**:
     - Iterate over each person in the input data.
     - Track the most recent completion of each training per person.
     - Increment the count for each training if it has been completed.

2. **Output 2 (`output_requirement_2.json`)**:
   - Given a list of specified trainings (`"Electrical Safety for Labs"`, `"X-Ray Safety"`, `"Laboratory Safety Training"`) and a fiscal year (`2024`), lists all people who completed those trainings in that fiscal year (from `July 1, 2023` to `June 30, 2024`).
   - **Logic**:
     - For each person, keep track of the most recent completion for each specified training.
     - Check if the completion falls within the specified fiscal year.
     - Append the person's name to the output if they completed the training within that fiscal year.

3. **Output 3 (`output_requirement_3.json`)**:
   - Given a date (`October 1, 2023`), finds all people with completed trainings that have expired or are expiring within one month from the given date.
   - **Logic**:
     - For each person, keep track of the most recent completion for each training.
     - Check if the expiration date is before or within one month after the given date.
     - Classify each training as `"expired"` or `"expires soon"` and include the person in the output.

### Code Walkthrough
The code follows these main steps to produce the outputs:

1. **Import Necessary Modules**:
   - `json` is used for loading and dumping JSON data.
   - `datetime` and `timedelta` from the `datetime` module are used to work with dates, comparing completion and expiration dates.

2. **Load Data from `trainings.txt`**:
   - The JSON file is loaded into a Python object (`data`), which contains a list of people and their training details.

3. **Task 1**: Count Each Completed Training
   - Use a dictionary to keep track of the most recent completion date for each training for each person.
   - Increment the training count if a training is found to be completed by a person.

4. **Task 2**: Identify People Who Completed Specific Trainings in a Fiscal Year
   - Use another dictionary to track the most recent completions of specified trainings for each person.
   - Check if the completion date falls within the fiscal year (`July 1, 2023` - `June 30, 2024`) and add the person's name to the corresponding training.

5. **Task 3**: Find People with Expired or Expiring Trainings
   - Use the specified date (`October 1, 2023`) and calculate a range of one month after this date.
   - Identify and classify trainings as `"expired"` or `"expires soon"` based on the expiration date for each person.

 
