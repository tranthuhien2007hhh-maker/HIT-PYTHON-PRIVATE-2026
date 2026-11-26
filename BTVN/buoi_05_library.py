class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self._is_borrowed=False
        self._history=[]
        
    @property
    def is_borrowed(self) -> bool:
        return self._is_borrowed
    
    @property
    def history(self) -> list:
        return list(self._history)

    def borrow(self) -> bool:
        if self._is_borrowed:
            return False
        self._is_borrowed=True
        self._history.append("borrow")
        return True

    def return_book(self) -> bool:
        if not self._is_borrowed:
            return False
        self._is_borrowed=False
        self._history.append("return")
        return True
    
a =Book("Python cơ bản", "Linh")
b =Book("Git thực hành", "Hà")
print(f"{a.title} - {a.author}")
print(f"{b.title} - {b.author}")    
print()
print(f"a.borrow(): {a.borrow()}")
print(f"a.borrow(): {a.borrow()}")
print(f"b.is_borrowed: {b.is_borrowed}")
print(f"a.return_book(): {a.return_book()}")
print(f"a.is_borrowed: {a.is_borrowed}")
print(f"a.return_book(): {a.return_book()}")
print()
print(f"Lịch sử của a: {a.history}")
print(f"Lịch sử của b: {b.history}")  