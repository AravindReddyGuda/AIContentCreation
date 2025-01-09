import csv
from datetime import datetime

def save_to_csv(topic: str, content: str):
    """
    Appends a row to a CSV file named with today's date, 
    containing a timestamp, topic, and the generated content.
    """
    filename = f"content_{datetime.now().strftime('%Y%m%d')}.csv"
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), topic, content])
