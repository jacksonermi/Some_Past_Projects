#include <stdio.h>
#include "ccrush.h"
#include "symbols.h"

/*
 This file contains code for managing the game board.  This includes
 functions like building and printing the board.
*/

/* P2 - Define process_command (see assignment for instructions) */	
void swap(board_t* game) {
	int a = game->cursor.y;
	int b = game->cursor.x +1;
	int c = game->cursor.x;
	int value_1 = game->board[a][c];
	int value_2 = game->board[a][b];
	game->board[a][c] = value_2;
	game->board[a][b] = value_1;
	
}	
int process_command(char cmd, board_t* game) {
	if (cmd == 'q') {
		return -1;
	}
	else if (cmd == 'a'){
		if (game->cursor.x == 0){ 
			return 0;
		}
		else {
			game->cursor.x = game->cursor.x-1;
		}	
	}
	else if (cmd == 'd') {
		if (game->cursor.x + 1 == BOARDSIZE-1){ 
			return 0;
		}
 		else {
			game->cursor.x = game->cursor.x + 1;
		}		
	}
	else if (cmd == 'w') { 
		if (game->cursor.y == BOARDSIZE - 1) {
			return 0;;
		}       
		else {
	 		game->cursor.y = game->cursor.y + 1;
		}		
	}
	else if (cmd == 's') {
		if (game->cursor.y == 0){
			return 0;
		}
		else {
			game->cursor.y = game->cursor.y - 1;
		}
	}
	else if (cmd == 'e') {
		swap(game);
	}

  /* Replace this return statement with the functionality described in the assignment */
  return 0;
}

/* P2 - Define game_logic (see assignment for instructions) */
void game_logic(board_t* game) {
  
}
