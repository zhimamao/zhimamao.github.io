// gcc -S SourceCode.c -o TargetCode.s
#include <stdio.h>

int main() {
  int i = 0;
  double x = 2;
  double sum = 0;
  while (i++ < 100) {
    sum += x*x;
  }
  printf("The sum is %f\n", sum);
}
