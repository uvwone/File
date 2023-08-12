#include <iostream>

using namespace std;

int main()
{
    FILE *fp;

    fp = fopen("C:\\temp\\f.txt", "r");
    if(fp == NULL)
    {
        cerr << "f.txt open error";
        return -1;
    }

    for(int ch; (ch=getc(fp)) != -1; )
    {
        if(islower(ch)) ch = toupper(ch);
        else if(isupper(ch)) ch = tolower(ch);

        cout << (char)ch;
    }

    fclose(fp);
    return 0;
}
