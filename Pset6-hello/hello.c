#include <stdio.h>
#include <cs50.h>


int main(void)
{
    // prompt user for a name
    string name = get_string("What is your name?\n");
    // return greeting and name 
    printf("Hello, %s.\n", name);
}
