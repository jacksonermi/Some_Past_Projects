#include "ccrush.h"
#include <stdio.h>
/*
  This file will contain all code for the main execution loop.  This
  code should be kept simple and concise. Functions containing more
  specialized behaviors will be placed in other files.
*/

/* P1 - Modify main function to make a game board and print it */
/* P2 - Add a "game loop" that accepts input from the user until
        a quit key is pressed, modifying the board based on the
        key pressed */
int main(void) {
	board_t x = load_board(MAP, 8);
	print_board(x);
	char cmd;
	while  (cmd != -1) {
		scanf("%c", &cmd);	
		process_command(cmd, &x);
		print_board(x);
	}
	return 0;

}
