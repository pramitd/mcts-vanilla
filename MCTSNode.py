from nodes_abc import AbstractNode

import numpy

class  MCTSNode (AbstractNode):

    def __init__(self,
                 state,
                 parent = None,
                 ):
        super().__init__(parent, state)

        self._visits = 0
        self._results = defaultdict(int)
        self._available_actions = None


    @property
    def N(self):
        return self._visits

    @property
    def Q(self):

        wins = self._results[self.parent.state.next_to_move]  # NOTE: Confusion Here Check Again
        losses  = self._results [ -1 * self.parent.state.next_to_move]
        return wins-losses
    
    @property
    def available_actions(self):

        if self._available_actions == None:
            self._available_actions = self.state.get_legal_actions()
        return self._available_actions


    def is_terminal():
        return self.state.is_game_over()

    def expand(self):

        new_action = self.available_actions.pop()  # remove an action from available actions from current node
        new_state = self.state.move(new_action) # Get the new game state caused by this action
        new_child = MCTSNode (parent = self, state = new_state) # Create a New Child with the new state and under the self parent
        self.children.append(new_child) # Add the new child node to the tree)

        return new_child


    def simulate(self):
        """
        In simulation we donot disturb the available_actions in the node
        To Avoid confusion we will use "available_action" or "new_action" when modifying or dealing with the MCTS Tree and Node
        And  available_moves or new_moves when performing simulation
        """

        current_state = self.state # Check if this needs to be a deepcopy to avoid modifications in the self.state

        while not current_state.is_game_over():
            available_moves = current_state.get_legal_actions()
            new_move = self.simulation_policy(available_moves)
            current_state = current_state.move(new_move)

        return current_state.game_result


    def back_propogate(self, result):

        self._visits += 1
        self._results[result] += 1

        if self.parent:
            self.parent.backpropogate(result) #Include a print statement at check the result dictionary output for clearer understanding of code




