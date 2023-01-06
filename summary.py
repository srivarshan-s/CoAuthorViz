def stats(event_seq_dict):

    total_api_calls = 0
    num_gpt3_used = 0
    num_gpt3_not_satsfd = 0
    num_gpt3_mods = 0
    num_gpt3_non_mods = 0

    total_num_sent = event_seq_dict["num_sent"][-1]
    num_user_authored = 0
    num_gpt3_authored = 0
    num_prompt = event_seq_dict["num_sent"][0]

    for seq in event_seq_dict["sequence"]:

        if ("gpt3-call" not in seq) and ("empty-call" not in seq):
            num_user_authored += 1
        if ("gpt3-call" in seq) and ("user" not in seq):
            if ("prompt" not in seq) and ("modify-gpt3" not in seq):
                num_gpt3_authored += 1

        for event in seq:
            if event == "gpt3-call":
                num_gpt3_used += 1
            if event == "empty-call":
                num_gpt3_not_satsfd += 1
            if event == "modify-gpt3":
                num_gpt3_mods += 1

    total_api_calls = num_gpt3_not_satsfd + num_gpt3_used
    num_gpt3_non_mods = num_gpt3_used - num_gpt3_mods
    num_gpt3_auth_user_mod = total_num_sent - \
        num_gpt3_authored - num_gpt3_authored - num_prompt

    sentence_metrics = {
        "Total number of sentences": total_num_sent,
        "Number of sentences of initial prompt": num_prompt,
        "Number of sentences completely authored by the user": num_user_authored,
        "Number of sentences completely authored by GPT-3": num_gpt3_authored,
        "Number of sentences authored by GPT-3 with user modification": num_gpt3_auth_user_mod,
    }

    api_metrics = {
        "Total number of GPT-3 calls made": total_api_calls,
        "Number of times GPT-3 suggestion is used": num_gpt3_used,
        "Number of times user rejected GPT-3 suggestion": num_gpt3_not_satsfd,
        "Number of times GPT-3 suggestion is modified": num_gpt3_mods,
        "Number of times GPT-3 suggestion is used as is": num_gpt3_non_mods,
    }

    return sentence_metrics, api_metrics

def print_summary_stats(event_seq_dict):
    sentence_metrics, api_metrics = stats(event_seq_dict)
    print("SENTENCE LEVEL METRICS")
    for ele in sentence_metrics:
        print(ele, ":", sentence_metrics[ele])
    print()
    print("API LEVEL METRICS")
    for ele in api_metrics:
        print(ele, ":", api_metrics[ele])