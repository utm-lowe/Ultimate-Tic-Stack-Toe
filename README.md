# Ultimate Tic-Stack-Toe
Welcome to this year's Hack-a-Thon! The hint was that you would be
creating an adversarial agent that can work in a simulated
environment. This year's environment is a simple one with a twist. Our
environment will consist of a game board, and your program will play
in a round robin tournament against other programs.

## Tic-Tac-Toe
We could have gone with a simple game of Tic-Tac-Toe, our familiar 3x3
grid where players take turns placing X's and O's until one player
gets three in a row, or they draw. A game like this:

```
   |   |  
---+---+---
   |   |  
---+---+---
   |   |  
```

Of course, we know what the draw back to this game is. Unless you are
playing against someone under the age of 5, the game will always end
in a draw. There simply isn't a winning strategy if neither player
makes a mistake.

## 3D Tic-Tac-Toe
Throughout the years, there have been a variety of extensions to the
came to correct this problem. For example, one might consider
a 3 dimensional tic-tac-toe game, where players take turns placing
X's and O's in a 3D grid. 

```
   |   |  
---+---+---
   |   |  
---+---+---
   |   |  

   |   |  
---+---+---
   |   |  
---+---+---
   |   |  

   |   |  
---+---+---
   |   |  
---+---+---
   |   |  
```

These grids are stacked on top of each other, and the game is won when
a player gets 3 in a row along any dimension. For instance, we can
have a vertical win:

```
 X |   |  
---+---+---
   |   |  
---+---+---
   |   |  

 X |   |  
---+---+---
   |   |  
---+---+---
   |   |  

 X |   |  
---+---+---
   |   |  
---+---+---
   |   |  
```

Or a win along a diagonal:

```
 X |   |  
---+---+---
   |   |  
---+---+---
   |   |  

   | X |  
---+---+---
   |   |  
---+---+---
   |   |  

   |   | X
---+---+---
   |   |  
---+---+---
   |   |  
```

## Ultimate Tic-Tac-Toe
3d Tic-Tac-Toe is a fun game, and in fact it is impossible for this
game to end in a draw! There is just one little problem. There is
a winning strategy for the first player. If the first player plays the
center square of the center board, they cannot lose unless they make
a mistake. If you alter the rules so that the first player cannot take
this square, then the first player who does take the square can force
a victory. So, in fact, this game is solved.

That's where we get into Ultimate Tic Tac Toe. In ultimate
tic-tac-toe, we have a 3x3 grid of tic-tac-toe boards. The first
player plays in any square of the center board, and the second player
plays in the square of the board that corresponds to the square
played by the first player. Suppose we have a grid that looks like
this: 


```
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
#######################################
   |   |    #  X |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
#######################################
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
```

Suppose the first player, who can move anywhere,  plays in square
(0,0) of the center board (1,1).  The second player must play in the
upper left board (board (0,0)).  Suppose that player plays in square
(1,0) of that board. X must now play on board (1,0). 

```
   | O |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
#######################################
   |   |    #  X |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
#######################################
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
```

When a player wins a board, the board is marked with either an X or an
O. After a win, or after a scratch on a board, the next player can
once again play anywhere on the board. Consider the following sample
final board:

```
 O | O | X  #    X    X   #   OOOOOO   
---+---+--- #     X  X    #  O      O  
 X |   | O  #      XX     #  O      O  
---+---+--- #     X  X    #  O      O  
 X | O | O  #    X    X   #   OOOOOO   
#######################################
   X    X   #   OOOOOO    #    X    X  
    X  X    #  O      O   #     X  X   
     XX     #  O      O   #      XX    
    X  X    #  O      O   #     X  X   
   X    X   #   OOOOOO    #    X    X  
#######################################
  OOOOOO    #    X    X   #  X | O | O 
 O      O   #     X  X    # ---+---+---
 O      O   #      XX     #  O | X |   
 O      O   #     X  X    # ---+---+---
  OOOOOO    #    X    X   #  O | X | O 
Winner: O
```

