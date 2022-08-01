#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

//prototypes
bool only_digits(string s);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    // if more than 2 arguments or key is not a number return false
    if (argc != 2 || only_digits(argv[1]) != true)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    // prompt user for input
     string plaintext = get_string("plaintext:  ");
    printf("Ciphertext: ");
    // change argv to int
     int key = atoi (argv[1]);

     for (int i = 0; i < strlen(plaintext); i++)
    {
        char c = rotate (plaintext[i], key);
        printf("%c", c);
    }

    printf("\n");
     // call the functions


}

bool only_digits(string s)
{
    // iterate over argv to check it is all digits
    for (int i = 0; i < strlen(s); i++)
    {
        if(isdigit(s[i]) == 0)
        {
            return false;
        }
    }
    return true;
}

char rotate(char c, int n)
{
    if (isalpha(c))
    {
        if (isupper(c))
        {
            c = (c - 'A' + n) % 26 + 'A';
        }
        else
        {
            c = (c - 'a' + n) % 26 + 'a';
        }
    }
    return c;
}