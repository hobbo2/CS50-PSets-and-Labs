#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage ./recover\n");
        return 1;
    }
    // open memory card to read and return if card cannot open or return file pointer
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open the file\n");
        return 1;
    }

    // declare variable for char to store 512 bytes
    unsigned char buffer[512];
    // keep track of images
    int jpegnum = 0;
    int filecount = 0;

    // define file for images
    FILE *img = NULL;

    // set file name and amount of bytes including /0
    char name[8];

    // read file
    while (fread(buffer, 512, 1, input) != 0)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (jpegnum == 0)
            {
                sprintf(name, "%03i.jpg", jpegnum);
                img = fopen(name, "w");
                fwrite(&buffer, 512, 1, img);
                jpegnum += 1;
            }
            else if (jpegnum > 0)
            {
                fclose(img);
                sprintf(name, "%03i.jpg", jpegnum);
                img = fopen(name, "w");
                fwrite(&buffer, 512, 1, img);
                jpegnum += 1;
            }
        }
        else if (jpegnum > 0)
        {
            fwrite(&buffer, 512, 1, img);
        }
    }
    fclose(input);
    fclose(img);

}