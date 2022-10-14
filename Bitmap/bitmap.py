class Bitmap(object):
    def __init__(self, n_bits: int, word_size=16) -> None:
        self.n_bits = n_bits
        self.word_size = word_size
        self.n_words = (n_bits + self.word_size -1) / self.word_size
        self.masks = []
        self.n_set = 0

        # set masks to [1,2,4,8....32768] powers of 2
        bit = 1
        for i in range(self.word_size):
            self.masks.append(bit)
            bit <<= 1 

        # create the empty bitmap
        self.map = []

    def _position(self, which):
        # from which bit number, calculate the mask and word address
        which_bit = which % self.n_bits
        self.which_word = which_bit / self.word_size # converted this to int
        self.mask = self.masks[which_bit % self.word_size]

    def set_bit(self, which):
        # set bit "which" to 1
        self._position(which)
        mask = self.mask
        if not self.map[self.which_word] and mask:
            self.n_set += 1 # count bits actually set
            self.map[self.which_word] |= mask   # set bit to one

    def get_bit(self, which):
        # return True if bit "which" if set, else False
        self._position(which)
        return (self.map[self.which_word] & self.mask) != 0