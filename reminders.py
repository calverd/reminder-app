tasks = []
task = input("What do you want to remember? ").strip()
if task == "":
    print("Nothing to save")
else:
    tasks.append(task)
print(f"Total tasks: {len(tasks)}")
print(tasks)
