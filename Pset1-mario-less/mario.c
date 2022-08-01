#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // do while loop
    int n;
    do
    {
        //Prompt use for number
        n = get_int("Height\n");
    }
    // while n is not in range 1-8 it will repeat
    while (n < 1 || n > 8);

// loop # blocks
    for (int i = 0 ; i < n; i++)
    {
// print spaces / dots to reverse pyramid
        for (int k = n - 1; k > i; k--)
        {
            printf(" ");
        }
// print number of # in row (haf square)
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }
// prints # on new line
        printf("\n");
    }

}


