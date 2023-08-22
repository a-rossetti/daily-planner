from utils.date_utils import get_current_date
from utils.error_handlers import handle_file_errors

class DiaryManager:
    def __init__(self, filename="archive/diary.txt"):
        self.filename = filename
        self.date = get_current_date()  # Assuming you have this function imported

    @handle_file_errors
    def write_entry(self):
        with open(self.filename, "a") as file:
            file.write("\n" + self.date + "\n")
            thoughts = str(input("\n\nWrite your thoughts here:\n"))
            file.write(thoughts + "\n")
