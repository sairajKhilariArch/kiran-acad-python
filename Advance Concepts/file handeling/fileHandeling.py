# f = open("hi.txt", "r")

# for i in f:
#     print(i)

# f.close()
# print("--------------------------------------------")

# f = open("hi.txt", "r")
# lines = f.read()
# print(lines)
# f.close()

# print("---------------------read-----------------------")

# f = open("hi.txt", "r")
# readline = f.readline()
# print(readline)
# f.close()

# print("---------------------readline-----------------------")


# f = open("hi.txt", "r")
# all_lines = f.readlines()
# print(all_lines)
# f.close()

# print("----------------------readlines----------------------")


# f = open("hi.txt", "r")
# print(f.tell())

# d1 = f.read(3)
# print(f.tell())

# f.seek(0)
# print(f.tell())
# institute = f.readline()


# print(d1)
# print(institute)


# f = open("students.txt", "a")
# jj = input("what is your name")
# f.write(f"{jj}\n")
# f.close()

f = open("students.txt", "a")
jj = ["sairaj\n", "soham\n", "yash\n", "om\n"]
f.writelines(jj)
f.close()


print("done")
