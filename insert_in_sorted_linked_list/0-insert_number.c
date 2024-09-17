#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the pointer of the head of the list.
 * @number: The number to insert.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = malloc(sizeof(listint_t));
    listint_t *current = *head;
    listint_t *prev = NULL;

    if (!new_node)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    if (!current || current->n >= number)
    {
        new_node->next = current;
        *head = new_node;
        return (new_node);
    }

    while (current && current->n < number)
    {
        prev = current;
        current = current->next;
    }

    new_node->next = current;
    prev->next = new_node;

    return (new_node);
}
