myshell:
	nasm -f elf32 -d ELF_TYPE funcionAssembler.asm
	gcc  -o ejecutable funcionAssembler.o -m32 funcc.c 
clean:
	rm -f *.o *.so ejecutable


