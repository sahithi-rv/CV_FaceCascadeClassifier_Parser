import xml.etree.ElementTree as ET
import sys
import myconstants as cnst

if __name__ == "__main__":
	filename = sys.argv[1];
	tree = ET.parse(filename)
	root = tree.getroot()

	
	stages = root[0][7];
	features = root[0][8]

	# get stage sizes and thresholds
	ss = open(cnst.StageSize, 'w');
	for dum in stages:

		 ss.write( dum[0].text.strip());
		 ss.write(" ");
		 ss.write(dum[1].text.strip());
		 ss.write('\n');
	ss.close();


	# parsing for thresholds, left and right values
	st = open(cnst.StageThres, 'w')
	for dum in stages:
		st.write(dum[0].text)
		st.write('\n')
		for weakclassifiers in dum.iter('weakClassifiers'):
			for dum2 in weakclassifiers:
				s0 = dum2[0].text.strip()
				s00 = s0.split()[2] + " " + s0.split()[3]
				st.write(s00)
				st.write(" ")
				s1 = dum2[1].text.strip()
				st.write(s1)
				st.write('\n')
		st.write('\n')

	#parsing rects
	sr = open(cnst.StageRects, 'w');
	for dum in features:
		for rects in dum:
			numrects = 0
			for dum2 in rects:
				numrects+=1
			sr.write(str(numrects))
			sr.write(" ")
			for dum2 in rects:
				sr.write(dum2.text.strip())
				sr.write(" ")
			sr.write('\n')
