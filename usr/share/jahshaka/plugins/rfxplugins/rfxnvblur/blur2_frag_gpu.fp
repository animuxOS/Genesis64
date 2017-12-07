!!FP1.0
# NV_fragment_program generated by NVIDIA Cg compiler
# cgc version 1.2.0001, build date Feb 19 2004  12:16:25
# command line args: -profile fp30
#vendor NVIDIA Corporation
#version 1.0.02
#profile fp30
#program main
#semantic main.texture : TEXUNIT0
#semantic main.texture2 : TEXUNIT1
#var sampler2D texture : TEXUNIT0 : texunit 0 : 2 : 1
#var sampler2D texture2 : TEXUNIT1 : texunit 1 : 3 : 1
#var float2 position : $vin.TEXCOORD0 : TEX0 : 0 : 1
#var float2 position2 : $vin.TEXCOORD1 : TEX1 : 1 : 1
#var half4 main : $vout.COLOR : COL : -1 : 1
TEX R0, f[TEX0].xyxx, TEX0, 2D;
ADDR R1.xy, f[TEX1].xyxx, {1}.x;
MULR R2.xy, R1.xyxx, {0.25}.x;
TEX R2, R2.xyxx, TEX1, 2D;
ADDR R2, R0, R2;
MADR R1.xy, R1.xyxx, {0.25}.x, {0.001}.x;
ADDR R0.xy, R1.xyxx, {0.001}.x;
TEX R1, R1.xyxx, TEX1, 2D;
TEX R3, R0.xyxx, TEX1, 2D;
ADDR R1, R2, R1;
ADDR R3, R1, R3;
ADDR R0.xy, R0.xyxx, {0.001}.x;
ADDR R1.xy, R0.xyxx, {0.001}.x;
TEX R0, R0.xyxx, TEX1, 2D;
TEX R2, R1.xyxx, TEX1, 2D;
ADDR R0, R3, R0;
ADDR R2, R0, R2;
ADDR R1.xy, R1.xyxx, {0.001}.x;
ADDR R0.xy, R1.xyxx, {0.001}.x;
TEX R1, R1.xyxx, TEX1, 2D;
TEX R0, R0.xyxx, TEX1, 2D;
ADDR R1, R2, R1;
ADDR R0, R1, R0;
ADDR R1.xy, f[TEX1].xyxx, {1}.x;
MADR R1.xy, R1.xyxx, {0.25}.x, -{0.001}.x;
ADDR R2.xy, R1.xyxx, -{0.001}.x;
TEX R1, R1.xyxx, TEX1, 2D;
TEX R3, R2.xyxx, TEX1, 2D;
ADDR R1, R0, R1;
ADDR R3, R1, R3;
ADDR R2.xy, R2.xyxx, -{0.001}.x;
ADDR R0.xy, R2.xyxx, -{0.001}.x;
TEX R1, R2.xyxx, TEX1, 2D;
TEX R0, R0.xyxx, TEX1, 2D;
ADDR R1, R3, R1;
ADDR R0, R1, R0;
MULR o[COLH], R0, {0.083333336}.x;
END
# 37 instructions, 4 R-regs, 0 H-regs.
# End of program
