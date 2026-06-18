numbers = [1, 2, 3, 4, 5, 3, 2]
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)

unique_numbers.add(6)
print("After adding 6:", unique_numbers)


unique_numbers.remove(2)
print("After removing 2:", unique_numbers)


other_set = {3, 4, 7}


print("Union:", unique_numbers | other_set)
print("Intersection:", unique_numbers & other_set)
print("Difference:", unique_numbers - other_set)



library = {}


def add_book(title, author, year, genre):
    library[title] = {"author": author, "year": year, "genre": genre}


def remove_book(title):
    if title in library:
        del library[title]


def search_books(keyword):
    results = []
    for title, info in library.items():
        if keyword.lower() in title.lower() or keyword.lower() in info["author"].lower() or keyword.lower() in info["genre"].lower():
            results.append((title, info))
    return results


def display_books(sort_by="title"):
    if sort_by == "title":
        sorted_books = sorted(library.items(), key=lambda x: x[0])
    else:
        sorted_books = sorted(library.items(), key=lambda x: x[1]["author"])
    for title, info in sorted_books:
        print(f"{title} - {info['author']} ({info['year']}) [{info['genre']}]")



add_book("Book A", "Author X", 2000, "Fiction")
add_book("Book B", "Author Y", 2010, "Science")
add_book("Book C", "Author Z", 1995, "History")

print("\nAll books sorted by title:")
display_books("title")

print("\nSearch for 'Author Y':")
print(search_books("Author Y"))

remove_book("Book B")

print("\nAll books sorted by author:")
display_books("author")