Here, O has won the final game by winning the three squares along the
diagonal. Now this game is fun to play! It can end in a draw, but
the strategy is not yet fully solved. Though mathematicians do suspect
that there is a first player advantage, it is not yet known if this is
true. This is also the stuff of many an AI homework assignment as the
decision tree of a game like this is quite large, and it must be
pruned. This is a good way to explore heuristic algorithms. The thing
is, there are lots of very good agents for this game readily available
for the taking, so it is well-explored territory. 

## Ultimate Tic-Stack-Toe
What if we can do better? What if we can make this game even more
difficult? What if we could make the game so complex that even ChatGPT
and Copilot will struggle to find a winning strategy? It turns out we
can! Enter ULTIMATE TIC-STACK-TOE the first three dimensional ultimate
tic-tac-toe game.

In this game, we have three layered ultimate tic-tac-toe boards:

```
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
#######################################
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
#######################################
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   

   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
#######################################
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
#######################################
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   

   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
#######################################
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
#######################################
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   
---+---+--- # ---+---+--- # ---+---+---
   |   |    #    |   |    #    |   |   

Enter your move as layer, bx, by, x, y: 
```

As you can see, a move consists of 5 coordinates. The layer, bx, by,
x, and y. Each layer acts like an independent tic-tac-toe board, and
each carries its own constraints. Your goal is to win the game by
winning boards in the layers. Vertical wins are possible, but only
from the outer layer of the ultimate tic-tac-toe board. Thus you score
a position in the 3d game by making moves on each of the ultimate
board layers. Here is an example final game configuration:

```
   | O |    #    X    X   #    |   | O 
---+---+--- #     X  X    # ---+---+---
 O | X | O  #      XX     #    | X | O 
---+---+--- #     X  X    # ---+---+---
   | O | X  #    X    X   #  X | O | X 
#######################################
   X    X   #  X |   |    #   OOOOOO   
    X  X    # ---+---+--- #  O      O  
     XX     #    |   |    #  O      O  
    X  X    # ---+---+--- #  O      O  
   X    X   #  O | X | O  #   OOOOOO   
#######################################
   |   | O  #    X    X   #   OOOOOO   
---+---+--- #     X  X    #  O      O  
 O |   | X  #      XX     #  O      O  
---+---+--- #     X  X    #  O      O  
 O | O | X  #    X    X   #   OOOOOO   

 O | X | O  #  O |   | O  #  O |   |   
---+---+--- # ---+---+--- # ---+---+---
 X | O | O  #    |   |    #  X |   |   
---+---+--- # ---+---+--- # ---+---+---
   | O |    #  X |   |    #    | O | X 
#######################################
   | X |    #  O |   | O  #   OOOOOO   
---+---+--- # ---+---+--- #  O      O  
   |   | X  #  O | X | X  #  O      O  
---+---+--- # ---+---+--- #  O      O  
 X |   | X  #  X | O |    #   OOOOOO   
#######################################
   |   |    #   OOOOOO    #  X |   |   
---+---+--- #  O      O   # ---+---+---
   | O | X  #  O      O   #    | O | X 
---+---+--- #  O      O   # ---+---+---
   | X | X  #   OOOOOO    #    | X | O 

  OOOOOO    #    X    X   #   OOOOOO   
 O      O   #     X  X    #  O      O  
 O      O   #      XX     #  O      O  
 O      O   #     X  X    #  O      O  
  OOOOOO    #    X    X   #   OOOOOO   
#######################################
  OOOOOO    #  O | X | O  #   OOOOOO   
 O      O   # ---+---+--- #  O      O  
 O      O   #  X | O | X  #  O      O  
 O      O   # ---+---+--- #  O      O  
  OOOOOO    #    | O | X  #   OOOOOO   
#######################################
 X | O | X  #    X    X   #    X    X  
---+---+--- #     X  X    #     X  X   
 X | X | O  #      XX     #      XX    
---+---+--- #     X  X    #     X  X   
 O | X | O  #    X    X   #    X    X  

Winner: O
```

Here, O has one via a vertical win. Can you see where it is?

