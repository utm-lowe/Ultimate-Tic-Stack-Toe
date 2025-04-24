#!/usr/bin/env python3
import json
import sys
from random import choice


try:
    while True:
        #get the board from stdin
        board=json.loads(input())
        sys.stderr.write(json.dumps(board)+'\n')

        # select a move at random from among the valid moves
        move=json.dumps(choice(board['moves']))

        # write the move to stderr (good for debugging)
        sys.stderr.write(move + '\n')

        # send the move to the board via stdout, being sure to flush
        print(move)
        sys.stdout.flush()
except:
    pass
