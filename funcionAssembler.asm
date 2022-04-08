
segment .text
    global calc

calc:

    enter 0,0
    mov eax, [ebp+8]       ;almacenamos en ebx el bitcoin en dolares      
    mul DWORD [ebp+12]     ;multiplicamos por la tasa 

  
    leave
    ret
