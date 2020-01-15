
import sys

ctags=['LOC', 'PER', 'ORG']
stags=['Process', 'Material', 'Task']
newtags=zip(stags, ctags)

#outfile = open("first.txt", "w")

annfile = sys.argv[1]
txtfile = annfile.replace(".ann", ".txt")
paragraph_ = open(txtfile, "r")
paragraph = paragraph_.read()
#print (paragraph)
#print (paragraph[24:28])
#print (paragraph[38:43])

#print (annfile, txtfile)

tag_out = []
lastind = 0

with open(annfile) as f:
    for line in f:
        if line.startswith('T'):
            tid, t_cinds, _ = line.split('\t')
            tag, start, end = t_cinds.split(' ')
            start=int(start)
            end=int(end)
            if start!=lastind:
                owords=paragraph[lastind:start].split(' ')
                for oword in owords:
                    if oword.strip()!='':
                        #tag_out+=[oword +' O']
                        print (oword + ' O')
            lastind=end
            words=paragraph[start:end].split(' ')
	    #print ("BARK", paragraph[start:end])
            #tag=[j for i,j in newtags if i==tag][0]
            for wind in range(len(words)):
                if wind==0:
                    print (words[wind] + ' B-'+tag)
                    #tag_out+=[words[wind] +' B-'+tag]
                else:
                    print (words[wind] + ' I-'+tag)
                    #tag_out+=[words[wind] +' I-'+tag]
                    
#print (lastind)
#print (len(paragraph))
#print (paragraph[lastind+1:len(paragraph)])
owords=paragraph[lastind+1:len(paragraph)].split(' ')
for oword in owords:
        if oword.strip()!='':
            tag_out+=[oword +' O']
            print (oword + ' O')
