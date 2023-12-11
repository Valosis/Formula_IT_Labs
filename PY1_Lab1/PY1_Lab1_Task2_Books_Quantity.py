# Listing CONST values
FLOPPY_DISK_SPACE = 1.44 * 2**20
BOOK_PAGES = 100
PAGE_LINES = 50
LINE_SYMBOLS = 25
SYMBOL_SIZE = 4

bookSize = BOOK_PAGES * PAGE_LINES * LINE_SYMBOLS * SYMBOL_SIZE
booksQuantity = int(FLOPPY_DISK_SPACE//bookSize)

print("Количество книг, помещающихся на дискету:", booksQuantity)