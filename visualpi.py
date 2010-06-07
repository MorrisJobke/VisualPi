#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) Morris Jobke 2010 <morris.jobke@googlemail.com>
# 
# VisualPi is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# VisualPi is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess

f = open('pi.txt', 'r')
c = f.read(1)
tmp =  range(10)

upperLim = [20,50,100,200,1000];
lowerLim = [0,20,50,100,200];

numbers = {}
for i in range(10):
	numbers[i] = 0
count = 0
maximum = 0
minimum = 100
while c:
	try:
		c = int(c)
	except:
		c = f.read(1)
		continue
	count += 1
	if c in tmp:
		numbers[c] += 1
		#print c
	t = ''
	minimum = 999999999999999999999999999
	for i in numbers:
		t += str(i) + '\t' + str(numbers[i]) + '\n'
		if numbers[i] > maximum:
			maximum = numbers[i]
		if numbers[i] < minimum:
			minimum = numbers[i]
			

	d = open('tmp.dat', 'w')	
	d.write(t)
	d.close()
		
	if not True:
		mi = minimum - minimum%10
		ma = maximum + 10 - maximum%10
	else:
		for i in upperLim:
			if maximum < i:
				ma = i
				break
			else:
				ma = maximum
		for i in upperLim:
			if minimum > i:
				mi = i
				break
			else:
				mi = minimum
	
	
	d = open('plot.plt', 'w')	
	t = '''set grid\n
		set nokey\n
		unset key\n
		set yrange [%i:%i]
		unset logscale x\n
		unset logscale y\n
		set title 'Pi %i. Nachkommastelle'\n
		set output '%.10i.png'\n
		set terminal png xffffff\n
		plot 'tmp.dat' using 1:2 with lines smooth sbezier'''%(mi,ma,count,count)	
	d.write(t)
	d.close()
	subprocess.Popen(
		[	'gnuplot',
			'plot.plt'
		]
	).communicate()
	
	c = f.read(1)
	if not count%10:
		print count
	if count == 1800:
		break
	


