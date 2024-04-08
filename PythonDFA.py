class DFA:
    def __init__(self, alphabet, states, start_state, accept_states, transitions):
        self.alphabet = alphabet
        self.states = states
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions

    def is_accepted(self, string):
        current_state = self.start_state
        for symbol in string:
            if (current_state, symbol) not in self.transitions:
                return False
            current_state = self.transitions[(current_state, symbol)]
        return current_state in self.accept_states
import json
def read_dfa_from_file(filename):
    with open(filename, 'r') as file:
        alphabet_line = file.readline().strip()
        alphabet = alphabet_line[1:-1].split(',')
        
        states_line = file.readline().strip()
        states = states_line[1:-1].split(',')
        
        start_state = file.readline().strip()
        
        accept_states_line = file.readline().strip()
        accept_states = accept_states_line[1:-1].split(',')
        
        transitions = {}
        for line in file:
            print("Transition line:", line.strip())
            parts = line.strip().split('->')
            if len(parts) != 2:
                print("Error: Invalid transition format:", line.strip())
                continue
            source_state, symbol = parts[0][1:-1].split(',')
            target_state = parts[1]
            transitions[(source_state, symbol)] = target_state
        return DFA(alphabet, states, start_state, accept_states, transitions)
    
def main():
    filename = input("Enter the DFA description file name: ").strip()
    dfa = read_dfa_from_file(filename)
    while True:
        string = input("Enter a string to test (press Enter to exit): ").strip()
        if not string:
            break
        if dfa.is_accepted(string):
            print("Accepted")
        else:
            print("Not accepted")

if __name__ == "__main__":
    main()