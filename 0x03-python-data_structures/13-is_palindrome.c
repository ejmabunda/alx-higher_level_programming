#include <stdlib.h>  /* NULL */

#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: points to the first node
 *
 * Return: 0 if not a palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed;
	listint_t *current;

	reversed = NULL;
	current = *head;

	/* copy list in reverse */
	while (current != NULL)
	{
		add_nodeint_end(&reversed, current->n);
		current = current->next;
	}

	/* check if nodes match */
	current = *head;
	while (current->n == reversed->n)
	{
		current = current->next;
		reversed = reversed->next;

		if (current == NULL && reversed == NULL)
			return (1);
	}

	/* not a palindrome */
	return (0);
}
