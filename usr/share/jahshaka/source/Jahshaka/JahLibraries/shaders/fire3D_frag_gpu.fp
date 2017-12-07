!!FP1.0
# NV_fragment_program generated by NVIDIA Cg compiler
# cgc version 1.2.0001, build date Feb 19 2004  12:16:25
# command line args: -profile fp30
#vendor NVIDIA Corporation
#version 1.0.02
#profile fp30
#program main
#semantic main.scale_factor : C0
#semantic main.distortion : C1
#semantic main.time : C2
#semantic main.timescale : C3
#semantic main.gradient : C4
#semantic main.cosine_factor : C5
#semantic main.base_scale_factor : C6
#semantic main.turbulence_texture : TEXUNIT0
#semantic main.base_texture : TEXUNIT1
#var float2 scale_factor : C0 :  : 2 : 1
#var float2 distortion : C1 :  : 3 : 1
#var float time : C2 :  : 4 : 1
#var float timescale : C3 :  : 5 : 1
#var float gradient : C4 :  : 6 : 1
#var float cosine_factor : C5 :  : 7 : 1
#var float2 base_scale_factor : C6 :  : 8 : 1
#var sampler2D turbulence_texture : TEXUNIT0 : texunit 0 : 9 : 1
#var sampler2D base_texture : TEXUNIT1 : texunit 1 : 10 : 1
#var float2 position : $vin.TEXCOORD0 : TEX0 : 0 : 1
#var float2 noise_position : $vin.TEXCOORD1 : TEX1 : 1 : 1
#var half4 main : $vout.COLOR : COL : -1 : 1
DECLARE scale_factor;
DECLARE distortion;
DECLARE time;
DECLARE timescale;
DECLARE gradient;
DECLARE cosine_factor;
DECLARE base_scale_factor;
RCPR R0.x, timescale.x;
MULR R0.x, time.x, R0.x;
MULR R0.x, R0.x, cosine_factor.x;
ADDR R0.xy, -R0.x, f[TEX1].xyxx;
COSR R0.w, R0.y;
COSR R0.x, R0.x;
RCPR R0.y, timescale.x;
MULR R0.y, time.x, R0.y;
ADDR R1.xy, -R0.y, f[TEX1].xyxx;
MOVR R2.y, R0.w;
MOVR R2.x, R0.x;
MOVR R2.xy, |R2.xyxx|;
MOVR R0.x, {0}.x;
SEQR H0.x, cosine_factor.x, R0.x;
MOVXC HC.x, H0.x;
MOVR R2.xy(GT.x), {1, 1}.xyxx;
SINR R0.x, R1.y;
SINR R0.y, R1.x;
MOVR R1.y, R0.x;
MOVR R1.x, R0.y;
MADR R2.xy, |R1.xyxx|, |R2.xyxx|, {0.1}.x;
MULR R2.xy, R2.xyxx, scale_factor.xyxx;
MULR R2.xy, R2.xyxx, {0.89999998}.x;
TEX R0.x, R2.xyxx, TEX0, 2D;
MULR R0.xy, R0.x, distortion.xyxx;
MULR R0.xy, R0.xyxx, {0.050000001}.x;
MOVR R0.w, gradient.x;
ADDR R0.w, {1}.x, -R0.w;
MADR R0.w, R0.w, f[TEX0].y, gradient.x;
MADR R0.xy, R0.xyxx, R0.w, f[TEX0].xyxx;
SGTR H0.x, R0.y, base_scale_factor.y;
SGTR H0.y, R0.x, base_scale_factor.x;
ADDX H0.x, H0.y, H0.x;
MINX H0.x, H0.x, {1}.x;
MOVXC HC.x, H0.x;
MOVR R0.x(GT.x), base_scale_factor.x;
MOVXC HC.x, H0.x;
MOVR R0.y(GT.x), base_scale_factor.y;
SLER H0.x, R0.y, {0}.x;
SLER H0.y, R0.x, {0}.x;
ADDX H0.x, H0.y, H0.x;
MINX H0.x, H0.x, {1}.x;
MOVXC HC.x, H0.x;
MOVR R0.x(GT.x), {0.0020000001}.x;
MOVXC HC.x, H0.x;
MOVR R0.y(GT.x), {0.0020000001}.x;
TEX o[COLH], R0.xyxx, TEX1, 2D;
END
# 47 instructions, 3 R-regs, 1 H-regs.
# End of program
