import re

def song_decoder(string):
    no_wub = string.replace("WUB", " ")
    return re.sub(' +', ' ', no_wub).strip()
