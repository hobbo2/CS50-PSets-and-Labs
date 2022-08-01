#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

// function prototypes
int count_letters(string text);
int count_words(string text);
int count_sentence(string text);


int main(void)
{
    // ask user for input
    string text = get_string("Text: ");


    // Call functons count_letters, count words and count sentences
    float letters = count_letters(text);
    float words = count_words(text);
    float sentences = count_sentence(text);

    // calculating score
    float L = letters / (words / 100);
    float S = sentences / (words / 100);
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    // Conditions for scores :
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }



}

// Function fo counting letters
int count_letters(string text)
{
    int count = 0;
    for (int i = 0, n = strlen(text); i < n ; i++)
    {
        if (isalpha(text[i]))
        {
            count++;
        }
    }
    return count;
}

// function to count words
int count_words(string text)
{
    int count = 1;
    for (int j = 0, n = strlen(text); j <= n ; j++)
    {
        if (isspace(text[j]))
        {
            count ++ ;
        }
        else if (n == 0)
        {
            count = 0 ;
        }
    }
    return count ;
}

// function to count sentences
int count_sentence(string text)
{
    int count = 0;

    for (int i = 0, n = strlen(text); i <= n ; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count ++ ;
        }
    }
    return count ;
}



