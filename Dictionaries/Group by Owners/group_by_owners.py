def group_by_owners(files):
    result = {}
    for k, v in files.items():
        if v not in result:
            result[v] = [k]
        else:
            result[v].append(k)

    return result


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))
