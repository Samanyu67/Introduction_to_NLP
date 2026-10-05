# 1) Import needed libraries (requests + your API key from config)

# 2) Set model ID, API URL, headers (Authorization), and the TOPICS list

# 3) Function: ask_hf(headline)
#    - Create payload with "inputs" and "candidate_labels"
#    - Send POST request
#    - If request fails, raise a friendly error
#    - Return the JSON response

# 4) Function: best_topic(preds)
#    - Find the prediction with the highest score
#    - Return best label + best score

# 5) Function: bar(score)
#    - Convert score to a simple 10-block bar (█/░)
#    - Return the bar string

# 6) Function: show(headline, preds)
#    - Print headline
#    - Print best topic + confidence %
#    - Print Top 3 guesses with bars

# 7) Function: main()
#    - Print welcome message + available topics
#    - Loop:
#       - Take headline input
#       - If "exit", stop
#       - If empty, ask again
#       - Call ask_hf()
#       - Show results (and handle unexpected response)

# 8) Run main() only when this file is executed directly
