#include <stdio.h>
#include <stdlib.h>

int foo(int x, int y){
    printf("you input %d and %d\n", x, y);
    return x+y;
}

// gcc -o libpycall.so -shared -fPIC pycall.c #.so 生成动态链接

// gcc main.c -L /root/lss/C/3-23/test1/lib -static -lmy -o main #.lib 静态链接库
// ar cqs test.a test.o #.a 静态库文件，由.o组成