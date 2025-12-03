import pandas
import random

# ============================================
# CONFIGURATION - Change these variables
# Both the sentence elements and the state transitions are saved as CSV files to make this code more readable.
# The number of sentences and max elements per per sentence can be set as you like.
# The variables are written in capital letters to indicate that they are going to stay the same all over the program.
# TODO 1. Fill in the path to the data file and transitions file
# TODO 2. Set the number of sentences and max element per sentence to a value that makes sense to you.
# ============================================
DATA_FILE = ''                        # Your data CSV file
TRANSITIONS_FILE = ''                 # Transition probabilities CSV file
NUM_SENTENCES = 0                     # How many sentences to generate
MAX_ELEMENTS = 0                      # Maximum words per sentence

# TODO 3. To test, print the content for each file to your console.

# ============================================
# Load word data from CSV
# ============================================
def load_word_data(filename):
    # Initialise the dictionary so we can return it later.
    dict = {}
    # Read the CSV file
    # TODO 4. Check the code from the exercise we did and complete this function
    # Because it is a function, use the variable "filename" from the function arguments above. The function will later be called with the file we'd like to load.
    # with open ...
        # Read the CSV
        # dataframe = 
        # Turn the dataframe into a dictionary (needed for the exercise, just uncomment the following line)
        # dict = dataframe.to_dict(orient="dict")

    # Print how many words we loaded
    # TODO 5. To check how many words were loaded, just uncomment the following:
    # for category, words in dict.items():
        # print(f"Loaded {len(words)} {category}(s)")
    
    # TODO 6. return the dict

# ============================================
# Load transition probabilities from CSV
# ============================================
def load_transitions(filename):
    # TODO 7. Read this carefully and add comments explaining what it does at every #
    # It's a bit too complex to write ourselves, so we'll just try to understand it.

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
# Choose the next state based on probabilities
# ============================================
def get_next_state(current_state, transitions):
    # If we don't have transitions for this state, end the sentence
    # TODO: 8. Check if the current state is part of the set of transitions.
    # Hint: you can check if something is in or not in a list or dict with "in" or "not in"
        # return the end state (check the transitions file to see what word is used for it)
        
    
    # Get all possible next states and their probabilities
    possible_transitions = transitions[current_state]
    states = [t[0] for t in possible_transitions]
    probabilities = [t[1] for t in possible_transitions]
    
    # Choose one randomly based on the probabilities
    # TODO: 9. Choose a random state based on the probabilities.
    # Read up online on random.choices. The probabilities are the weights.
    # You have to pick the content of the list by accessing that element
    

# ============================================
# Get a random word from a category
# ============================================
def get_random_word(category, data):
    # TODO: 10. Add comments to this to explain what all of it does
    #
    if category in data and data[category]:
        #
        return random.choice(data[category])
    #
    return ""

# ============================================
# Generate a single sentence
# ============================================
def generate_sentence(data, transitions, max_elements):
    # TODO: 11. Initialise the sentence parts as a list
    sentence_parts = []
    # TODO: 12. Set the current state to the starting state. Check the state transitions file to check what state that is.
    
    
    # Keep adding words until we reach max elements or END
    # TODO: 13. Add more words until "max_elements" is reached. Iterate over the range of max_elements with a for loop.
    
        # TODO: 14. Get the next state (there is a function for that above)
        
        
        # If we should end, stop adding words
        # TODO: 15. If the next state is to end, then don't add any more works. You can stop an iteration by calling "break"
        
        
        
        # Get a random word from this category
        # TODO: 16. Get a random state by calling the corresponding function and save it in the variable "word"
        
        # TODO: 17. Check if "word" actually exists and isn't an empty string (as a safety measure, so we don't get into any trouble)
        # TODO: 18. If true, add the "word" to the sentence parts (we've used this with lists) and move to the next state
        # TODO: 19. If false, break
        
        
        
        
    
    # If we have no words, return empty
    if not sentence_parts:
        return ""
    
    # Capitalize first letter and add period
    sentence = ' '.join(sentence_parts)
    sentence = sentence[0].upper() + sentence[1:] + '.'
    return sentence

# ============================================
# Main program
# ============================================

# Load the data and transitions
# TODO: 20. Call the function that loads the data and pass it the file with the data
word_data = ''
# TODO: 21. Call the function that loads the transitions and pass it the file with the transitions
transition_probs = ''

# Generate sentences
print(f"\n{'='*60}")
print(f"Generating {NUM_SENTENCES} sentences:")
print(f"{'='*60}\n")

# TODO: 22. Iterate over the NUM_SENTENCES with for
    # TODO: 23. Call the function that geneartes a sentence and pass it the necessary arguments

    # Print the sentences.
    # if sentence:
        # print(f"{i+1}. {sentence}")