student = {}

#student['adrian'] = 15
student['paul'] = 21
student['adam'] = 16

if "adrian" in student:
    del student['adrian']
else:
    print("Adrian is not inside. Ignoring...")

print(student)

