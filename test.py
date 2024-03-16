from core.apps.nlp_engine.utils import preprocess_text


problems = {
    'engin': 'Is the engine making a strange noise? (yes/no)',
    'chassi': 'Are there any visible damages to the chassis? (yes/no)',
    'tire': 'Are the tires worn out or deflated? (yes/no)',
}

follow_ups = {
    'engine_noise': 'We suggest checking the engine oil level and bringing your car to a mechanic.',
    'engine_light': 'Please check the engine control system with a diagnostic tool.',
    'chassis_damage': 'A damaged chassis can affect vehicle safety. Have it inspected by a professional.',
    'tires_condition': 'Consider replacing your tires or inflating them to the correct pressure.',
}


def simple_chat(preprocessed_tokens, state):
    print(f"Debug: Preprocessed tokens are {preprocessed_tokens}")
    if state:
        if 'yes' in preprocessed_tokens:
            follow_up_response = follow_ups[f"{state}_noise"] if 'noise' in state else follow_ups[state]
            return follow_up_response, None
        elif 'no' in preprocessed_tokens:
            return "Could you provide more details about the problem?", state
        else:
            return "Please answer yes or no.", state

    for problem, message in problems.items():
        if problem in preprocessed_tokens:
            return message, problem
    
    return "I'm sorry, I can only help with engine, chassis, or tires issues. Please specify one of these.", None

if __name__ == "__main__":
    print("Welcome to AutoAssist. Type 'quit' to exit.")
    state = None

    while True:
        user_input = input("Please describe your problem with engine, chassis, or tires.\n> " if not state else "> ")
        if user_input.lower() == 'quit':
            break

        preprocessed_input = preprocess_text(user_input)

        response, new_state = simple_chat(preprocessed_input, state)
        print(response)

        if not state and new_state:
            state = new_state

        elif state:
            if 'yes' in preprocessed_input or 'no' in preprocessed_input:
                state = None
