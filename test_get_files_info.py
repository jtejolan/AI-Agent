from main import get_files_info

print("Running: get_files_info('calculator', '.')")
print(get_files_info("calculator", "."))
print()

print("Running: get_files_info('calculator', '/bin')")
print(get_files_info("calculator", "/bin"))
print()

print("Running: get_files_info('calculator', '../')")
print(get_files_info("calculator", "../"))
print()

print("Running: get_files_info('calculator', 'main.py')")
print(get_files_info("calculator", "main.py"))