Now we have a game worthy of this modern generative ai-powered age.
The game is complex, it has an unknown strategy, and it is also
possible to end in a draw. Sure, it may be slightly impractical for
human players, but the age of man has passed. We are in the machine age!
So let's get to work!

## Running the Programs
The programs are written in Python 3.8. They use built-in python
modules and should work on any operating system but they have only
been tested in UNIX-like environments. The programs are designed to be
run inside of GitHub Codespaces, so you can rest assured that they
will work there. You are welcome to use any of the code in the python
files, just note that I will be running your programs against a stock
version of them.

There are four programs in the repository:
  1. `playTTT.py` - This allows you to play the standard game of
     tic-tac-toe. This is handy to get a feel for how the coordinate
     system works.

  2. `play3dTTT.py` - This allows you to play the 3d version of the
     game. Again, you might want to try this to get the layered
     coordinate system down.

  3. `playUTTT.py` - This allows you to play ultimate tic-tac-toe.

  4. `playUTST.py` - And this program allows you to play the current
     state of the art in tic-tac-toe technology: ultimate
     tic-stack-tac-toe.

In all cases, there are few things to note about the games. The first
is that the coordinates are all zero based. They are simply being used
as array indices. Second, when you start the game, you will be asked
who will play each side:

````
Who will play X?
1: Human Player
2: /Ultimate-Tic-Stack-Toe/agents/random-move.py
Your choice? 
````

The first option is a human player, that's you, and the rest are
agents which are stored in the `agents` directory. The programs simply
scan this folder looking for executable files. Any program in here can
be run as an agent. As a sample, you are provided with
'random-move.py' and easily defeated agent that simply selects
a random valid move. `random-move.py` may be a terrible player, but it
is a versatile one! It can play any tic-tac-toe variation. You don't
have to do that with your agent though, you only need to create an
agent which can play Ultimate Tic-Stack-Toe.

## Writing Your Agent
Your agent will simply be a program which will be placed in the agents
directory. You can write this program in any language that you can get
working on Codespaces (which is pretty much every language that has
ever existed as this is simply a Debian-based Linus environment). Your
agent will communicate with the game environment via standard input
and standard output. The game will send you a JSON encoded object
consisting of the following fields:

```
{
   boards: The list game boards (3 of them)
   winner: The winner of the game
   moves: A list of valid moves from this position
}
```

Your task is to select one of the moves from among those in the list
and send back a JSON encoded object consisting of an array of
coordinates by printing it to standard out.

Here's an example transaction from `random-move.py`. First the input (sent
from the game):

