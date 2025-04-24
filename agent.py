import subprocess
import json

class Agent:
    """
    Base class of a tic-tac-toe playing agent. (A pure abstract one,
    anyway.)
    """
    def get_move(self, board):
        pass

class HumanAgent:
    """
    A human agent that plays tic-tac-toe.
    """

    def __init__(self, coord_string='x, y'):
        self.coord_string = coord_string

    def get_move(self, board):
        """
        Get the move from the human player as a tuple.
        """
        return eval(input(f"Enter your move as {self.coord_string}: "))

class ProgramAgent(Agent):
    """
    Interface with a tic-tac-toe playing program.
    """

    def __init__(self, program):
        self.program = program
        self.process = subprocess.Popen( 
            program,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=None,
            text=True,
            universal_newlines=True
        )


    def __del__(self):
        self.process.terminate()
        self.process.wait()


    def get_move(self, board):
        """
        Get the move from the program, via JSON communication.
        """
        # send the status
        bd = board.to_dict()
        bd['moves'] = board.moves()
        json.dump(bd, self.process.stdin)
        self.process.stdin.write('\n')
        self.process.stdin.flush()

        # get the move
        move = json.loads(self.process.stdout.readline())

        return move


def agent_list():
    """
    Return a list of all the executable files in the agents directory.
    """
    import os
    from pathlib import Path

    agents_dir = Path(__file__).parent / 'agents'
    agents = [agents_dir / f for f in os.listdir(agents_dir) if
              os.access(agents_dir/f, os.X_OK) and
              os.path.isfile(agents_dir/f)]
    return agents

def agent_select(coord_string='x, y'):
    """
    Return an agent item according to the user's choice.
    """
    agents = ['Human Player'] + agent_list()
    for i in range(1, len(agents)+1):
        print(f"{i}: {agents[i-1]}")
    while True:
        i = int(input("Your choice? "))-1
        if i<0 or i>=len(agents):
            print("Invalid choice. Please Try Again.")
        else:
            break

    # Return the selected agent
    if i == 0:
        return HumanAgent(coord_string=coord_string)
    else:
        return ProgramAgent(agents[i])

def get_players(coord_string='x, y'):
    """
    Get players for X and O. Return as a dicitionary.
    """
    result = {}
    print("Who will play X?")
    result['X'] = agent_select(coord_string=coord_string)
    print("Who will play O?")
    result['O'] = agent_select(coord_string=coord_string)

    return result
