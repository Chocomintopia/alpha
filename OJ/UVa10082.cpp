// UVa10082
// 把手放在键盘上，稍不注意就会往右错一位。这样，输入Q会变成输入W，输入J会变成输入K等。
// 输入一个错位后敲出来的字符串（所有字母均大写），
// 输出打字员本来想打出的矩阵输入保证合法，即一定是错位之后的字符串。
// 例如输入中不会出现大写字母A。

// 多行输入 每行包括数字，空格，大写字母（除了Q，A，Z）或者是标点符号
// （除了“'”(L右面第2个)），标有单词的按键，如Tab，BackSp，Control等等不会出现

// 你需要用每个字母或者符号左面的（在如图给出的QWERTY类型的键盘）
// 那个按键内容替换他，输入的空格不作处理，依然输出空格

#include<stdio.h>
#include<string.h>

int main(){
    char s[] = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./";
    char c;
    while((c = getchar()) != EOF){
        for(int i=0; i<strlen(s); i++){
            if(s[i]==c) { putchar(s[i-1]); break; }
            else if(i==strlen(s)-1) putchar(c);
        }
    }
    return 0;
}