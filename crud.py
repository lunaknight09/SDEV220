#Nathan Hopkins
#Fast API assignment
#Feb 10, 2024

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database initialization
conn = sqlite3.connect('books.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              book_name TEXT,
              author TEXT,
              publisher TEXT)''')
conn.commit()

# Create
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    book_name = data.get('book_name')
    author = data.get('author')
    publisher = data.get('publisher')

    if not book_name or not author or not publisher:
        return jsonify({'error': 'Please provide all required fields (book_name, author, publisher)'}), 400

    c.execute('''INSERT INTO books (book_name, author, publisher)
                 VALUES (?, ?, ?)''', (book_name, author, publisher))
    conn.commit()

    return jsonify({'message': 'Book created successfully'}), 201

# Read
@app.route('/books', methods=['GET'])
def get_all_books():
    c.execute('''SELECT * FROM books''')
    books = c.fetchall()
    return jsonify({'books': books})

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    c.execute('''SELECT * FROM books WHERE id = ?''', (book_id,))
    book = c.fetchone()
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify({'book': book})

# Update
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book_name = data.get('book_name')
    author = data.get('author')
    publisher = data.get('publisher')

    if not book_name or not author or not publisher:
        return jsonify({'error': 'Please provide all required fields (book_name, author, publisher)'}), 400

    c.execute('''UPDATE books
                 SET book_name = ?, author = ?, publisher = ?
                 WHERE id = ?''', (book_name, author, publisher, book_id))
    conn.commit()

    return jsonify({'message': 'Book updated successfully'})

# Delete
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    c.execute('''DELETE FROM books WHERE id = ?''', (book_id,))
    conn.commit()
    return jsonify({'message': 'Book deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
    
    
#bug report 
#not running as the warning says development server and not to use in production deployment 
#says to use WSGI server instead and was confused on that part
#all other bugs were mispellings of message and successfully 