# data from the previous exercise
Artist = "One Direction"
Genre = "Pop"
Year = 2012

def ArtistName():
    return Artist


def MusicGenre():
    return Genre


def YearOfRelease():
    return Year

def TypeOfGenre():
    if(Genre == "Pop"):
        return True
    else:
        return False

print(ArtistName())
print(MusicGenre())   
print(YearOfRelease())
print(TypeOfGenre())


