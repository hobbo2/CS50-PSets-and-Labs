#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

// prototype
bool only_digits(string s);
char rotate(char c, int n);


int main(int argc, string argv[])
{


    // Make sure command line only takes 1 argument
    // call only digits into main
    if (argc != 2 || only_digits(argv[1]) != true)
    {
        printf("Usage: Caesar key \n");
        return 1;
    }
    else
    {

        // modify argv[1] into in
        int key = atoi(argv[1]);
        // prompt user for input
        string plain_text = get_string("Plaintext:  ");
        // call rotate and cipher
        printf("ciphertext: ");
        for (int i = 0; i < strlen(plain_text); i ++)
        {
            char c = rotate(plain_text[i], key);
            printf("%c", c) ;
        }
        printf("\n");
    }

}


// Check if only digits and return true or false
bool only_digits(string s)
{

    for (int i = 0; i < strlen(s); i++)
    {
        if (isdigit(s[i]))
        {

        }
        else
        {
            return false ;
        }

    }
    return true;
}


// function to rotate char taking key as input int.
char rotate(char c, int n)
{
    // take char c and check if it is alpha

    if (isalpha(c))
    {
        // check if upper or lower case
        if (isupper(c))
        {
            c = ((c) - 'A' + n) % 26 + 'A';
        }
        else
        {
            c = ((c) - 'a' + n) % 26 + 'a';
        }
    }

    return c;
}





