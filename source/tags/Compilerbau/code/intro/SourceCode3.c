// cpp SourceCode3.c > SourceCode3.i
// gcc -S SourceCode3.i
// as -o SourceCode3.o SourceCode3.s
// ld -o SourceCode3 SourceCode3.o

#define CUBE(x) (x)*(x)*(x)
int main() {
  int i = 0;
  int x = 2;
  int sum = 0;
  while (i++ < 100) {
    sum += CUBE(x);
  }
  //printf("The sum is %d\n", sum);
}
