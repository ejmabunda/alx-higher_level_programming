#include <stdlib.h>  /* NULL */

#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the first node
 * @number: number to initialize node with
 *
 * Return: the address of the new node, NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *next_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}

	while (((*head)->next)->n <= number)
		*head = (*head)->next;

	next_node = (*head)->next;
	(*head)->next = new_node;
	new_node->next = next_node;

	return (new_node);
}
