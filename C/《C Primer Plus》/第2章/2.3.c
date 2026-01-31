# include <stdio.h> // 这句是必须的，意思是包含标准输入输出库，方便使用printf函数，scanf函数，等等

int main(void) // main函数是程序的入口，程序从这里开始执行,void表示main函数没有返回值 ,void中文意思 是空
{
    int q; // 定义一个整数变量q
    printf("%d is neat. \n", q); // 输出q的值，并加上一句“ is neat. ”
    return 0; // 返回0，表示程序正常结束
}
