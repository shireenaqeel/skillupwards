#pip install fastapi uvicorn

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Sample dataset
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 3, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
]

# Pydantic model for Book
class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    year: int

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API. Use /docs to see available endpoints."}

# CREATE: Add a new book
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    book_dict = book.dict()
    book_dict["id"] = max(b["id"] for b in books) + 1
    books.append(book_dict)
    return book_dict

# READ: Get all books
@app.get("/books/", response_model=List[Book])
def read_books():
    return books

# READ: Get a specific book by ID
@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int):
    book = next((b for b in books if b["id"] == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# UPDATE: Update a book
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    book_index = next((i for i, b in enumerate(books) if b["id"] == book_id), None)
    if book_index is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    books[book_index].update(updated_book.dict(exclude_unset=True))
    books[book_index]["id"] = book_id
    return books[book_index]

# DELETE: Delete a book
@app.delete("/books/{book_id}", response_model=dict)
def delete_book(book_id: int):
    book_index = next((i for i, b in enumerate(books) if b["id"] == book_id), None)
    if book_index is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    deleted_book = books.pop(book_index)
    return {"message": f"Book '{deleted_book['title']}' has been deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)