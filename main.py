import os
from datetime import datetime

archive = "archive"

# get date and time
now = datetime.now()
d = now.strftime("%d/%m/%Y")

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

mode = int(input("What do you want to do?\n1.write goals\n2.read goals\n3.review goals\n"))

for filename in os.listdir(archive):
    if filename != "eodt.txt":  # don't want to iterate trought eodt
        # open a file and print its name
        file = os.path.join(archive, filename)
        with open(file, "r") as f:
            name = f.readline()
            print("\n" + name.rstrip())
            f.close()

        # set goals
        if mode == 1:
            # print date
            print("Today is " + d + "\n")
            # add date to file
            with open(file, "a") as f:
                f.write("\n" + d + "\n")

                # set goals for the day
                print("What are today's goals? Input 0 when done.")
                goal = str(input())
                while goal != "0":
                    f.write("-" + goal + "\n")
                    goal = str(input())
            f.close()

        # read goals
        elif mode == 2:
            print_goals(file)

        # review goals
        else:
            print_goals(file, review=True)

# write eodt if in review mode
if mode == 3:
    with open("archive/eodt.txt", "a") as f:
        f.write("\n" + d + "\n")
        eodt = str(input("End of day thoughts:\n"))
        f.write(eodt + "\n")
        f.close()