#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checkd if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if list has a cycle, 0 if not
 */

int check_cycle(listint_t *list1)
{
	if (!list1)
		return 0;


	listint_t *current = list1;
	listint_t *runner = list1->next;

	while (runner && runner->next)
	{
		if (current == runner)
			return 1;

		current = current->next;
		runner = runner->next->next;
	}

	return 0;
}
