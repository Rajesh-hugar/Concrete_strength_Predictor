import csv
import sqlite3

def import_data(csv_file,data_base,table_name):
    # Connect to the database
    conn = sqlite3.connect(data_base)

    # Create a cursor
    c = conn.cursor()

    # Open the CSV file
    with open(csv_file, "r") as f:
        # Create a CSV reader
        reader = csv.reader(f)[1:]

        # Iterate over the rows of the CSV file
        for row in reader:
            # Insert the data into the table
            c.execute("INSERT INTO " + table_name + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", row)

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()
    
    
if __name__ == "__main__":
    csv_file = 'concrete_data.csv'
    data_base = 'Concrete_strength.db'
    table_name= 'Concrete'
    import_data(csv_file,data_base,table_name)