from similarity import (
    global_similarity
)


def retrieve_top_k(
    query_case,
    candidate_cases,
    k=3
):

    scored_cases = []
    for case in candidate_cases:
        similarity = global_similarity.calculate_similarity(
            query_case,
            case
        )
        scored_cases.append({
            "similarity": similarity,
            "root_cause": case.root_cause,
            "solution": case.solution,
            "error_log": case.error_log,
        })

    scored_cases.sort(
        key=lambda x: x["similarity"],
        reverse=True
    )

    return scored_cases[:k]