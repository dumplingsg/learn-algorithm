# to draw a christmas tree

with open("Output.txt", "w") as file1:
    height = input("please input a number as height:")

    try:
        height = int(height)
    except ValueError:
        height = 20

    print((height * " ") + "?", file=file1)

    for i in range(1, height):
        print((height - i) * " " + (i * 2 + 1) * "*", file=file1)

    for i in range(height + 1, height + 8):
        print((height - 3) * " " + 7 * "*", file=file1)
