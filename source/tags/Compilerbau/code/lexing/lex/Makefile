
all: a.out
	wc *.input
	time ./a.out <linear_bs.input 
	time ./a.out <linear_asb.input
	time ./a.out <quadratic.input
	time ./a.out <quadratic2.input

lex.yy.c:	quadratic.lex
	lex --verbose quadratic.lex

a.out:	lex.yy.c
	cc lex.yy.c

clean:
	rm ./*.out
	rm *.c

simple:
	lex --verbose simple.lex
	cc lex.yy.c -o simple.out