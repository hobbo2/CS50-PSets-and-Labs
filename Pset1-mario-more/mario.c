#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // decalre variable n
    int n ;
    // do while loop to keep asking unless meets criteria
    do
    {
        n = get_int("Height: \n");
    }
    while (n < 1 || n > 8);

    // for loop to print # that match number n input
    for (int i = 0; i < n; i++)
    {
        // internal loop 1 : adding spaces from the left
        for (int k = n - 1; k > i ; k--)
        {
            printf(" ");
        }
        // internal loop 2 : create block
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");

        }

        printf("  ");
        // left side
        for (int l = 0; l < i + 1 ; l++)
        {
            printf("#");
        }
        printf("\n");
    }


}