
segment .data

segment .bss

segment .text
    global calc

calc:

    push ebp
    mov ebp,esp

    mov eax, [ebp+8]       ;almacenamos en ebx el bitcoin en dolares  
    mov edx, [ebp+12]    
    mul edx     ;multiplicamos por la tasa 

    pop ebp
    ret
