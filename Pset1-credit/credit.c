#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    long long n;
    // prompt for input
    do
    {
        n = get_long_long("Number: ");
    }
    while (n < 0);

    // take n and perform luhnes algo on it
    // sum the last number
    // get second last number and multiply by 2
    //loop the process
    int num0;
    int sum0 = 0;
    int num1;
    int d1; // the sum of the digits from num1
    long long cardnum = n;

    while (cardnum != 0)
    {
        num0 = cardnum % 10;
        sum0 += num0;
        num1 = ((cardnum / 10) % 10) * 2;
        d1 = (num1 / 10) + (num1 % 10);
        sum0 += d1;
        cardnum /= 100;
    }
    //printf("%i\n", sum0);

    // calculate length of cardnumer using log???
    int c_len = 0;
    long long card = n;
    while (card > 0)
    {
        card = card / 10;
        c_len ++;
    }
    //printf("%i\n", c_len);

    // calculate first digits of card number
    int start = n / pow(10, c_len - 2);

    // return values and if statements
    if (sum0 % 10 != 0)
    {
        printf("INVALID\n");
    }
    else if (c_len == 15 && (start == 34 || start == 37))
    {
        printf("AMEX\n");
    }
    else if (c_len == 16 && (start >= 51 && start <= 55))
    {
        printf("MASTERCARD\n");
    }
    else if ((c_len == 13 || c_len == 16) && (start / 10) == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}