import utils
from sorts import bubble_sort, quicksort

bookshelf = utils.load_books('books_small.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()
long_bookshelf = utils.load_books('books_large.csv')

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])

sort_1 = bubble_sort(bookshelf, by_title_ascending)
for book in sort_1:
  print(book['title'])

sort_2 = bubble_sort(bookshelf_v1, by_author_ascending)
for book in sort_2:
  print(book['author'])

quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
book_2 = [book['author_lower'] for book in bookshelf_v2]
print(book_2)

# sort_3 = bubble_sort(long_bookshelf, by_total_length)

quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)
book_3 = [book['author_lower'] for book in long_bookshelf]
print(book_3)
