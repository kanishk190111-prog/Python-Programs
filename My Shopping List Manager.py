file_name = "shopping_list.txt"

initial_items = "apples\nbananas\nmilk\n"
with open(file_name, "w") as file:
    file.write(initial_items)

with open(file_name, "r") as file:
    complete_content = file.read()
    print(complete_content)

new_items = "bread\neggs\n"
with open(file_name, "a") as file:
    file.write(new_items)

with open(file_name, "r") as file:
    lines = file.readlines()
    for line in lines:
        print(f"Item: {line.strip()}")