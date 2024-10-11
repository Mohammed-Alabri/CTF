* challange ```Ldr```
* In this challange we got elf file to exucute shellcodes and a shellcode file, running the file will asks for flag to be entered.

* I use an online shellcode disassembler to return this code to assembly https://defuse.ca/online-x86-assembler.htm.
```asm

00000000  55                push rbp
00000001  4889E5            mov rbp,rsp
00000004  4883EC48          sub rsp,byte +0x48
00000008  4889BD48FFFFFF    mov [rbp-0xb8],rdi
0000000F  48B85B2A5D205374  mov rax,0x72617453205d2a5b
         -6172
00000019  48BA74696E672074  mov rdx,0x206f7420676e6974
         -6F20
00000023  488945D0          mov [rbp-0x30],rax
00000027  488955D8          mov [rbp-0x28],rdx
0000002B  48B8636865636B20  mov rax,0x6874206b63656863
         -7468
00000035  48BA6520666C6167  mov rdx,0x2e2e67616c662065
         -2E2E
0000003F  488945E0          mov [rbp-0x20],rax
00000043  488955E8          mov [rbp-0x18],rdx
00000047  66C745F02E0A      mov word [rbp-0x10],0xa2e
0000004D  488D4DD0          lea rcx,[rbp-0x30]
00000051  48C7C001000000    mov rax,0x1
00000058  48C7C701000000    mov rdi,0x1
0000005F  4889CE            mov rsi,rcx
00000062  48C7C222000000    mov rdx,0x22
00000069  0F05              syscall
0000006B  48B86E6671805551  mov rax,0x184a51558071666e
         -4A18
00000075  48BA807815058015  mov rdx,0x806f158005157880
         -6F80
0000007F  48894590          mov [rbp-0x70],rax
00000083  48895598          mov [rbp-0x68],rdx
00000087  48B81C6905628061  mov rax,0x5b7061806205691c
         -705B
00000091  48BA80596D567C80  mov rdx,0x8016807c566d5980
         -1680
0000009B  488945A0          mov [rbp-0x60],rax
0000009F  488955A8          mov [rbp-0x58],rdx
000000A3  48B87C711C6D4D6C  mov rax,0x65196c4d6d1c717c
         -1965
000000AD  48BA1C806C514A6D  mov rdx,0x1c4d6d4a516c801c
         -4D1C
000000B7  488945B0          mov [rbp-0x50],rax
000000BB  488955B8          mov [rbp-0x48],rdx
000000BF  48B84D1C4F684669  mov rax,0x4f526946684f1c4d
         -524F
000000C9  48BA5C524851550F  mov rdx,0x4e500f555148525c
         -504E
000000D3  488945BE          mov [rbp-0x42],rax
000000D7  488955C6          mov [rbp-0x3a],rdx
000000DB  C745FC00000000    mov dword [rbp-0x4],0x0
000000E2  EB04              jmp short 0xe8
000000E4  8345FC01          add dword [rbp-0x4],byte +0x1
000000E8  8B45FC            mov eax,[rbp-0x4]
000000EB  4863D0            movsxd rdx,eax
000000EE  488B8548FFFFFF    mov rax,[rbp-0xb8]
000000F5  4801D0            add rax,rdx
000000F8  0FB600            movzx eax,byte [rax]
000000FB  84C0              test al,al
000000FD  75E5              jnz 0xe4
000000FF  837DFC3E          cmp dword [rbp-0x4],byte +0x3e
00000103  0F8490000000      jz near 0x199
00000109  48B85B2D5D205468  mov rax,0x20656854205d2d5b
         -6520
00000113  48BA73697A65206F  mov rdx,0x20666f20657a6973
         -6620
0000011D  48898550FFFFFF    mov [rbp-0xb0],rax
00000124  48899558FFFFFF    mov [rbp-0xa8],rdx
0000012B  48B874686520656E  mov rax,0x65746e6520656874
         -7465
00000135  48BA72656420666C  mov rdx,0x67616c6620646572
         -6167
0000013F  48898560FFFFFF    mov [rbp-0xa0],rax
00000146  48899568FFFFFF    mov [rbp-0x98],rdx
0000014D  48B8206973206E6F  mov rax,0x20746f6e20736920
         -7420
00000157  48BA636F72726563  mov rdx,0x2e74636572726f63
         -742E
00000161  48898570FFFFFF    mov [rbp-0x90],rax
00000168  48899578FFFFFF    mov [rbp-0x88],rdx
0000016F  C645800A          mov byte [rbp-0x80],0xa
00000173  488D8D50FFFFFF    lea rcx,[rbp-0xb0]
0000017A  48C7C001000000    mov rax,0x1
00000181  48C7C701000000    mov rdi,0x1
00000188  4889CE            mov rsi,rcx
0000018B  48C7C231000000    mov rdx,0x31
00000192  0F05              syscall
00000194  E906010000        jmp 0x29f
00000199  66C745FA0000      mov word [rbp-0x6],0x0
0000019F  C745F400000000    mov dword [rbp-0xc],0x0
000001A6  EB3C              jmp short 0x1e4
000001A8  8B45F4            mov eax,[rbp-0xc]
000001AB  4863D0            movsxd rdx,eax
000001AE  488B8548FFFFFF    mov rax,[rbp-0xb8]
000001B5  4801D0            add rax,rdx
000001B8  0FB600            movzx eax,byte [rax]
000001BB  83F024            xor eax,byte +0x24
000001BE  0FBEC0            movsx eax,al
000001C1  8D5005            lea edx,[rax+0x5]
000001C4  8B45F4            mov eax,[rbp-0xc]
000001C7  4898              cdqe
000001C9  0FB6440590        movzx eax,byte [rbp+rax-0x70]
000001CE  0FB6C0            movzx eax,al
000001D1  39C2              cmp edx,eax
000001D3  7517              jnz 0x1ec
000001D5  8345F401          add dword [rbp-0xc],byte +0x1
000001D9  0FB745FA          movzx eax,word [rbp-0x6]
000001DD  83C001            add eax,byte +0x1
000001E0  668945FA          mov [rbp-0x6],ax
000001E4  837DF43E          cmp dword [rbp-0xc],byte +0x3e
000001E8  75BE              jnz 0x1a8
000001EA  EB01              jmp short 0x1ed
000001EC  90                nop
000001ED  66837DFA3E        cmp word [rbp-0x6],byte +0x3e
000001F2  7535              jnz 0x229
000001F4  48B85B2B5D204E6F  mov rax,0x63696f4e205d2b5b
         -6963
000001FE  48894585          mov [rbp-0x7b],rax
00000202  C7458C6365210A    mov dword [rbp-0x74],0xa216563
00000209  488D4D85          lea rcx,[rbp-0x7b]
0000020D  48C7C001000000    mov rax,0x1
00000214  48C7C701000000    mov rdi,0x1
0000021B  4889CE            mov rsi,rcx
0000021E  48C7C20B000000    mov rdx,0xb
00000225  0F05              syscall
00000227  EB76              jmp short 0x29f
00000229  48B85B2D5D205468  mov rax,0x20656854205d2d5b
         -6520
00000233  48BA656E74657265  mov rdx,0x2064657265746e65
         -6420
0000023D  48898550FFFFFF    mov [rbp-0xb0],rax
00000244  48899558FFFFFF    mov [rbp-0xa8],rdx
0000024B  48B8666C61672069  mov rax,0x2073692067616c66
         -7320
00000255  48BA6E6F7420636F  mov rdx,0x72726f6320746f6e
         -7272
0000025F  48898560FFFFFF    mov [rbp-0xa0],rax
00000266  48899568FFFFFF    mov [rbp-0x98],rdx
0000026D  48B86F7272656374  mov rax,0xa2e74636572726f
         -2E0A
00000277  4889856DFFFFFF    mov [rbp-0x93],rax
0000027E  488D8D50FFFFFF    lea rcx,[rbp-0xb0]
00000285  48C7C001000000    mov rax,0x1
0000028C  48C7C701000000    mov rdi,0x1
00000293  4889CE            mov rsi,rcx
00000296  48C7C225000000    mov rdx,0x25
0000029D  0F05              syscall
0000029F  C9                leave
000002A0  C3                ret
```

