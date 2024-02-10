import csv
from datetime import datetime
import logging

logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')

def processData(file_path):
    data = {}

    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            try:
                datetime.strptime(row['birthday'], '%d/%m/%Y')
                data[row['id']] = row
            except ValueError as e:
                logging.error(f"Error processing for ID #{id}")
                
    return data

def displayPerson(data, person_id):
    return data.get(person_id, "Invalid ID.")

def main():
    file_path = 'birthdays100.csv'
    data = processData(file_path)
    
    while True:
        person_id = input("Enter a ID: ")
        if person_id.lower() == 'exit':
            break
        print(displayPerson(data, person_id))

if __name__ == "__main__":
    main()