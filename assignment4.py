# Error Handling using:
'''
try:
    file = open("sample.txt",'r')
    print("Reading File Content:")
    read_file = file.read()
    print(read_file)
    file.close()
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")
'''


# Write & Append Data to a file:
'''
def write():
    write_input = input("Enter a text to the file: ")
    file = open("output.txt",'r+')
    write_file = file.write(write_input+"\n")
    print("Data successfully written to 'output.txt'.\n")
    file.close()

def append():
    append_input = input("Enter additional text to append: ")
    file = open("output.txt",'a')
    append_file = file.write(append_input+"\n")
    print("Data successfully appended.\n")
    file.close()

def read():
    file = open("output.txt",'r')
    print("Final Content of output.txt:")
    read_file = file.read()
    print(read_file)
    file.close()

writing = write()
adding = append()
reading = read()
'''