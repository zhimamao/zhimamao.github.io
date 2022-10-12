// gcc -S SourceCode.c -o TargetCode.s
#include <stdio.h>

int main() {
  int i = 0;
  int x = 2;
  int sum = 0;
  while (i++ < 100) {
    sum += x*x;
  }
  printf("The sum is %d\n", sum);
}
