from time import sleep
import trail

print("This is my file to demonstrate best practices.")

def process_data_1(data):
    trail.process_data();
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data

def read_data_from_web():
    print("Reading data from the Web")
    data = "Data from the web"
    return data

def write_data_to_database(data):
    print("Writing data to a database")
    print(data)

def main():
    data = read_data_from_web()
    modified_data = process_data_1(data)
    write_data_to_database(modified_data)

if __name__ == "__main__":
    main()