num_of_steps = 3
report_template = (
    "Report\n"
    "We have made {total} observations from tossing a coin: "
    "{tails} of them were tails and {heads} of them were heads. "
    "The probabilities are {tail_fraction:.2f}% and {head_fraction:.2f}%, respectively. "
    f"Our forecast is that in the next {num_of_steps} observations we will have: "
    "{predict_tails} tails and {predict_heads} heads."
)
