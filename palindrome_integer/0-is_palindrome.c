#include "palindrome.h"

/**
* is_palindrome - checks whether or not a given unsigned integer is a palindrome.
* @n: number to be checked
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(unsigned long n) {
    unsigned long reversed = 0, original = n, remainder;

    while (n != 0) {
        remainder = n % 10;
        reversed = reversed * 10 + remainder;
        n /= 10;
    }

    if (original == reversed) {
        return 1;
    } else {
        return 0;
    }
}
