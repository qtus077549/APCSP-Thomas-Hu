#include<stdlib.h>
#include<stdio.h>
#include<cs50.h>
#include<time.h>
#include<string.h>
#include<ctype.h>

string sequence;
int object;
int numbers[];


void openfile(void);
void linearsearch (void);
void binarysearch (void);
int *selectionsort (void);
int *bubblesort (void);
void arrayaction (int *naxuy);

int main(void)
{
    bool file=0;
    int logic=0;
    do
    {
    printf("=======================================================\n");
    printf("welcome to Thomas's bimbimbambam program, help yourself\n");
    printf("Input:                                                 \n");
    printf("1. To read a file                                      \n");
    printf("2. To sort a file                                      \n");
    printf("3. To search a file                                    \n");
    printf("4. To write a file                                     \n");
    printf("5. Exit                                                \n");
    printf("=======================================================\n");
    int *naxuy=NULL;
    do
    {
    logic= get_int("Enter your number:");
    }
    while (logic<1 || logic>4);

    if (logic==1)
    {
        printf("=======================================================\n");
        openfile();
        naxuy= numbers;
        file=1;
        printf("=======================================================\n");
    }

    else if (logic==2 && file==1)
    {
        printf("=======================================================\n");
            if (sequence[2]== 'e')
            {
                binarysearch ();
            }
            else
            {
                linearsearch ();
            }
        printf("=======================================================\n");
    }

    else if (logic==3 && file==1)
    {
        int sortmethod;
        printf("=======================================================\n");
        printf("Sort with:                                             \n");
        printf("1. Bubble Sort                                         \n");
        printf("2. Selection Sort                                      \n");
        printf("=======================================================\n");
        do
        {
            sortmethod= get_int("Enter the sort logic you want to deploy:");
        }
        while (sortmethod!=1 && sortmethod!=2);
        if (sortmethod==1)
        {
            naxuy= bubblesort();
        }
        else
        {
            naxuy= selectionsort();
        }
        printf("=======================================================\n");
    }

    else if (logic==4 && file==1)
    {
        arrayaction(naxuy);
    }

    else if (file==0)
    {
        printf("=======================================================\n");
        printf("You must open a file first\n");
        printf("=======================================================\n");
    }
    }
    while (logic!=5);
}




void openfile (void)
{
    sequence = get_string("file type and operation (random or reversed): ");
    string object1 = get_string ("file size (5000-50000): ");
    object= atoi(object1);
    int numlength= strlen(object1);
    string fileName1= strcat(sequence, object1);
    string fileName=strcat(fileName1, ".txt");
    FILE *file= fopen(fileName, "r");
    if(!file)
    {
        printf("Unabble to open: %s\n", fileName);
    }
    char options[object][numlength];
    for (int i=0; i<object; i++)
    {
        fscanf(file, "%s", options[i]);
        numbers[i]=atoi(options[i]);
    }
    fclose(file);
}





void linearsearch (void)
{
int number= get_int ("input a number from 1-%i: ", object);
bool found=0;
    for(int i=0; i<object; i++)
    {
        if (number== numbers[i])
        {
            found=1;
            printf("index: %i\n", i);
            break;
        }
    }
    if (!found)
    {
    printf("please input a number from 1-5000: ");
    }
}






void binarysearch (void)
{
int number= get_int("input a number from 1-%i:\n", object);
int upper= object;
int lower= 0;
int avg;
    do
    {
        avg= (upper+lower)/2;
        if (number>numbers[avg])
        {
            upper= avg-1;
        }
        else if (number<numbers[avg])
        {
            lower= avg+1;
        }
    }
    while (number!= numbers[avg]);
    int index= avg;
    printf("index: %i\n", index);
}





int *selectionsort(void)
{
    int index;
    for (int j=0; j<object; j++)
    {
    int min= object;
    for (int i=j; i<object; i++)
    {
        if (numbers[i]<min)
        {
            min=numbers[i];
            index=i;
        }
    }
    int temp= numbers[j];
    numbers[j]= min;
    numbers[index]= temp;
    }
    return numbers;
}





int *bubblesort(void)
{
    bool swap;
    do
    {
        swap=0;
    for (int j=0; j<object-1; j++)
    {
        if(numbers[j]>numbers[j+1])
        {
            int temp= numbers[j+1];
            numbers[j+1]=numbers[j];
            numbers[j]=temp;
            swap=1;
        }
    }
    }
    while (swap);
    return numbers;
}





void arrayaction (int *naxuy)
{
    char type= get_char("do you want to write into a file or print your array? (w/p): ");
    if (type== 'w')
    {
    string name= get_string("How do you want to call your file: ");
    char filename[5];
    sprintf(filename, "%s.txt", name);
    FILE *file = fopen(filename, "w");
    for (int i=0; i< object; i++)
    {
        fprintf(file, "%i\n", naxuy[i]);
    }
    }
    if (type== 'p')
    {
        for (int i=0; i<object; i++)
        {
            printf ("%i\n", naxuy[i]);
        }
    }
}
