#include <cs50.h>
#include <stdio.h>
#include <math.h>
int main(void)
{
    //declare n as long
    long long n;
    // intialise do while loop
    do
    {
        n = get_long_long("Number: ");
    }
    while (n < 0); // possibly add check for lenth < 13

    // count number of numbers used
    int count = 0;
    long long cardnumber = n;
    while (cardnumber > 0)
    {
        cardnumber = cardnumber / 10;
        count++ ;
    }

    // sum of 1st from back numbers
    int sum = 0;
    long long i = cardnumber;
    int last_n;
    int second_n ;
    int digits; // sum of the digits on a product not the ACTUAL PRODUCT

    while (i != 0)
    {
       int d1 = i % 10;
        sum += d1;
        int d2 = 2 * ((i / 10) % 10);
        int r1 = (d2 % 10) + floor((d2 / 10) % 10);
        sum += r1;
        i /= 100;
    }


    // checksum
    string cardtype;
    int check = n / pow(10, count - 2);



    // American express card has 15 digits and starts with 34 OR 37
    if (count == 15 && (check == 34 || check == 37))
    {
        cardtype = "AMEX";
    }
    // MASTERCARD has 16 digits and starts ranges from 51 t0 55 <>
    else if (count == 16 && check >= 51 && check <= 55)
    {
        cardtype = "MASTERCARD";
    }
    else if ((count == 13 || count == 16) && (check / 10) == 4)
    {
        cardtype = "VISA" ;
    }
    else
    {
        printf("INVALID");
    }

    //checksum no correct)
    if (sum % 10 == 0)
    {
        printf("%s\n", cardtype);
    }
    else
    {
        printf("INVALID\n");
    }
}