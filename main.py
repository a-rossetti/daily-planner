import os
from datetime import datetime

archive = "archive"

# get date and time
now = datetime.now()
d = now.strftime("%d/%m/%Y")

def write_goals(filename):
    # print date
    print("Today is " + d + "\n")
    # add date to file
    with open(filename, "a") as f:
        f.write("\n" + d + "\n")

        # write goals for the day
        print("What are today's goals? Input 0 when done.")
        goal = str(input())
        while goal != "0":
            f.write("-" + goal + "\n")
            goal = str(input())
    f.close()

def print_goals(filename, review=False):
    i = -1  # to get proper index of line
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            i += 1
            l = line.rstrip()
            if l == d:
                for line1 in lines[lines.index(line, i) + 1:]:
                    if line1 == "\n":
                        break
                    else:
                        print(lines[lines.index(line1, i)].rstrip())
                        if review:
                            # asking whether the goal was achieved
                            c = str(input("Did you succesfully complete this task? (y/n): "))
                            if c == "y":
                                lines[lines.index(line1, i)] = lines[lines.index(line1, i)].rstrip() + "  :)\n"
                            else:
                                lines[lines.index(line1, i)] = lines[lines.index(line1, i)].rstrip() + "  :(\n"
    f.close()
    with open(filename, "w") as f:
        for line in lines:
            f.writelines(line)
    f.close()

def print_review_check(review=False):
    with open("archive/simple-full.txt", "r") as f:
        # getting last date on file
        for line in f:
            pass
        last_date = line
        if last_date == d:
            with open("archive/sdp.txt", "r") as f:
                name = f.readline()
                print("\n" + name.rstrip())
                f.close()

            print_goals("archive/sdp.txt", review)
        else:
            for filename in os.listdir(archive):
                if filename != "eodt.txt" and filename != "sdp.txt" and filename != "simple-full.txt":
                    # open a file and print its name
                    file = os.path.join(archive, filename)
                    with open(file, "r") as f:
                        name = f.readline()
                        print("\n" + name.rstrip())
                        f.close()

                    print_goals(file, review)


mode = int(input("What do you want to do?\n1.write goals\n2.read goals\n3.review goals\n"))

# write goals
if mode == 1:
    # choosing daily planner to write goals
    dp = int(input("Which daily planner do you want to use?\n1.full daily planner\n2.simple daily planner\n"))
    # full daily planner
    if dp == 1:
        for filename in os.listdir(archive):
            if filename != "eodt.txt" and filename != "sdp.txt" and filename != "simple-full.txt":
                # open a file and print its name
                file = os.path.join(archive, filename)
                with open(file, "r") as f:
                    name = f.readline()
                    print("\n" + name.rstrip())
                    f.close()

                write_goals(file)

    # simple daily planner
    if dp == 2:
        with open("archive/sdp.txt", "r") as f:
            name = f.readline()
            print("\n" + name.rstrip())
            f.close()

        write_goals("archive/sdp.txt")

        # save date in simple-full.txt to remember which planner was used
        with open("archive/simple-full.txt", "a") as f:
            f.write("\n" + d)

# read goals
if mode == 2:
    # checking which daily planner has been used and printing goals
    print_review_check()
    
# review goals
if mode == 3:
    print_review_check(True)

    # write eodt
    with open("archive/eodt.txt", "a") as f:
        f.write("\n" + d + "\n")
        eodt = str(input("\n\nEnd of day thoughts:\n"))
        f.write(eodt + "\n")
        f.close()


# if saved as executable, it won't close immediately after it runs
input("\n\nPress Enter to close the program...")
