x = {}
print(type(x))  # dict

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts)                # {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}
print(file_counts["txt"])         # 14
print("jpg" in file_counts)       # True
print("html" in file_counts)      # False

file_counts["cfg"] = 8            # Add new key-value pair
file_counts["csv"] = 17           # Update existing value
print(file_counts)                # {'jpg': 10, 'txt': 14, 'csv': 17, 'py': 23, 'cfg': 8}

del file_counts["cfg"]            # Delete a key-value pair
print(file_counts)                # {'jpg': 10, 'txt': 14, 'csv': 17, 'py': 23}
