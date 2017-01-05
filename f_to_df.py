##Produced by Yunjae Lee
##2016.08.12.
##Version 1.0.0
##E-mail : yunjaelee@yonsei.ac.kr

##Loading file part
xaxis = open("x_axis","r").readline().split()
yaxis = open("y_axis","r").readline().split()

xa = [float(line) for line in xaxis] ##Array of x axis
ya = [float(line) for line in yaxis] ##Array of y axis

nxa = len(xa) ##Number of x axis array
nya = len(ya) ##Number of y axis array


##Decision part for validity of input file
if nxa != nya :
        print "***********************************************"
	print "*Please input the same number of x and y array*"
	print "***********************************************"
	exit()

else :
	##Definition of valuable
	dxa = list()
	dya = list()
	dfa = list()
	xsa = list()
	xpa = list()
	dfas = ""
	xpas = ""
	
	##Calculation part for derivative
	for n in range(0,nxa-1):
       		dxa.append(xa[n+1] - xa[n])
       		dya.append(ya[n+1] - ya[n])
       		dfa.append(dya[n] / dxa[n])
       		xsa.append(xa[n+1] + xa[n])
       		xpa.append(xsa[n] / 2)
		dfas += str(dfa[n])
		dfas += " "
		xpas += str(xpa[n])
		xpas += " "
		
dfas += "\n"
xpas += "\n"

print "****************************"
print "*Calculating successfully!!*"
print "****************************"

##Saving file part
Filex = open("df_y_axis","w")
Filey = open("xp_x_axis","w")

Filex.write(dfas)
Filey.write(xpas)
