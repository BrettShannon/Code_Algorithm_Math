/*
# include <stdio.h> //header file

int main() //main function
{
    printf("Hello\n");
    printf("World\n");
    printf("\n");
}
*/

/*
#include <stdio.h>

int main()
{
    printf("Hello\n");
    printf("World\n");
    printf("\n");
    
    return 0;
}
*/

#include <stdio.h>

int main(void)
{
    printf("Hello\n");
    printf("World\n");

    fflush(stdout);               // 保证输出立即显示
    printf("\nPress Enter to exit...");
    getchar();                     // 等待按回车，防止终端关闭

    return 0;                      // 程序正常结束
}
