print("=== 1. BOOK LIST OPERATIONS ===")
books = [
    "To Kill a Mockingbird",
    "1984",
    "The Great Gatsby",
    "Pride and Prejudice",
]
print(f"Initial Books: {books}")

books.append("The Catcher in the Rye")
print(f"After Adding a Book: {books}")

books.remove("1984")
print(f"After Removing '1984': {books}")

books.sort()
print(f"Sorted Books: {books}")

books.reverse()
print(f"Reversed List: {books}")

print(f"First Book (Indexing): {books[0]}")
print(f"First Two Books (Slicing): {books[:2]}")
print("-" * 40)


print("\n=== 2. LIBRARIAN DETAILS DICTIONARY ===")
librarian = {
    "name": "Sarah Connor",
    "employee_id": "LIB-1042",
    "shift": "Morning",
    "department": "Main Fiction",
}
print(f"Librarian Details: {librarian}")

print(f"Librarian Name: {librarian['name']}")

librarian["shift"] = "Evening" 
librarian["years_experience"] = 5  
print(f"Updated Librarian Details: {librarian}")
print("-" * 40)


print("\n=== 3. BOOK DIRECTORY CREATION ===")
book_titles = [
    "The Great Gatsby",
    "To Kill a Mockingbird",
    "Pride and Prejudice",
    "Moby Dick",
]
book_ids = ["BK-001", "BK-002", "BK-003", "BK-004"]

book_directory = dict(zip(book_ids, book_titles))

print("Book Directory (ID: Title):")
for book_id, title in book_directory.items():
    print(f"  {book_id} -> {title}")