# your code goes here
line = input()
line_arr = line.split(",")

def your_answer(w, c):
    new_w = w.replace(c, '')

    return new_w

print(your_answer(line_arr[0], line_arr[1].strip()))