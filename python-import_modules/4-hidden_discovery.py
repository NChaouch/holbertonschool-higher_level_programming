#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # Get all module attributes
    attributes_names = dir(hidden_4)

    # Filter and sort names
    for name in sorted(attributes_names):
        if not name.startswith("__"):
            print(name)
