import json
from datetime import datetime, timedelta

# Load data from JSON file
with open(r'C:\Users\abhil\OneDrive\Desktop\training-data-analysis\trainings.txt', 'r') as file:
    data = json.load(file)

# Task 1: Count each completed training
training_counts = {}
for person in data:
    completed_trainings = {}
    for completion in person['completions']:
        training_name = completion['name']
        completion_date = datetime.strptime(completion['timestamp'], "%m/%d/%Y")
        
        # Keep only the most recent completion of each training
        if training_name not in completed_trainings or completed_trainings[training_name] < completion_date:
            completed_trainings[training_name] = completion_date

    # Update counts for unique trainings
    for training_name in completed_trainings:
        training_counts[training_name] = training_counts.get(training_name, 0) + 1

# Write output for Task 1
with open(r'C:\Users\abhil\OneDrive\Desktop\training-data-analysis\output_requirement_1.json', 'w') as file:
    json.dump(training_counts, file, indent=4)

# Task 2: List people who completed specific trainings in the specified fiscal year
specified_trainings = ["Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"]
fiscal_year = 2024
fiscal_start = datetime(fiscal_year - 1, 7, 1)
fiscal_end = datetime(fiscal_year, 6, 30)

training_completions = {training: [] for training in specified_trainings}
for person in data:
    completed_trainings = {}
    for completion in person['completions']:
        training_name = completion['name']
        completion_date = datetime.strptime(completion['timestamp'], "%m/%d/%Y")
        
        # Keep only the most recent completion of each training
        if training_name not in completed_trainings or completed_trainings[training_name]['date'] < completion_date:
            completed_trainings[training_name] = {'date': completion_date, 'person': person['name']}
    
    # Check if the completion falls within the fiscal year
    for training_name, info in completed_trainings.items():
        if training_name in specified_trainings and fiscal_start <= info['date'] <= fiscal_end:
            training_completions[training_name].append(info['person'])

# Write output for Task 2
with open(r'C:\Users\abhil\OneDrive\Desktop\training-data-analysis\output_requirement_2.json', 'w') as file:
    json.dump(training_completions, file, indent=4)

# Task 3: Find people with expired or soon-to-expire trainings
specified_date = datetime(2023, 10, 1)
expires_within_one_month = specified_date + timedelta(days=30)

expired_or_expiring_trainings = {}
for person in data:
    person_expiring_trainings = []
    completed_trainings = {}
    
    for completion in person['completions']:
        training_name = completion['name']
        if completion['expires']:
            expiration_date = datetime.strptime(completion['expires'], "%m/%d/%Y")
            if training_name not in completed_trainings or completed_trainings[training_name] < expiration_date:
                completed_trainings[training_name] = expiration_date

    # Check if training is expired or expiring soon
    for training_name, expiration_date in completed_trainings.items():
        if expiration_date < specified_date:
            person_expiring_trainings.append({
                "training_name": training_name,
                "status": "expired"
            })
        elif specified_date <= expiration_date <= expires_within_one_month:
            person_expiring_trainings.append({
                "training_name": training_name,
                "status": "expires soon"
            })

    if person_expiring_trainings:
        expired_or_expiring_trainings[person['name']] = person_expiring_trainings

# Write output for Task 3
with open(r'C:\Users\abhil\OneDrive\Desktop\training-data-analysis\output_requirement_3.json', 'w') as file:
    json.dump(expired_or_expiring_trainings, file, indent=4)

print("All outputs generated.")
