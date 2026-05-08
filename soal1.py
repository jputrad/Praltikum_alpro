d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print(f"{'key':<8} {'value':<8} {'item'}")
print("-" * 28)
for key, value in d.items():
    print(f"{key:<8} {value:<8} {key}")