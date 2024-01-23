#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <stdint.h>
#define BLOCK_SIZE 512
typedef uint8_t  BYTE;
int main(int argc, char *argv[])
{
    if(argc!=2)
    {
        printf("error: input the replacement key and the program\n");
        return 1;
    }
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Error opening file \n");
        return 1;
    }
    bool found= false;
    int count= 0;
    BYTE buffer[BLOCK_SIZE];
    char name[8];
    FILE *final;

    while (fread(buffer, sizeof(BYTE),BLOCK_SIZE, file)== BLOCK_SIZE)
    {
        if (buffer[0]== 0xff &&
            buffer[1]== 0xd8 &&
            buffer[2]== 0xff &&
            (buffer[3] & 0xf0)== 0xe0
            )
        {
            if (count ==0)
            {
            sprintf(name, "%03i.jpg", count);
            final= fopen(name, "w");
            fwrite (&buffer, sizeof(BYTE), BLOCK_SIZE, final);
            count++;
            }
            else
            {
            fclose(final);
            sprintf(name, "%03i.jpg", count);
            final= fopen(name, "w");
            fwrite (&buffer, sizeof(BYTE), BLOCK_SIZE, final);
            count++;
            }
            // close final
            // create name and reopen final
            //count++
            //this is unfinished, will need further feedback and amendments
    }
    }
    fclose (file);
return 0;
}
