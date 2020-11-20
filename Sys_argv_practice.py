import sys
import os

os.system("cls||clear")

export_file_index = 1
type_of_file_index = 2

def export_file(list_of_content, filename, type_of_file):
    if type_of_file != "a" and type_of_file != "w":
        raise ValueError("Wrong Mode")
    else:
        with open(filename, type_of_file) as file_to_write:
            for content in list_of_content:
                content = content.replace(" "," | ")
                file_to_write.write(content + "\n")

        
def main():
    my_args = sys.argv
    if len(my_args) >= 2:
        file_name = my_args[export_file_index]
        type_of_file = my_args[type_of_file_index]
        # print(type_of_file)
        list_of_content = [argument for argument in my_args[(type_of_file_index + 1):]]
        # print(list_of_content)
        try:
            export_file(list_of_content, file_name, type_of_file)
        except ValueError as error:
            print(error)
    

if __name__ == "__main__":
    main()