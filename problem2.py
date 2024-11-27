
book_records = []

while True:
    user_input = input("Enter book title and borrowing days in the format 'book title - days', or 'done' to finish: \n")
    if user_input.lower() == "done":
        break
    book_records.append(user_input)

book_borrow_data_dic = {}
all_titles = set()

for i in book_records:
    title , days = i.split(" - ")
    days = int(days)

    if title in book_borrow_data_dic:
        book_borrow_data_dic[title] += days
    else:
        book_borrow_data_dic[title] = days

    all_titles.add(title)


print("Total borrowing days for each book:", book_borrow_data_dic)
print("List of unique book titles:", all_titles)


most_borrowed_books = max(book_borrow_data_dic, key=book_borrow_data_dic.get)
print(f"The most borrowed book is '{most_borrowed_books}' with {book_borrow_data_dic[most_borrowed_books]} days.")

least_borrowed_books = min(book_borrow_data_dic, key=book_borrow_data_dic.get)
print(f"The least borrowed book is '{least_borrowed_books}' with {book_borrow_data_dic[least_borrowed_books]} days.")

average_borrowing_time = sum(book_borrow_data_dic.values()) / len(book_borrow_data_dic)
print(f"The average borrowing time for all books is: {average_borrowing_time:.2f} days.")

# book_borrow_data = {
#     "a": 3,
#     "b": 7,
#     "c": 5
# }

# [("a", 3), ("b", 7), ("c", 5)]

sorted_books = sorted(book_borrow_data_dic.items(), key=lambda x: x[1], reverse=True)
sorted_books_titles = [book[0] for book in sorted_books]
print("Books sorted by borrowing time (descending order):", sorted_books_titles)












