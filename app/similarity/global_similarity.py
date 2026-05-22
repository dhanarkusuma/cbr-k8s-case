def global_similarity(case_input, stored_case):

    pod_similarity = (
        1 if case_input["pod_status"]
        == stored_case["pod_status"]
        else 0
    )

    cpu_similarity = numeric_similarity(
        case_input["cpu_usage"],
        stored_case["cpu_usage"]
    )

    memory_similarity = numeric_similarity(
        case_input["memory_usage"],
        stored_case["memory_usage"]
    )

    log_similarity = text_similarity(
        case_input["error_log"],
        stored_case["error_log"]
    )

    final_score = (
        (0.2 * pod_similarity) +
        (0.2 * cpu_similarity) +
        (0.2 * memory_similarity) +
        (0.4 * log_similarity)
    )

    return final_score
