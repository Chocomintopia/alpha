// UVa 272
// 在TeX中，左双引号的"``",右双引号是"''"。
// 输入一篇包含双引号的文章，你的任务是把它转换成TeX的格式。

#include<stdio.h>
#include<string.h>

int main(){
    char quote_left[] = "``";   //不需要转义字符
    char quote_right[] = "''";
    bool flag = 1;
    //char s1[999], s2[999];
    //memset(s1, '\0', sizeof(s1));   //原文本
    //memset(s1, '\0', sizeof(s2));   //修改后的文本
    //scanf("%s", s1); 
    //本题不能使用scanf，因为遇到空格/TAB/换行符就会停止输入；
    //本题不需要存储，边读边处理，使用getchar，输入结束之后ctrl+z，Enter

    char c;
    while((c = getchar()) != EOF){
        if(c=='"')
            //左引号
            if(flag)    { printf(quote_left); flag = !flag; }
            //右引号
            else    {printf(quote_right); flag = !flag; }
            //这段使用 printf("%s", flag ? "``" : "''"); flag = !flag; 会更好
        else    printf("%c", c);
 
    }
    return 0;
}