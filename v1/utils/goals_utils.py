from utils.date_utils import get_current_date
from utils.error_handlers import handle_file_errors

class GoalsManager:
    def __init__(self, filename):
        self.filename = filename
        self.date = get_current_date()


    @handle_file_errors
    def write_goals(self):
        # append current date and today's goals to goals.txt
        with open(self.filename, "a") as file:
            file.write("\n" + self.date + "\n")

            print("What are today's goals? Enter your goals one by one. Press Enter on a blank line to finish.")
            goal = str(input())

            while goal:
                file.write("- " + goal + "\n")
                goal = str(input())


    @handle_file_errors
    def read_goals(self):
        # read today's goals from goals.txt
        with open(self.filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(f"Line: '{line}'")
            
            stripped_lines = [line.strip() for line in lines]
            if self.date in stripped_lines:
                start_index = stripped_lines.index(self.date) + 1
                for line in lines[start_index:]:
                    if line == "\n":
                        break
                    print(line.rstrip())


    @handle_file_errors
    def review_goals(self):
        # asking whether the goals were achieved
        with open(self.filename, "r") as file:
            lines = file.readlines()

            stripped_lines = [line.strip() for line in lines]
            if self.date in stripped_lines:
                start_index = stripped_lines.index(self.date) + 1
                current_index = start_index
                for line in lines[start_index:]:
                    if line == "\n":
                        break
                    print(line.rstrip())

                    print("Did you succesfully complete this task? (y/n): ")
                    yn = str(input())
                    if yn == "y":
                        lines[current_index] = line.rstrip() + "  :)\n"
                    else:
                        lines[current_index] = line.rstrip() + "  :(\n"
                    current_index += 1
        
        with open(self.filename, "w") as file:
            for line in lines:
                file.write(line)
