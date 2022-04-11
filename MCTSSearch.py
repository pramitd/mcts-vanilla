import numpy
import time

class MCTSSearch():

    def __init__(self, root_node):
        """
        Args:
            root_node: MCTSNode  
        """
        self.root_node = root_node

    def best_action (self, max_sims = None, max_time = None):
        """
        Select the best action from the given node by performing MCTS

        Args:
            max_sims (int): Maximum Number of Simulations to be Performed 
            max_time (int): Maximum Time for which MCTS to be run in seconds

        Returns:
            best_child_node (MCTSNode): Best child node from the given root node --> the C parameter can be varied 

        """

        #assert max_sims is not None and max_time is not None, "Specify Either Max Sims or Max Time"
        if max_sims in None:
            assert (max_time is not None, "Specify Either Max Sims or Max Time")
            end_time  = time.time() + max_time

            while time.time() < end_time:
                new_node  = self.tree_policy()
                sim_result = new_mode.simulate()
                new_node.back_propogate(sim_result)

        else:
            for _ in range(0, max_sims):
                new_node  = self.tree_policy()
                sim_result = new_mode.simulate()
                new_node.back_propogate(sim_result)


        return self.root_node.best_child() #Using UCT to Select the Best Node Additionally C=0 can be specified to only select Q_child/N_child


    def tree_policy(self):
        current_node = self.root_node # Alwayds Start TP from root node.  NOTE: Check if Deepcopy required
        
        while not current_node.is_terminal():
            if not current_node.is_expanded():
                return current_node.expand()
            else:
                current_node = current_node.best_child()    


        return current_node

        

                


