from Tournaments import *
from validation import *

welcome = "########## ########  ##    ##  #########   ##   ##     ####         ###       ###      #########  ##   ##   ##########\n" \
          "    ##     ##    ##  ##    ##  ##     ##   ###  ##    ##  ##       ## ##     ## ##     ##         ###  ##       ##    \n" \
          "    ##     ##    ##  ##    ##  #########   ##  ###   ########     ##   ##   ##   ##    #########  ##  ###       ##    \n" \
          "    ##     ##    ##  ##    ##  ##      ##  ##   ##  ##      ##   ##     ## ##     ##   ##         ##   ##       ##    \n" \
          "    ##     ########  ########  ##      ##  ##   ## ##        ## ##       ###       ##  #########  ##   ##       ##    \n" \
          "\n" \
          "\n" \
          "                 ### ###   #### ####  ##### ## ##  ##     ######  ##  ##  ####   ###   ###  ##### #####  ####\n" \
          "  ###########    ### #     ##   ##    ## ## ## ### ##       ##    ##  ##  ##    ##    ##    ## ## ## ##  ##  \n" \
          "  ###########    ####      #### ####  ##### ## ## ###       ##    ######  ####    #  ##     ## ## #####  ####\n" \
          "                 ### #     ##   ##    ##    ## ##  ##       ##    ##  ##  ##     ##   ##    ## ## ##  #  ##  \n" \
          "                 ###  ###  #### ####  ##    ## ##  ##       ##    ##  ##  ####  ##     ##   ##### ##   # #### \n"

print(welcome)

from Play import *

#todo wenni implement intro with input = Name of the league


new_game = Play()
new_game.print_league()
new_game.start_tournament()
print(new_game)