* Then I put this code again in Online Assembly to C Converter tool.
* https://www.codeconvert.ai/assembly-to-c-converter
```c
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char message1[] = "[*] Starting to check the flag...\n";
    char message2[] = "[-] The size of the entered flag is not correct.\n";
    char message3[] = "[+] Nice!\n";
    char message4[] = "[-] The entered flag is not correct.\n";
    
    char flag[] = {
        0x6e, 0x66, 0x71, 0x80, 0x55, 0x51, 0x4A, 0x18, 0x80, 0x78, 0x15, 0x05, 0x80, 0x15, 0x6F, 0x80,
        0x1C, 0x69, 0x05, 0x62, 0x80, 0x61, 0x70, 0x5B, 0x80, 0x59, 0x6D, 0x56, 0x7C, 0x80, 0x16, 0x80,
        0x7C, 0x71, 0x1C, 0x6D, 0x4D, 0x6C, 0x19, 0x65, 0x1C, 0x80, 0x6C, 0x51, 0x4A, 0x6D, 0x4D, 0x1C,
        0x4D, 0x1C, 0x4F, 0x68, 0x46, 0x69, 0x52, 0x4F, 0x5C, 0x52, 0x48, 0x51, 0x55, 0x0F, 0x50, 0x4E
    };

    printf("%s", message1);

    if (strlen(argv[1]) != 62) {
        printf("%s", message2);
        return 0;
    }

    int correct_chars = 0;
    for (int i = 0; i < 62; i++) {
        if (((argv[1][i] ^ 0x24) + 5) == flag[i]) {
            correct_chars++;
        }
    }

    if (correct_chars == 62) {
        printf("%s", message3);
    } else {
        printf("%s", message4);
    }

    return 0;
}
```

* the program looping through the entered flag (length=62) and xor it with 0x24 and add 5 and compare it with encrpyted flag

* I made this code to decrypt the flag
```python
flag = b"\x6e\x66\x71\x80\x55\x51\x4A\x18\x80\x78\x15\x05\x80\x15\x6F\x80\x1C\x69\x05\x62\x80\x61\x70\x5B\x80\x59\x6D\x56\x7C\x80\x16\x80\x7C\x71\x1C\x6D\x4D\x6C\x19\x65\x1C\x80\x6C\x51\x4A\x6D\x4D\x1C\x4D\x1C\x4F\x68\x46\x69\x52\x4F\x5C\x52\x48\x51\x55\x0F\x50\x4E"


# bruteforce way
res = ""
for char in flag:
    for i in range(256):
        if (i ^ 0x24) + 5 == char:
            res += chr(i)

print(res)

# rev way
res = ""
for char in flag:
    res += chr(char - 5 ^ 0x24)

print(res)
```

* Flag ```MEH_tha7_W4$_4N_3@$y_xOr_pLuS_5_SH3LlC0D3_ChaLl3l3nGe@insight.om```