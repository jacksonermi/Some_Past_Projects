#include <stdio.h>
#include "ccrush.h"
#include "symbols.h"
#include <stdlib.h>
char* SHAPES[] = {Y, G, W, P, B, R, O};

/*
 This file contains code for managing the game board.  This includes
 functions like building and printing the board.
*/

/* P1 - Define print_board (see assignment for instructions) */
void print_board(board_t game)
{
	// might be %d or %c idk yet)
	for (int i = 0; i<51; i++){
		printf("\n");
	}
	printf("+-----------------+\n");
	for (int i = game.size-1; i >=0; i--){
		printf("%c", '|');
		for (int j = 0; j<game.size; j++){
			int shape_to_print = game.board[i][j];
			if (i == game.cursor.y && j == game.cursor.x){
				printf("<%s", SHAPES[shape_to_print]);
			}
			else if (i== game.cursor.y&& j== game.cursor.x + 1){
				printf(" %s>", SHAPES[shape_to_print]);
			}
			else if (i == game.cursor.y && j == game.cursor.x + 2){
				printf("%s", SHAPES[shape_to_print]);
			}	
			else{
		//	printf("%s ", game.board[i][j]);
				printf(" %s", SHAPES[shape_to_print]);
			}
		}
		if (game.cursor.x == BOARDSIZE - 2 && game.cursor.y == i){
			printf("%c\n", '|');
		}
		else {
			printf(" %c\n", '|');
		}
	}
	printf("+-----------------+\n");
}

/* P1 - Define build_board (see assignment for instructions) */
board_t load_board(const char* filepath, int size)
{
	// break into two parts
	// open file
	// malloc board
	// determine whats in file then place into board one at a time
	// instead of printing assign 
	//
	FILE* file = fopen(filepath, "r");
	int** board_arr = malloc(sizeof(int*) * size);
	for (int i = 0; i<size; i++){
		board_arr[i] = malloc(sizeof(int) * size);
		for (int j = 0; j < size; j++) { 
			board_arr[i][j] = (fgetc(file) - 48); //offset
		}
		fgetc(file);
	}
	fclose(file);
	cursor_t cursor;
	cursor.x = 0;
	cursor.y = 0;
	board_t new_board;
	new_board.cursor = cursor;
	new_board.size = size;
	new_board.board = board_arr;
	return new_board;
}

