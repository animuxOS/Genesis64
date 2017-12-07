!!ARBfp1.0
# ARB_fragment_program generated by NVIDIA Cg compiler
# cgc version 1.2.1001, build date Mar 17 2004  10:32:28
# command line args: -profile arbfp1
#vendor NVIDIA Corporation
#version 1.0.02
#profile arbfp1
#program main
#semantic main.horizontal : C0
#semantic main.vertical : C1
#semantic main.stretch : C2
#semantic main.blend : C3
#semantic main.transparency : C4
#semantic main.weight : C5
#semantic main.texture : TEXUNIT0
#var float horizontal : C0 : c[0] : 1 : 1
#var float vertical : C1 : c[1] : 2 : 1
#var float stretch : C2 : c[2] : 3 : 1
#var float blend : C3 : c[3] : 4 : 1
#var float transparency : C4 : c[4] : 5 : 1
#var float weight : C5 : c[5] : 6 : 1
#var sampler2D texture : TEXUNIT0 : texunit 0 : 7 : 1
#var float2 position : $vin.TEXCOORD0 : TEX0 : 0 : 1
#var half4 main : $vout.COLOR : COL : -1 : 1
PARAM u0 = program.local[0];
PARAM u1 = program.local[1];
PARAM u2 = program.local[2];
PARAM u3 = program.local[3];
PARAM u4 = program.local[4];
PARAM u5 = program.local[5];
PARAM c0 = {1, 0, 2, 0};
TEMP R0;
TEMP R1;
TEMP R2;
TEMP R3;
TEMP R4;
TEMP R5;
TEMP R6;
TEMP R7;
TEMP H0;
TEMP H1;
TEX R0, fragment.texcoord[0], texture[0], 2D;
MOV R1.x, u0.x;
ADD R1.x, c0.y, -R1.x;
CMP H0.x, R1.x, c0.x, c0.y;
MOV R1.x, u1.x;
ADD R1.x, c0.y, -R1.x;
CMP H0.y, R1.x, c0.x, c0.y;
ADD H0.y, H0.x, H0.y;
MIN H0.y, H0.y, c0.x;
MOV R1.x, u0.x;
ADD R1.x, c0.y, -R1.x;
CMP H0.x, R1.x, c0.x, c0.y;
MUL H0.x, H0.y, H0.x;
ADD R1.x, fragment.texcoord[0].x, u2.x;
MOV R2.y, fragment.texcoord[0];
CMP R2.x, -H0.x, R1, fragment.texcoord[0];
MOV R1.x, u1.x;
ADD R1.x, c0.y, -R1.x;
CMP H0.z, R1.x, c0.x, c0.y;
MUL H0.z, H0.y, H0.z;
TEX R1, R2, texture[0], 2D;
MAD R1, R1, u5.x, R0;
CMP H1, -H0.x, R1, R0;
ADD R1.x, fragment.texcoord[0].x, -u2.x;
MOV R3.y, fragment.texcoord[0];
CMP R3.x, -H0.x, R1, fragment.texcoord[0];
MOV R1.x, u0.x;
ADD R1.x, c0.x, -R1.x;
CMP H0.y, R1.x, c0.x, c0.y;
MOV R1.x, u1.x;
ADD R1.x, c0.x, -R1.x;
CMP H0.w, R1.x, c0.x, c0.y;
ADD H0.w, H0.y, H0.w;
MIN H0.w, H0.w, c0.x;
TEX R1, R3, texture[0], 2D;
MAD R1, R1, u5.x, H1;
CMP H1, -H0.x, R1, H1;
CMP R1.x, -H0.x, c0.x, c0.y;
ADD R4.x, fragment.texcoord[0].y, u2.x;
MOV R5.x, fragment.texcoord[0];
CMP R5.y, -H0.z, R4.xxzw, fragment.texcoord[0];
MOV R1.y, u0.x;
ADD R1.y, c0.x, -R1.y;
CMP H0.x, R1.y, c0.x, c0.y;
MUL H0.x, H0.w, H0.x;
TEX R4, R5, texture[0], 2D;
MAD R4, R4, u5.x, H1;
CMP H1, -H0.z, R4, H1;
ADD R4.x, fragment.texcoord[0].y, -u2.x;
MOV R6.x, fragment.texcoord[0];
CMP R6.y, -H0.z, R4.xxzw, fragment.texcoord[0];
TEX R4, R6, texture[0], 2D;
MAD R4, R4, u5.x, H1;
CMP H1, -H0.z, R4, H1;
MOV R4.y, R2;
ADD R7.x, R2.x, u2.x;
CMP R4.x, -H0.x, R7, R2;
MOV R1.y, u1.x;
ADD R1.y, c0.x, -R1.y;
CMP H0.y, R1.y, c0.x, c0.y;
MUL H0.y, H0.w, H0.y;
TEX R2, R4, texture[0], 2D;
MAD R2, R2, u5.x, H1;
CMP H1, -H0.x, R2, H1;
MOV R2.y, R3;
ADD R7.x, R3.x, -u2.x;
CMP R2.x, -H0.x, R7, R3;
TEX R3, R2, texture[0], 2D;
MAD R3, R3, u5.x, H1;
CMP H1, -H0.x, R3, H1;
MOV R3.x, R5;
ADD R7.x, R5.y, u2.x;
CMP R3.y, -H0.y, R7.xxzw, R5;
TEX R5, R3, texture[0], 2D;
MAD R5, R5, u5.x, H1;
CMP H1, -H0.y, R5, H1;
MOV R5.x, R6;
ADD R7.x, R6.y, -u2.x;
CMP R5.y, -H0.y, R7.xxzw, R6;
ADD R1.y, R1.x, c0.x;
CMP R1.x, -H0.z, R1.y, R1.x;
MOV R1.y, u0.x;
ADD R1.y, c0.z, -R1.y;
CMP H0.z, R1.y, c0.x, c0.y;
MOV R1.y, u1.x;
ADD R1.y, c0.z, -R1.y;
CMP H0.w, R1.y, c0.x, c0.y;
ADD H0.w, H0.z, H0.w;
MIN H0.w, H0.w, c0.x;
ADD R1.y, R1.x, c0.x;
CMP R1.x, -H0.x, R1.y, R1.x;
TEX R6, R5, texture[0], 2D;
MAD R6, R6, u5.x, H1;
CMP H1, -H0.y, R6, H1;
MOV R6.y, R4.y;
ADD R1.y, R4.x, u2.x;
MOV R6.x, R1.y;
TEX R4, R6, texture[0], 2D;
MAD R4, R4, u5.x, H1;
MOV R1.y, u0.x;
ADD R1.y, c0.z, -R1.y;
CMP H0.x, R1.y, c0.x, c0.y;
MUL H0.x, H0.w, H0.x;
CMP H1, -H0.x, R4, H1;
ADD R1.y, R1.x, c0.x;
CMP R1.x, -H0.y, R1.y, R1.x;
MOV R4.y, R2.y;
ADD R1.y, R2.x, -u2.x;
MOV R4.x, R1.y;
TEX R2, R4, texture[0], 2D;
MAD R2, R2, u5.x, H1;
CMP H1, -H0.x, R2, H1;
MOV R1.y, u1.x;
ADD R1.y, c0.z, -R1.y;
CMP H0.y, R1.y, c0.x, c0.y;
MUL H0.y, H0.w, H0.y;
ADD R1.y, R1.x, c0.x;
CMP R1.x, -H0.x, R1.y, R1.x;
MOV R2.x, R3.x;
ADD R1.y, R3.y, u2.x;
MOV R2.y, R1.y;
TEX R2, R2, texture[0], 2D;
MAD R2, R2, u5.x, H1;
CMP H1, -H0.y, R2, H1;
ADD R1.y, R1.x, c0.x;
CMP R1.x, -H0.y, R1.y, R1.x;
MOV R2.x, R5.x;
ADD R1.y, R5.y, -u2.x;
MOV R2.y, R1.y;
TEX R2, R2, texture[0], 2D;
MAD R2, R2, u5.x, H1;
CMP H1, -H0.y, R2, H1;
MUL R1.y, R1.x, u5.x;
MAD R1.y, R1.y, c0.z, c0.x;
RCP R1.y, R1.y;
ADD R1.x, c0.y, -R1.x;
CMP H0.x, R1.x, c0.x, c0.y;
MUL R1, H1, R1.y;
CMP H1, -H0.x, R1, H1;
MOV R1.x, u3.x;
ADD R1.x, c0.x, -R1.x;
MAD R1, R1.x, H1, u3.x;
MUL R2, u4.x, H1;
MOV R3.x, u4.x;
ADD R3.x, c0.x, -R3.x;
MUL R0, R3.x, R0;
MAD result.color, R2, R1, R0;
END
# 147 instructions, 8 R-regs, 2 H-regs.
# End of program