from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data
books = [
    {"title": "Book 1", "author": "Author 1"},
    {"title": "Book 2", "author": "Author 2"},
    {"title": "Book 3", "author": "Author 3"}
]

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    books.append({"title": title, "author": author})
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
