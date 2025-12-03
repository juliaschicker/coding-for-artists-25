import pandas
import random

# ============================================
# CONFIGURATION
# 
# 
# 
# 
# 
# ============================================
DATA_FILE = 'markov_data.csv'           # 
TRANSITIONS_FILE = 'state_transitions.csv'  # 
NUM_SENTENCES = 10                    # 
MAX_ELEMENTS = 5                      # 

# TODO 3. To test, print the content for each file to your console.
print(DATA_FILE)
print(TRANSITIONS_FILE)

# ============================================
# 
# ============================================
def load_word_data(filename):
    # 
    dict = {}
    # 
    # 
    # 
    # 
    with open(filename, 'r', encoding='utf-8') as f:
        # 
        dataframe = pandas.read_csv(f)
        # 
        dict = dataframe.to_dict(orient="dict")
    
    # 
    # 
    for category, words in dict.items():
        print("Loaded {len(words)} {category}(s)")
    
    # 
    return dict

# ============================================
# 
# ============================================
def load_transitions(filename):
    # Dictionary to store transitions: state -> list of (next_state, probability)
    df = pandas.read_csv(filename, encoding='utf-8')

    #
    transitions = {}

    #
    for index, row in df.iterrows():
        current_state = row['from_state']
        next_state = row['to_state']
        probability = float(row['probability'])
        
        if current_state not in transitions:
            transitions[current_state] = []
        transitions[current_state].append((next_state, probability))

    return transitions

# ============================================
# 
# ============================================
def get_next_state(current_state, transitions):
    # 
    # 
    # 
    if current_state not in transitions:
        # 
        return 'END'
    
    # 
    possible_transitions = transitions[current_state]
    states = [t[0] for t in possible_transitions]
    probabilities = [t[1] for t in possible_transitions]
    
    # 
    # 
    # 
    # 
    return random.choices(states, weights=probabilities)[0]

# ============================================
# 
# ============================================
def get_random_word(category, data):
    # 
    #
    if category in data and data[category]:
        #
        return random.choice(data[category])
    #
    return ""

# ============================================
# 
# ============================================
def generate_sentence(data, transitions, max_elements):
    # 
    sentence_parts = []
    # 
    current_state = 'START'
    
    # 
    # 
    for index in range(max_elements):
        # 
        next_state = get_next_state(current_state, transitions)
        
        # 
        # 
        if next_state == 'END':
            break
        
        # 
        # 
        word = get_random_word(next_state, data)
        # 
        # 
        # 
        if word:
            sentence_parts.append(word)
            current_state = next_state
        else:
            break
    
    # 
    if not sentence_parts:
        return ""
    
    # 
    sentence = ' '.join(sentence_parts)
    sentence = sentence[0].upper() + sentence[1:] + '.'
    return sentence

# ============================================
# 
# ============================================

# 
# 
word_data = load_word_data(DATA_FILE)
# 
transition_probs = load_transitions(TRANSITIONS_FILE)

# 
print(f"\n{'='*60}")
print(f"Generating {NUM_SENTENCES} sentences:")
print(f"{'='*60}\n")

# 
for i in range(NUM_SENTENCES):
    # 
    sentence = generate_sentence(word_data, transition_probs, MAX_ELEMENTS)
    if sentence:
        print(f"{i+1}. {sentence}")