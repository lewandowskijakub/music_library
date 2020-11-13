"""
The main program should use functions from music_reports and display modules
"""
import display
import music_reports
import file_handling

def get_file():
    return file_handling.import_data()

def get_option():
    while True:
        user_option = input("\nProvide option you want to choose: \n")
        if user_option == "0" or user_option == "1" or user_option == "2" or user_option == "3":
            return user_option

def get_genre():
    return input("\nPlease provide genre: \n")

def do_option(user_option, albums):
    if user_option == "1":
        genre = get_genre()
        try:
            by_genre = music_reports.get_albums_by_genre(albums,genre)
            display.print_albums_list(by_genre)
            while True:
                try:
                    way_of_export = input("\nProvide mode a or w: \n")
                    file_handling.export_data(by_genre, "albums_kuba.txt", way_of_export)
                    break
                except ValueError:
                    display.print_command_result("Wrond mode!")
        except ValueError:
            display.print_command_result("There is no genre like yours!")


    if user_option == "2":
        longest_album = music_reports.get_longest_album(albums)
        display.print_command_result("The longest album is: ")
        display.print_album_info(longest_album)

    if user_option == "3":
        total_albums_length = music_reports.get_total_albums_length(albums)
        display.print_command_result(f"Total length of albums is: {total_albums_length}.")

def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    options = ["Exit","Get albums of chosen genre", "Get longest album", "Get total albums length"]
    display.print_program_menu(options)
    albums = get_file()
    user_option = None
    while user_option != "0":
        user_option = get_option()
        do_option(user_option, albums)
    display.print_command_result("That's everything, thank you!")



if __name__ == '__main__':
    main()
