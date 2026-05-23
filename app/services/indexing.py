def build_index(cases):
    index = {}
    for case in cases:
        key = case.pod_status
        if key not in index:
            index[key] = []
        index[key].append(case)

    return index