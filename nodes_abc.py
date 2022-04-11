from abc import ABC, abstractmethod
from collections import defaultdict

import numpy
import math




class AbstractNode (ABC):
    
    """ Node is a abtract class to define the base unit of the tree.

    Args:
        parent (int): Parent of the node, Type(Node), Default = none
        state : GameState at current node
        children (list): children of current node

    """
    def __init__(self, 
                 state,
                 parent=None):
        self.parent = parent
        self.state = state
        self.children = []

    @property
    @abstractmethod
    def N(self):
        """ Number of Visits of the current node"""
        pass

    @property
    @abstractmethod
    def Q(self):
         """ Q Value the current node"""
         pass

    @property
    @abstractmethod
    def available_actions(self):
        """Can Be Further expanded"""
        pass

    @abstractmethod
    def is_terminal(self):
        pass

    @abstractmethod
    def is_expanded(self):
        return len(self.available_actions)==0

    @abstractmethod
    def expand(self):
        pass

    @abstractmethod
    def simulate(self):
        pass

    @abstractmethod
    def back_propogate(self, reward_val):
        pass

    
    def best_child(self, C = np.sqrt(2)):
        """ Using UCT to select best child node Q_Child / N_Child + c * sqrt(log(N_Self) / N_Child)
        Args:
            C (float): Exloration vs Exploitation Factor, Default = sqrt(2)

        Returns:
            child node from self.children list
        """
        
        uct = [ child.Q / child.N + C * np.sqrt(2 * np.log(self.N) / child.N) for child in self.children ]
        
        return self.children[np.argmax(uct)]

    def simulation_policy(self, available_moves):
        """ Randomly select an action from given available actions list
        
        In simulation we donot disturb the available_actions in the node
        To Avoid confusion we will use "available_action" or "new_action" when modifying or dealing with the MCTS Tree and Node
        And  available_moves or new_moves when performing simulation
        
        Args: 
            available_moves(list)
        Returns:
            Action from list of available actions
        """
        return available_moves[np.random.randint(len(available_moves))]






