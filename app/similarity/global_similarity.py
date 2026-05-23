from similarity import (
    numeric,
    text
)


def calculate_similarity(
    query_case,
    stored_case
):

    pod_similarity = (
        1
        if query_case["pod_status"]
        == stored_case.pod_status
        else 0
    )

    cpu_similarity = numeric.numeric_similarity(
        query_case["cpu_usage"],
        stored_case.cpu_usage
    )

    memory_similarity = numeric.numeric_similarity(
        query_case["memory_usage"],
        stored_case.memory_usage
    )

    log_similarity = text.text_similarity(
        query_case["error_log"],
        stored_case.error_log
    )

    final_score = (
        (0.2 * pod_similarity) +
        (0.2 * cpu_similarity) +
        (0.2 * memory_similarity) +
        (0.4 * log_similarity)
    )

    return round(final_score, 4)