```
{"winner": null, "boards": [{"winner": null, "grid": [[{"winner": null, "grid": 
[[{"winner": null}, {"winner": null}, {"winner": "X"}], [{"winner": "X"}, {"winn
er": "O"}, {"winner": null}], [{"winner": "O"}, {"winner": null}, {"winner": "O"
}]]}, {"winner": "O", "grid": [[{"winner": null}, {"winner": "X"}, {"winner": "O
"}], [{"winner": "O"}, {"winner": "O"}, {"winner": "O"}], [{"winner": null}, {"w
inner": "X"}, {"winner": null}]]}, {"winner": "X", "grid": [[{"winner": "X"}, {"
winner": "O"}, {"winner": "X"}], [{"winner": null}, {"winner": "X"}, {"winner": 
"O"}], [{"winner": "X"}, {"winner": "O"}, {"winner": "O"}]]}], [{"winner": "X", 
"grid": [[{"winner": "O"}, {"winner": "X"}, {"winner": "O"}], [{"winner": null},
 {"winner": "X"}, {"winner": null}], [{"winner": null}, {"winner": "X"}, {"winne
r": null}]]}, {"winner": null, "grid": [[{"winner": null}, {"winner": "O"}, {"wi
nner": "O"}], [{"winner": "O"}, {"winner": null}, {"winner": null}], [{"winner":
 "O"}, {"winner": "X"}, {"winner": "X"}]]}, {"winner": null, "grid": [[{"winner"
: null}, {"winner": null}, {"winner": "X"}], [{"winner": "O"}, {"winner": null},
 {"winner": null}], [{"winner": "O"}, {"winner": "X"}, {"winner": "X"}]]}], [{"w
inner": null, "grid": [[{"winner": "X"}, {"winner": null}, {"winner": null}], [{
"winner": "O"}, {"winner": null}, {"winner": "X"}], [{"winner": null}, {"winner"
: "O"}, {"winner": null}]]}, {"winner": null, "grid": [[{"winner": "X"}, {"winne
r": "O"}, {"winner": null}], [{"winner": "O"}, {"winner": null}, {"winner": "O"}
], [{"winner": "O"}, {"winner": "X"}, {"winner": "X"}]]}, {"winner": "O", "grid"
: [[{"winner": "O"}, {"winner": "O"}, {"winner": "O"}], [{"winner": null}, {"win
ner": "X"}, {"winner": "O"}], [{"winner": null}, {"winner": null}, {"winner": "X
"}]]}]], "last_board": [0, 2]}, {"winner": null, "grid": [[{"winner": "O", "grid
": [[{"winner": null}, {"winner": null}, {"winner": null}], [{"winner": null}, {
"winner": null}, {"winner": null}], [{"winner": "O"}, {"winner": "O"}, {"winner"
: "O"}]]}, {"winner": null, "grid": [[{"winner": "O"}, {"winner": null}, {"winne
r": "X"}], [{"winner": null}, {"winner": "O"}, {"winner": "X"}], [{"winner": nul
l}, {"winner": null}, {"winner": null}]]}, {"winner": "O", "grid": [[{"winner": 
"X"}, {"winner": null}, {"winner": "X"}], [{"winner": "O"}, {"winner": "O"}, {"w
inner": "O"}], [{"winner": null}, {"winner": "O"}, {"winner": "O"}]]}], [{"winne
r": null, "grid": [[{"winner": null}, {"winner": "X"}, {"winner": null}], [{"win
ner": null}, {"winner": null}, {"winner": "O"}], [{"winner": "X"}, {"winner": nu
ll}, {"winner": "X"}]]}, {"winner": null, "grid": [[{"winner": null}, {"winner":
 null}, {"winner": "X"}], [{"winner": "X"}, {"winner": null}, {"winner": "X"}], 
[{"winner": "X"}, {"winner": null}, {"winner": null}]]}, {"winner": null, "grid"
: [[{"winner": null}, {"winner": "X"}, {"winner": "X"}], [{"winner": "X"}, {"win
ner": "O"}, {"winner": "O"}], [{"winner": null}, {"winner": null}, {"winner": nu
ll}]]}], [{"winner": null, "grid": [[{"winner": "X"}, {"winner": "X"}, {"winner"
: "O"}], [{"winner": null}, {"winner": "O"}, {"winner": null}], [{"winner": "X"}
, {"winner": "O"}, {"winner": "O"}]]}, {"winner": "O", "grid": [[{"winner": "O"}
, {"winner": "O"}, {"winner": "O"}], [{"winner": "X"}, {"winner": null}, {"winne
r": null}], [{"winner": "O"}, {"winner": "X"}, {"winner": null}]]}, {"winner": n
ull, "grid": [[{"winner": "X"}, {"winner": null}, {"winner": "X"}], [{"winner": 
"X"}, {"winner": null}, {"winner": null}], [{"winner": null}, {"winner": "O"}, {
"winner": null}]]}]], "last_board": [0, 1]}, {"winner": null, "grid": [[{"winner
": null, "grid": [[{"winner": "O"}, {"winner": null}, {"winner": null}], [{"winn
er": null}, {"winner": "X"}, {"winner": null}], [{"winner": null}, {"winner": "O
"}, {"winner": "X"}]]}, {"winner": null, "grid": [[{"winner": null}, {"winner": 
"O"}, {"winner": "O"}], [{"winner": "X"}, {"winner": null}, {"winner": "X"}], [{
"winner": "X"}, {"winner": null}, {"winner": null}]]}, {"winner": null, "grid": 
[[{"winner": "X"}, {"winner": null}, {"winner": "O"}], [{"winner": "O"}, {"winne
r": "X"}, {"winner": "O"}], [{"winner": null}, {"winner": "O"}, {"winner": null}
]]}], [{"winner": null, "grid": [[{"winner": "O"}, {"winner": "X"}, {"winner": n
ull}], [{"winner": "X"}, {"winner": "X"}, {"winner": null}], [{"winner": "X"}, {
"winner": "O"}, {"winner": "O"}]]}, {"winner": "X", "grid": [[{"winner": null}, 
{"winner": null}, {"winner": "X"}], [{"winner": null}, {"winner": null}, {"winne
r": null}], [{"winner": "X"}, {"winner": "X"}, {"winner": "X"}]]}, {"winner": nu
ll, "grid": [[{"winner": null}, {"winner": "X"}, {"winner": null}], [{"winner": 
"O"}, {"winner": "X"}, {"winner": "X"}], [{"winner": null}, {"winner": "O"}, {"w
inner": null}]]}], [{"winner": null, "grid": [[{"winner": null}, {"winner": null
}, {"winner": "O"}], [{"winner": "X"}, {"winner": "O"}, {"winner": null}], [{"wi
nner": null}, {"winner": "O"}, {"winner": null}]]}, {"winner": "X", "grid": [[{"
winner": "X"}, {"winner": "X"}, {"winner": "X"}], [{"winner": "X"}, {"winner": n
ull}, {"winner": "O"}], [{"winner": "O"}, {"winner": "X"}, {"winner": "X"}]]}, {
"winner": null, "grid": [[{"winner": null}, {"winner": null}, {"winner": "X"}], 
[{"winner": null}, {"winner": "X"}, {"winner": "O"}], [{"winner": null}, {"winne
r": "O"}, {"winner": null}]]}]], "last_board": [0, 2]}], "moves": [[0, 0, 2, 0, 
2], [0, 0, 2, 1, 0], [0, 0, 2, 1, 1], [0, 0, 2, 2, 0], [0, 0, 2, 2, 2], [1, 0, 1
, 0, 0], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 0, 1, 1, 2], [1, 0, 1, 2, 0], [2,
 0, 2, 0, 0], [2, 0, 2, 0, 2], [2, 0, 2, 1, 0], [2, 0, 2, 2, 1], [2, 0, 2, 2, 2]
]}
```

