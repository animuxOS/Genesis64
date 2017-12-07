!!FP1.0
# NV_fragment_program generated by NVIDIA Cg compiler
# cgc version 1.2.0001, build date Feb 19 2004  12:16:25
# command line args: -profile fp30
#vendor NVIDIA Corporation
#version 1.0.02
#profile fp30
#program main
#semantic main.BaseTexture : TEXUNIT0
#semantic main.contrastTexture : TEXUNIT1
#semantic main.randomTexture : TEXUNIT2
#semantic main.light_color : C0
#var sampler2D BaseTexture : TEXUNIT0 : texunit 0 : 5 : 1
#var sampler2D contrastTexture : TEXUNIT1 : texunit 1 : 6 : 1
#var sampler2D randomTexture : TEXUNIT2 : texunit 2 : 7 : 1
#var float4 light_color : C0 :  : 8 : 1
#var float2 base_uv : $vin.TEXCOORD0 : TEX0 : 0 : 1
#var float4 light1Position : $vin.TEXCOORD1 : TEX1 : 1 : 1
#var float edge : $vin.TEXCOORD2 : TEX2 : 2 : 1
#var float2 random_uv : $vin.TEXCOORD3 : TEX3 : 3 : 1
#var float2 contrast_uv : $vin.TEXCOORD4 : TEX4 : 4 : 1
#var float4 color : $vout.COLOR : COL : 9 : 1
DECLARE light_color;
TEX R0, f[TEX0].xyxx, TEX0, 2D;
MULR R0, f[TEX2].x, R0;
MULR o[COLR], R0, light_color;
END
# 3 instructions, 1 R-regs, 0 H-regs.
# End of program