def retrieve_top_k(query_case, stored_cases, k=3):

    scored_cases = []

    for case in stored_cases:

        similarity = global_similarity(
            query_case,
            case
        )

        scored_cases.append({
            "case": case,
            "similarity": similarity
        })

    scored_cases.sort(
        key=lambda x: x["similarity"],
        reverse=True
    )

    return scored_cases[:k]
