!!ARBfp1.0
# ARB_fragment_program generated by NVIDIA Cg compiler
# cgc version 1.2.0001, build date Feb 19 2004  12:16:25
# command line args: -profile arbfp1
#vendor NVIDIA Corporation
#version 1.0.02
#profile arbfp1
#program main
#semantic main.xcenter : C0
#semantic main.ycenter : C1
#semantic main.swirl_radius : C2
#semantic main.twist_effect : C3
#semantic main.texture
#var float xcenter : C0 : c[0] : 1 : 1
#var float ycenter : C1 : c[1] : 2 : 1
#var float swirl_radius : C2 : c[2] : 3 : 1
#var float twist_effect : C3 : c[3] : 4 : 1
#var sampler2D texture :  : texunit 0 : 5 : 1
#var float2 uv : $vin.TEXCOORD0 : TEX0 : 0 : 1
#var half4 main : $vout.COLOR : COL : -1 : 1
PARAM u0 = program.local[0];
PARAM u1 = program.local[1];
PARAM u2 = program.local[2];
PARAM u3 = program.local[3];
PARAM c0 = {0, 0, 0, 1};
PARAM c1 = {1e-07, 0.99921381, -0.32117498, 0.14626446};
PARAM c2 = {-0.038986512, 2, -1, 0};
PARAM c3 = {0, 3.1415927, 1.5707964, 1.5707964};
TEMP R0;
TEMP R1;
TEMP R2;
TEMP R3;
TEMP R4;
TEMP H0;
TEX R0, fragment.texcoord[0], texture[0], 2D;
ADD R1.x, fragment.texcoord[0].y, -u1.x;
ADD R1.x, R1.x, c1.x;
ADD R1.y, fragment.texcoord[0].x, -u0.x;
ADD R1.y, R1.y, c1.x;
ADD R1.z, R1.x, -R1.y;
CMP H0.x, R1.z, c0.w, c0.x;
ADD R1.z, R1.x, R1.y;
CMP H0.y, R1.z, c0.x, c0.w;
MUL R1.z, H0.y, H0.x;
MOV R2.x, R1.z;
RCP R1.z, R1.y;
MUL R1.z, R1.x, R1.z;
ADD R1.w, R1.y, -R1.x;
CMP H0.x, R1.w, c0.w, c0.x;
ADD R1.w, -R1.y, -R1.x;
CMP H0.y, R1.w, c0.x, c0.w;
MUL R1.w, H0.y, H0.x;
MOV R2.y, R1.w;
ADD R1.w, R1.y, R1.x;
ADD R1.w, c0.x, -R1.w;
CMP H0.x, R1.w, c0.w, c0.x;
MOV R3.x, R1.z;
MOV R3.y, R1.z;
ADD R1.z, R1.x, -R1.y;
CMP H0.y, R1.z, c0.x, c0.w;
MUL R1.z, H0.y, H0.x;
MOV R2.z, R1.z;
RCP R1.z, R1.x;
MUL R1.z, -R1.y, R1.z;
MOV R3.z, R1.z;
ADD R1.z, R1.y, R1.x;
CMP H0.x, R1.z, c0.w, c0.x;
ADD R1.z, R1.y, -R1.x;
CMP H0.y, R1.z, c0.x, c0.w;
MUL R1.z, H0.y, H0.x;
MOV R2.w, R1.z;
MOV R4.xyz, R3;
MOV R4.w, R3.z;
DP4 R1.z, R4, R2;
DP4 R1.w, c3, R2;
MUL R2.x, c2.x, R1.z;
MAD R2.x, R2.x, R1.z, c1.w;
MUL R2.x, R2.x, R1.z;
MAD R2.x, R2.x, R1.z, c1.z;
MUL R2.x, R2.x, R1.z;
MAD R2.x, R2.x, R1.z, c1.y;
ADD R2.y, R1.x, -c0.x;
CMP H0.x, R2.y, c0.x, c0.w;
MAD R2.y, H0.x, c2.y, c2.z;
MUL R1.w, R2.y, R1.w;
MAD R1.w, R2.x, R1.z, R1.w;
MUL R1.x, R1.x, R1.x;
MAD R1.x, R1.y, R1.y, R1.x;
RSQ R1.x, R1.x;
RCP R1.x, R1.x;
MOV R1.y, u2.x;
MAD R1.y, -c0.w, R1.x, R1.y;
MAD R1.w, -R1.y, u3.x, R1.w;
MUL R1.x, c0.w, R1.x;
COS R1.y, R1.w;
MAD R1.y, R1.x, R1.y, u0.x;
SIN R1.w, R1.w;
MAD R1.w, R1.x, R1.w, u1.x;
MOV R2.x, R1.y;
MOV R2.y, R1.w;
ADD R1.x, R1.x, -u2.x;
CMP H0.x, R1.x, c0.w, c0.x;
ADD H0.x, -H0.x, c0.w;
TEX R1, R2, texture[0], 2D;
CMP R0.xyz, -H0.x, R0, R1;
MOV result.color.xyz, R0;
MOV result.color.w, c0.w;
END
# 73 instructions, 5 R-regs, 1 H-regs.
# End of program