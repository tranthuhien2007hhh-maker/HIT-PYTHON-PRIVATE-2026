text = ("  Nguyễn   An  ","minh","   ")
def normalize_name(note):
        return " ".join(note.split())
for a in text:
    b=" ".join(a.split())
    print(f"{b}")
    