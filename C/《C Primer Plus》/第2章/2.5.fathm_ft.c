// fathm_ft.c -- 把2英寻转换成英尺
#include <stdio.h>
int main(void)
{
    int feet, fathoms; // 英尺和英寻

    fathoms = 2; // 2英寻
    feet = fathoms * 6; // 1英寻 = 6英尺
    printf("There are %d feet in %d fathoms!\n", feet, fathoms);
    printf("Yes, I said %d feet!\n", 6 * fathoms);

    return 0;
}