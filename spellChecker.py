from Bitmap.bitmap import Bitmap

if __name__ == '__main__':
    # on modern computers this can be as easy as reading the file
    # and storing each of the words in that file inside
    # a dictionary/hashmap(whatever you call it)
    # this makes for fast lookup times since dictionaries 
    # have O(1) lookup times
    with open('spell.words', 'r') as word_list:
        words = [word.strip() for word in word_list.readlines()]

        hash = {}
        for word in words:
            hash[word] = True

    # let us go back a few years ago to the 70's when we never had this power
    # enter the bitmap
    bitmap = Bitmap(64)
    bitmap.set_bit(0) # giving me errors(still WIP)

