import csv
from datetime import datetime

def export_to_csv(history):
    filename = f"Clipboard_History_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Timestamp', 'Token Count', 'Character Count', 'Content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for record in history:
            writer.writerow(record)

    return filename
