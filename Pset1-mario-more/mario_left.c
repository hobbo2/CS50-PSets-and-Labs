#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;

    do
    {
        n = get_int("Height: \n");
    }
    while (n < 0 || n > 8);

    for(int i = 0; i < n ; i++ )
    {
        for(int l = 0; l < i + 1 ; l++)
        {
            printf("#");
        }


        printf("\n");
    }
}