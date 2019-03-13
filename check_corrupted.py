import ROOT
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import numpy as np

inF = [x for x in sys.argv if '.root' in x]

badFiles = []

for f in inF:
	TF = ROOT.TFile(f,'READ')
	TT = TF.Get("livetime")

	try:
		nevt = TT.GetEntries()
	except AttributeError:
		print (f)
		badFiles.append(f)
		TF.Close()
		continue


	# for n in range( nevt ):
	#
	# 	pev = TT.GetEntry(n)
	#
	# 	try:
	# 		argla = float(TT.MLscore_ntSelec_noFirstLay_full)
	# 	except AttributeError:
	# 		print "Error in file: ", f
	# 		badFiles.append(f)
	#
	# 	break

	TF.Close()

with open( 'badFiles.bad','w') as f:
	for item in badFiles:
		f.write( item+'\n')
