import file_handling

GENRE_INDEX = 3
LENGTH_INDEX = 4
TITLE_INDEX = 1

def get_genre_stats():
    pass

def get_last_oldest():
    pass

def get_last_oldest_of_genre():
    pass

def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    list_of_albums_in_genre = []
    for album in albums:
        if album[GENRE_INDEX] == genre:
            list_of_albums_in_genre.append(album)
    if list_of_albums_in_genre == []:
        raise ValueError("Wrong genre")
    return list(list_of_albums_in_genre)


def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    max_length_of_album = max([float(album[LENGTH_INDEX].replace(":",".")) for album in albums])
    for album in albums:
        if max_length_of_album == float(album[LENGTH_INDEX].replace(":",".")):
            return album



def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    list_of_albums_length = []
    for album in albums:
        length_of_album = album[LENGTH_INDEX].split(":")
        minutes = float(length_of_album[0])
        seconds = float(length_of_album[1])/60
        length_of_album = minutes + seconds
        list_of_albums_length.append(length_of_album)    
    
    sum_of_lentgh = sum(list_of_albums_length)
    return round(sum_of_lentgh,2)



