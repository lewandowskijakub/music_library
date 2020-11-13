def import_data(filename='albums_data.txt'):
    """
    Import data from a file to a list. Expected returned data format:
        ["David Bowie", "Low", "1977", "rock", "38:26"],
        ["Britney Spears", "Baby One More Time", "1999", "pop", "42:20"],
        ...]

    :param str filename: optional, name of the file to be imported

    :returns: list of lists representing albums' data
    :rtype: list
    """
    with open(filename,"r") as file_to_open:
        lines = file_to_open.readlines()
        list_of_lines = []
        for line in lines:
            line = line.replace("\n","").split(",")
            list_of_lines.append(line)
        return list_of_lines


def export_data(albums, filename='albums_data.txt', mode='a'):
    """
    Export data from a list to file. If called with mode 'w' it should overwrite
    data in file. If called with mode 'a' it should append data at the end.

    :param list albums: albums' data
    :param str filename: optional, name of file to export data to
    :param str mode: optional, file open mode with the same meaning as\
    file open modes used in Python. Possible values: only 'w' or 'a'

    :raises ValueError: if mode other than 'w' or 'a' was given. Error message:
        'Wrong write mode'
    """
    if mode != "a" and mode != "w":
        raise ValueError("Wrong write mode")
    else:
        with open(filename, mode) as file_to_write:
            for album in albums:
                file_to_write.write(",".join(album)+"\n")



