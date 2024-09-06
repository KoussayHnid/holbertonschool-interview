#include "substring.h"
#include <stdlib.h>
#include <string.h>

/**
 * find_substring - Finds all the possible substrings containing a list of words.
 * @s: The string to scan.
 * @words: The array of words, each substring must be a concatenation of these words.
 * @nb_words: The number of elements in the array words.
 * @n: Pointer to store the number of elements in the returned array.
 *
 * Return: An allocated array storing each index in s where a substring was found.
 */
int *find_substring(char const *s, char const **words, int nb_words, int *n)
{
    int str_len = strlen(s);
    int word_len = strlen(words[0]);
    int substr_len = word_len * nb_words;
    int *indices = NULL;
    int count = 0;

    if (substr_len > str_len)
    {
        *n = 0;
        return NULL;
    }

    indices = malloc(sizeof(int) * (str_len - substr_len + 1));
    if (indices == NULL)
        return NULL;

    char **temp = malloc(sizeof(char *) * nb_words);
    int *freq = malloc(sizeof(int) * nb_words);
    for (int i = 0; i < nb_words; i++)
        freq[i] = 0;

    for (int i = 0; i <= str_len - substr_len; i++)
    {
        for (int j = 0; j < nb_words; j++)
            temp[j] = strndup(s + i + j * word_len, word_len);

        for (int j = 0; j < nb_words; j++)
            freq[j] = 0;

        int valid = 1;
        for (int j = 0; j < nb_words; j++)
        {
            int found = 0;
            for (int k = 0; k < nb_words; k++)
            {
                if (strcmp(temp[j], words[k]) == 0 && freq[k] == 0)
                {
                    freq[k] = 1;
                    found = 1;
                    break;
                }
            }
            if (!found)
            {
                valid = 0;
                break;
            }
        }

        if (valid)
        {
            indices[count] = i;
            count++;
        }

        for (int j = 0; j < nb_words; j++)
            free(temp[j]);
    }

    free(temp);
    free(freq);

    if (count == 0)
    {
        free(indices);
        *n = 0;
        return NULL;
    }

    *n = count;
    return indices;
}
