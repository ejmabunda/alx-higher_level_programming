#include <stdlib.h> /* NULL */

#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: list to check
 *
 * Return: 0 if there's no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *start_node;

	/* save pointer to the head */
	start_node = list;
	while (list->next != NULL)
	{
		list = list->next;
		/* check if head is encountered again */
		if (start_node == list)
			return (1);
	}

	/* no cycle */
	return (0);
}
