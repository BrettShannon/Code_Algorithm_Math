# include <stdio.h> // 包含标准输入输出库
int main(void) // 主函数
{
    int num; // 声明一个整数变量
    num = 1; // 给变量赋值

    printf("I am a simple "); // 打印字符串
    printf("computer.\n"); // 打印字符串并换行
    printf("My favorite number is %d.\n", num); // 打印字符串和变量值

    getchar(); // 等待用户输入任意字符后程序结束
    return 0; // 返回0表示程序正常结束
}