# Bookstore - Django Query Optimization Examples

## Introduction

This repository contains examples of Django query optimization techniques. The examples are based on a simple bookstore application that has the following models:

- Author
- Book


## Installation

1. Clone the repository:

```bash
    git clone
```

2. Install the dependencies:

```bash
    python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && docker-compose up -d
```

3. Run the migrations:

```bash
    python manage.py migrate
```

4. Create a superuser:

```bash
    python manage.py createsuperuser
```

5. feed the database with some data:

```bash
    python manage.py generate_books_csv && python manage.py load_books_from_csv
```

## Commands to run analysis and see the results

1. Run the Django shell:

1 - A function that will print the book title and the author name (who wrote it) for all the books we have in the database

```bash
    python3 manage.py analyse_books show_book_and_author
```


2 - A function that will print the author’s name and all the books he wrote. For all the authors we have in the database. Like this

```bash
    python3 manage.py analyse_books list_all_authors_their_books
```


3 - Implementing a function, it should print the author’s name and the number of books he wrote. Order by the number of books written, descending.

```bash
    python3 manage.py analyse_books get_books_qty_for_each_author
```

