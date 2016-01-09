#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'GPIO处理'
__author__ = 'kakake'

ASCII8x16={
#/*--  调入了一幅图像：这是您新建的图像  --*/
#/*--  宽度x高度=8x16  --*/
'32':[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
#/*--  文字:  !  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'33':[0x00,0x00,0x00,0x18,0x3C,0x3C,0x3C,0x18,0x18,0x00,0x18,0x18,0x00,0x00,0x00,0x00],

#/*--  文字:  "  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'34':[0x00,0x00,0x00,0x66,0x66,0x66,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],

#/*--  文字:  #  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'35':[0x00,0x00,0x00,0x36,0x36,0x7F,0x36,0x36,0x36,0x7F,0x36,0x36,0x00,0x00,0x00,0x00],

#/*--  文字:  $  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'36':[0x00,0x18,0x18,0x3C,0x66,0x60,0x30,0x18,0x0C,0x06,0x66,0x3C,0x18,0x18,0x00,0x00],

#/*--  文字:  %  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'37':[0x00,0x00,0x70,0xD8,0xDA,0x76,0x0C,0x18,0x30,0x6E,0x5B,0x1B,0x0E,0x00,0x00,0x00],

#/*--  文字:  &  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'38':[0x00,0x00,0x00,0x38,0x6C,0x6C,0x38,0x60,0x6F,0x66,0x66,0x3B,0x00,0x00,0x00,0x00],

#/*--  文字:  '  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'39':[0x00,0x00,0x00,0x18,0x18,0x18,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],

#/*--  文字:  (  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'40':[0x00,0x00,0x00,0x0C,0x18,0x18,0x30,0x30,0x30,0x30,0x30,0x18,0x18,0x0C,0x00,0x00],

#/*--  文字:  )  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'41':[0x00,0x00,0x00,0x30,0x18,0x18,0x0C,0x0C,0x0C,0x0C,0x0C,0x18,0x18,0x30,0x00,0x00],

#/*--  文字:  *  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'42':[0x00,0x00,0x00,0x00,0x00,0x36,0x1C,0x7F,0x1C,0x36,0x00,0x00,0x00,0x00,0x00,0x00],

#/*--  文字:  +  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'43':[0x00,0x00,0x00,0x00,0x00,0x18,0x18,0x7E,0x18,0x18,0x00,0x00,0x00,0x00,0x00,0x00],

#/*--  文字:  ,  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'44':[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1C,0x1C,0x0C,0x18,0x00,0x00],

#/*--  文字:  -  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'45':[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x7E,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],

#/*--  文字:  .  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'46':[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1C,0x1C,0x00,0x00,0x00,0x00],

#/*--  文字:  /  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'47':[0x00,0x00,0x00,0x06,0x06,0x0C,0x0C,0x18,0x18,0x30,0x30,0x60,0x60,0x00,0x00,0x00],
#  文字:  0  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'48':[0x00,0x00,0x00,0x1E,0x33,0x37,0x37,0x33,0x3B,0x3B,0x33,0x1E,0x00,0x00,0x00,0x00],

#  文字:  1  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'49':[0x00,0x00,0x00,0x0C,0x1C,0x7C,0x0C,0x0C,0x0C,0x0C,0x0C,0x0C,0x00,0x00,0x00,0x00],

#  文字:  2  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'50':[0x00,0x00,0x00,0x3C,0x66,0x66,0x06,0x0C,0x18,0x30,0x60,0x7E,0x00,0x00,0x00,0x00],

#  文字:  3  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'51':[0x00,0x00,0x00,0x3C,0x66,0x66,0x06,0x1C,0x06,0x66,0x66,0x3C,0x00,0x00,0x00,0x00],

#  文字:  4  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'52':[0x00,0x00,0x00,0x30,0x30,0x36,0x36,0x36,0x66,0x7F,0x06,0x06,0x00,0x00,0x00,0x00],

#  文字:  5  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'53':[0x00,0x00,0x00,0x7E,0x60,0x60,0x60,0x7C,0x06,0x06,0x0C,0x78,0x00,0x00,0x00,0x00],

#  文字:  6  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'54':[0x00,0x00,0x00,0x1C,0x18,0x30,0x7C,0x66,0x66,0x66,0x66,0x3C,0x00,0x00,0x00,0x00],

#  文字:  7  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'55':[0x00,0x00,0x00,0x7E,0x06,0x0C,0x0C,0x18,0x18,0x30,0x30,0x30,0x00,0x00,0x00,0x00],

#  文字:  8  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'56':[0x00,0x00,0x00,0x3C,0x66,0x66,0x76,0x3C,0x6E,0x66,0x66,0x3C,0x00,0x00,0x00,0x00],

#  文字:  9  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'57':[0x00,0x00,0x00,0x3C,0x66,0x66,0x66,0x66,0x3E,0x0C,0x18,0x38,0x00,0x00,0x00,0x00],
#/*--  文字:  :  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'58':[0x00,0x00,0x00,0x00,0x00,0x1C,0x1C,0x00,0x00,0x00,0x1C,0x1C,0x00,0x00,0x00,0x00],

#/*--  文字:  ;  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'59':[0x00,0x00,0x00,0x00,0x00,0x1C,0x1C,0x00,0x00,0x00,0x1C,0x1C,0x0C,0x18,0x00,0x00],

#/*--  文字:  <  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'60':[0x00,0x00,0x00,0x06,0x0C,0x18,0x30,0x60,0x30,0x18,0x0C,0x06,0x00,0x00,0x00,0x00],

#/*--  文字:  =  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'61':[0x00,0x00,0x00,0x00,0x00,0x00,0x7E,0x00,0x7E,0x00,0x00,0x00,0x00,0x00,0x00,0x00],

#/*--  文字:  >  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'62':[0x00,0x00,0x00,0x60,0x30,0x18,0x0C,0x06,0x0C,0x18,0x30,0x60,0x00,0x00,0x00,0x00],

#/*--  文字:  ?  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'63':[0x00,0x00,0x00,0x3C,0x66,0x66,0x0C,0x18,0x18,0x00,0x18,0x18,0x00,0x00,0x00,0x00],

#/*--  文字:  @  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'64':[0x00,0x00,0x00,0x7E,0xC3,0xC3,0xCF,0xDB,0xDB,0xCF,0xC0,0x7F,0x00,0x00,0x00,0x00],

#/*--  文字:  A  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'65':[0x00,0x00,0x00,0x18,0x3C,0x66,0x66,0x66,0x7E,0x66,0x66,0x66,0x00,0x00,0x00,0x00],

#/*--  文字:  B  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'66':[0x00,0x00,0x00,0x7C,0x66,0x66,0x66,0x7C,0x66,0x66,0x66,0x7C,0x00,0x00,0x00,0x00],

#/*--  文字:  C  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'67':[0x00,0x00,0x00,0x3C,0x66,0x66,0x60,0x60,0x60,0x66,0x66,0x3C,0x00,0x00,0x00,0x00],

#/*--  文字:  D  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'68':[0x00,0x00,0x00,0x78,0x6C,0x66,0x66,0x66,0x66,0x66,0x6C,0x78,0x00,0x00,0x00,0x00],

#/*--  文字:  E  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'69':[0x00,0x00,0x00,0x7E,0x60,0x60,0x60,0x7C,0x60,0x60,0x60,0x7E,0x00,0x00,0x00,0x00],

#/*--  文字:  F  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'70':[0x00,0x00,0x00,0x7E,0x60,0x60,0x60,0x7C,0x60,0x60,0x60,0x60,0x00,0x00,0x00,0x00],

#/*--  文字:  G  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'71':[0x00,0x00,0x00,0x3C,0x66,0x66,0x60,0x60,0x6E,0x66,0x66,0x3E,0x00,0x00,0x00,0x00],

#/*--  文字:  H  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'72':[0x00,0x00,0x00,0x66,0x66,0x66,0x66,0x7E,0x66,0x66,0x66,0x66,0x00,0x00,0x00,0x00],

#/*--  文字:  I  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'73':[0x00,0x00,0x00,0x3C,0x18,0x18,0x18,0x18,0x18,0x18,0x18,0x3C,0x00,0x00,0x00,0x00],

#/*--  文字:  J  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'74':[0x00,0x00,0x00,0x06,0x06,0x06,0x06,0x06,0x06,0x66,0x66,0x3C,0x00,0x00,0x00,0x00],

#/*--  文字:  K  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'75':[0x00,0x00,0x00,0x66,0x66,0x6C,0x6C,0x78,0x6C,0x6C,0x66,0x66,0x00,0x00,0x00,0x00],

#/*--  文字:  L  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'76':[0x00,0x00,0x00,0x60,0x60,0x60,0x60,0x60,0x60,0x60,0x60,0x7E,0x00,0x00,0x00,0x00],

#/*--  文字:  M  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'77':[0x00,0x00,0x00,0x63,0x63,0x77,0x6B,0x6B,0x6B,0x63,0x63,0x63,0x00,0x00,0x00,0x00],

#/*--  文字:  N  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'78':[0x00,0x00,0x00,0x63,0x63,0x73,0x7B,0x6F,0x67,0x63,0x63,0x63,0x00,0x00,0x00,0x00],

#/*--  文字:  O  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'79':[0x00,0x00,0x00,0x3C,0x66,0x66,0x66,0x66,0x66,0x66,0x66,0x3C,0x00,0x00,0x00,0x00],

#/*--  文字:  P  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'80':[0x00,0x00,0x00,0x7C,0x66,0x66,0x66,0x7C,0x60,0x60,0x60,0x60,0x00,0x00,0x00,0x00],

#/*--  文字:  Q  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'81':[0x00,0x00,0x00,0x3C,0x66,0x66,0x66,0x66,0x66,0x66,0x66,0x3C,0x0C,0x06,0x00,0x00],

#/*--  文字:  R  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'82':[0x00,0x00,0x00,0x7C,0x66,0x66,0x66,0x7C,0x6C,0x66,0x66,0x66,0x00,0x00,0x00,0x00],

#/*--  文字:  S  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'83':[0x00,0x00,0x00,0x3C,0x66,0x60,0x30,0x18,0x0C,0x06,0x66,0x3C,0x00,0x00,0x00,0x00],

#/*--  文字:  T  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'84':[0x00,0x00,0x00,0x7E,0x18,0x18,0x18,0x18,0x18,0x18,0x18,0x18,0x00,0x00,0x00,0x00],

#/*--  文字:  U  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'85':[0x00,0x00,0x00,0x66,0x66,0x66,0x66,0x66,0x66,0x66,0x66,0x3C,0x00,0x00,0x00,0x00],

#/*--  文字:  V  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'86':[0x00,0x00,0x00,0x66,0x66,0x66,0x66,0x66,0x66,0x66,0x3C,0x18,0x00,0x00,0x00,0x00],

#/*--  文字:  W  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'87':[0x00,0x00,0x00,0x63,0x63,0x63,0x6B,0x6B,0x6B,0x36,0x36,0x36,0x00,0x00,0x00,0x00],

#/*--  文字:  X  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'88':[0x00,0x00,0x00,0x66,0x66,0x34,0x18,0x18,0x2C,0x66,0x66,0x66,0x00,0x00,0x00,0x00],

#/*--  文字:  Y  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'89':[0x00,0x00,0x00,0x66,0x66,0x66,0x66,0x3C,0x18,0x18,0x18,0x18,0x00,0x00,0x00,0x00],

#/*--  文字:  Z  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'90':[0x00,0x00,0x00,0x7E,0x06,0x06,0x0C,0x18,0x30,0x60,0x60,0x7E,0x00,0x00,0x00,0x00],

#/*--  文字:  [  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'91':[0x00,0x00,0x00,0x3C,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x3C,0x00],

#/*--  文字:  \  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'92':[0x00,0x00,0x00,0x60,0x60,0x30,0x30,0x18,0x18,0x0C,0x0C,0x06,0x06,0x00,0x00,0x00],

#/*--  文字:  ]  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'93':[0x00,0x00,0x00,0x3C,0x0C,0x0C,0x0C,0x0C,0x0C,0x0C,0x0C,0x0C,0x0C,0x0C,0x3C,0x00],

#/*--  文字:  ^  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'94':[0x00,0x18,0x3C,0x66,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],

#/*--  文字:  _  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'95':[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFF,0x00],

#/*--  文字:  `  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'96':[0x00,0x38,0x18,0x0C,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],


#  文字:  a  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'97':[0x00,0x00,0x00,0x00,0x00,0x3C,0x06,0x06,0x3E,0x66,0x66,0x3E,0x00,0x00,0x00,0x00],

#  文字:  b  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'98':[0x00,0x00,0x00,0x60,0x60,0x7C,0x66,0x66,0x66,0x66,0x66,0x7C,0x00,0x00,0x00,0x00],

#  文字:  c  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'99':[0x00,0x00,0x00,0x00,0x00,0x3C,0x66,0x60,0x60,0x60,0x66,0x3C,0x00,0x00,0x00,0x00],

#  文字:  d  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'100':[0x00,0x00,0x00,0x06,0x06,0x3E,0x66,0x66,0x66,0x66,0x66,0x3E,0x00,0x00,0x00,0x00],

#  文字:  e  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'101':[0x00,0x00,0x00,0x00,0x00,0x3C,0x66,0x66,0x7E,0x60,0x60,0x3C,0x00,0x00,0x00,0x00],

#  文字:  f  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'102':[0x00,0x00,0x00,0x1E,0x30,0x30,0x30,0x7E,0x30,0x30,0x30,0x30,0x00,0x00,0x00,0x00],

#  文字:  g  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'103':[0x00,0x00,0x00,0x00,0x00,0x3E,0x66,0x66,0x66,0x66,0x66,0x3E,0x06,0x06,0x7C,0x00],

#  文字:  h  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'104':[0x00,0x00,0x00,0x60,0x60,0x7C,0x66,0x66,0x66,0x66,0x66,0x66,0x00,0x00,0x00,0x00],

#  文字:  i  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'105':[0x00,0x00,0x18,0x18,0x00,0x78,0x18,0x18,0x18,0x18,0x18,0x7E,0x00,0x00,0x00,0x00],

#  文字:  j  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'106':[0x00,0x00,0x0C,0x0C,0x00,0x3C,0x0C,0x0C,0x0C,0x0C,0x0C,0x0C,0x0C,0x0C,0x78,0x00],

#  文字:  k  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'107':[0x00,0x00,0x00,0x60,0x60,0x66,0x66,0x6C,0x78,0x6C,0x66,0x66,0x00,0x00,0x00,0x00],

#  文字:  l  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'108':[0x00,0x00,0x00,0x78,0x18,0x18,0x18,0x18,0x18,0x18,0x18,0x7E,0x00,0x00,0x00,0x00],

#  文字:  m  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'109':[0x00,0x00,0x00,0x00,0x00,0x7E,0x6B,0x6B,0x6B,0x6B,0x6B,0x63,0x00,0x00,0x00,0x00],

#  文字:  n  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'110':[0x00,0x00,0x00,0x00,0x00,0x7C,0x66,0x66,0x66,0x66,0x66,0x66,0x00,0x00,0x00,0x00],

#  文字:  o  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'111':[0x00,0x00,0x00,0x00,0x00,0x3C,0x66,0x66,0x66,0x66,0x66,0x3C,0x00,0x00,0x00,0x00],

#  文字:  p  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'112':[0x00,0x00,0x00,0x00,0x00,0x7C,0x66,0x66,0x66,0x66,0x66,0x7C,0x60,0x60,0x60,0x00],

#  文字:  q  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'113':[0x00,0x00,0x00,0x00,0x00,0x3E,0x66,0x66,0x66,0x66,0x66,0x3E,0x06,0x06,0x06,0x00],

#  文字:  r  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'114':[0x00,0x00,0x00,0x00,0x00,0x66,0x6E,0x70,0x60,0x60,0x60,0x60,0x00,0x00,0x00,0x00],

#  文字:  s  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'115':[0x00,0x00,0x00,0x00,0x00,0x3E,0x60,0x60,0x3C,0x06,0x06,0x7C,0x00,0x00,0x00,0x00],

#  文字:  t  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'116':[0x00,0x00,0x00,0x30,0x30,0x7E,0x30,0x30,0x30,0x30,0x30,0x1E,0x00,0x00,0x00,0x00],

#  文字:  u  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'117':[0x00,0x00,0x00,0x00,0x00,0x66,0x66,0x66,0x66,0x66,0x66,0x3E,0x00,0x00,0x00,0x00],

#  文字:  v  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'118':[0x00,0x00,0x00,0x00,0x00,0x66,0x66,0x66,0x66,0x66,0x3C,0x18,0x00,0x00,0x00,0x00],

#  文字:  w  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'119':[0x00,0x00,0x00,0x00,0x00,0x63,0x6B,0x6B,0x6B,0x6B,0x36,0x36,0x00,0x00,0x00,0x00],

#  文字:  x  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'120':[0x00,0x00,0x00,0x00,0x00,0x66,0x66,0x3C,0x18,0x3C,0x66,0x66,0x00,0x00,0x00,0x00],

#  文字:  y  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'121':[0x00,0x00,0x00,0x00,0x00,0x66,0x66,0x66,0x66,0x66,0x66,0x3C,0x0C,0x18,0xF0,0x00],

#  文字:  z  --*/
#  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'122':[0x00,0x00,0x00,0x00,0x00,0x7E,0x06,0x0C,0x18,0x30,0x60,0x7E,0x00,0x00,0x00,0x00],
#/*--  文字:  {  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'123':[0x00,0x00,0x00,0x0C,0x18,0x18,0x18,0x30,0x60,0x30,0x18,0x18,0x18,0x0C,0x00,0x00],

#/*--  文字:  |  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'124':[0x00,0x00,0x00,0x18,0x18,0x18,0x18,0x18,0x18,0x18,0x18,0x18,0x18,0x18,0x18,0x00],

#/*--  文字:  }  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'125':[0x00,0x00,0x00,0x30,0x18,0x18,0x18,0x0C,0x06,0x0C,0x18,0x18,0x18,0x30,0x00,0x00],

#/*--  文字:  ~  --*/
#/*--  Fixedsys12;  此字体下对应的点阵为：宽x高=8x16   --*/
'126':[0x00,0x00,0x00,0x71,0xDB,0x8E,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
}