Then the program responds with the following:

```
[2, 0, 2, 1, 0]
```

At first glance, this may seem overwhelming. Really though, it's just
a bunch of nested associative arrays. To keep things general, each
layer has a "winner". Suppose we decoded the JSON object into an
object called `state`. In python, this would come across as
a dictionary. The winner of the overall game would be found at:

```
state['winner']
```

The winner of given layer would be:
```
state['boards'][layer]['winner']
```

The winner of one of the layer's sub-boards would be at
```
state['boards'][layer]['grid'][by][bx]['winner']
```

And the occupant of a given square (full 5 dimensional coordinate)
would be at:
```
state['boards'][layer]['grid'][by][bx]['grid'][y][x]['winner']
```

You can also have a look at `ticTacToe.py` to see how the game is
implemented. It is basically the above structure, plus the logic for
checking for wins. Of course, the above would need to be adjusted for
the JSON implementation of the language of your choice. I would
strongly recommend that you grab a pre-made JSON library for this
because parsing this would be a challenge unto itself.

## Submitting Your Agent
Your agent needs to be able to run in GitHub codespaces. To submit
your agent, I would like you to commit and push your source code and
your codespaces compiled binary in the agents directory. Do your work
in this repository, submitting all source and that binary by committing
and pushing your changes. You are welcome to work on your own
computers, just be sure that your program runs on codespaces before
the final submission.

In addition to the source code, please fill out the "AGENT-FORM.md"
file with the information in requests. Be sure to include any special
installation or compilation instructions.


## Judging
Your program will play in a round robin tournament against the other
submissions. In each game, the X and O player will be randomly
assigned. The program that wins the most games will be declared the
winner! If there is a tie, we will play a best two out of three runoff
between the tied programs.

And with that, I will leave you to it. Go forth and write your
competitive agent. 

Enjoy!
