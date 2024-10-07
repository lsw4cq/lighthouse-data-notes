# Question 1 Tests


def test_add_book(add_book_function):
    """Tests the add_book function."""

    library = {}
    test_title = "The Hobbit"
    test_author = "J.R.R. Tolkien"
    test_year = 1937
    test_genres = ["Fantasy", "Adventure"]

    add_book_function(library, test_title, test_author, test_year, test_genres)

    assert test_title in library, "Test Failed: Book title not added."
    assert (
        library[test_title]["author"] == test_author
    ), "Test Failed: Author is incorrect."
    assert (
        library[test_title]["year"] == test_year
    ), "Test Failed: Publication year is incorrect."
    assert (
        test_genres == library[test_title]["genres"]
    ), "Test Failed: Genres are incorrect."

    print("Test Passed: Book added successfully with correct details.")


def test_filter_books_by_genre(filter_books_by_genre_function):
    """Tests the filter_books_by_genre function."""
    library = {
        "To Kill a Mockingbird": {
            "author": "Harper Lee",
            "year": 1960,
            "genres": ["Drama", "Fiction"],
        },
        "1984": {
            "author": "George Orwell",
            "year": 1949,
            "genres": ["Dystopian", "Political Fiction"],
        },
        "Brave New World": {
            "author": "Aldous Huxley",
            "year": 1932,
            "genres": ["Dystopian", "Science Fiction"],
        },
        "The Great Gatsby": {
            "author": "F. Scott Fitzgerald",
            "year": 1925,
            "genres": ["Novel", "Fiction"],
        },
        "The Catcher in the Rye": {
            "author": "J.D. Salinger",
            "year": 1951,
            "genres": ["Fiction", "Bildungsroman"],
        },
    }

    filtered_books_fiction = filter_books_by_genre_function(library, ["Fiction"])
    assert (
        len(filtered_books_fiction) == 3
    ), "Test Failed: Incorrect number of books returned for 'Fiction'."

    filtered_books_dystopian = filter_books_by_genre_function(
        library, ["Dystopian", "Novel"]
    )
    assert (
        len(filtered_books_dystopian) == 3
    ), "Test Failed: Incorrect number of books returned for 'Dystopian' and 'Novel'."

    filtered_books_bildungsroman = filter_books_by_genre_function(
        library, ["Bildungsroman"]
    )
    assert (
        len(filtered_books_bildungsroman) == 1
    ), "Test Failed: Incorrect number of books returned for 'Bildungsroman'."
    assert (
        "The Catcher in the Rye" in filtered_books_bildungsroman
    ), "Test Failed: 'The Catcher in the Rye' should be in the results for 'Bildungsroman'."

    filtered_books_horror = filter_books_by_genre_function(library, ["Horror"])
    assert (
        len(filtered_books_horror) == 0
    ), "Test Failed: Books returned for a genre not present."

    print("All tests passed successfully.")


def test_find_books_by_year(find_books_by_year):
    """Tests the find_books_by_year function"""

    library = {
        "To Kill a Mockingbird": {
            "author": "Harper Lee",
            "year": 1960,
            "genres": ["Drama", "Fiction"],
        },
        "1984": {
            "author": "George Orwell",
            "year": 1949,
            "genres": ["Dystopian", "Political Fiction"],
        },
        "Brave New World": {
            "author": "Aldous Huxley",
            "year": 1932,
            "genres": ["Dystopian", "Science Fiction"],
        },
        "The Great Gatsby": {
            "author": "F. Scott Fitzgerald",
            "year": 1925,
            "genres": ["Novel", "Fiction"],
        },
        "The Catcher in the Rye": {
            "author": "J.D. Salinger",
            "year": 1951,
            "genres": ["Fiction", "Bildungsroman"],
        },
    }

    books_1950_1960 = find_books_by_year(library, 1950, 1960)
    assert (
        len(books_1950_1960) == 2
    ), "Test Failed: Incorrect number of books returned for 1950 to 1960."
    assert (
        "To Kill a Mockingbird" in books_1950_1960
        and "The Catcher in the Rye" in books_1950_1960
    ), "Test Failed: Missing books from 1950 to 1960."

    books_1920_1940 = find_books_by_year(library, 1920, 1940)
    assert (
        len(books_1920_1940) == 2
    ), "Test Failed: Incorrect number of books returned for 1920 to 1940."
    assert (
        "The Great Gatsby" in books_1920_1940 and "Brave New World" in books_1920_1940
    ), "Test Failed: Missing books from 1920 to 1940."

    books_1980_2000 = find_books_by_year(library, 1980, 2000)
    assert (
        len(books_1980_2000) == 0
    ), "Test Failed: No books should be found from 1980 to 2000."

    print("All tests passed successfully.")
