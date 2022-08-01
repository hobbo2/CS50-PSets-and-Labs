#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>


bool only_alpha(string s);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else if (strlen(argv[1]) != 26 || only_alpha(argv[1]) != true)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
}

bool only_alpha(string s)
{
    // iterate over argv to check it is all digits
    for (int i = 0; i < strlen(s); i++)
    {
        if(isalpha(s[i]) == 0)
        {
            return false;
        }
    }
    return true;
}

// function for converting key to plaintext
// iterate over the key
char rotate(char c, int n)
{
    
}