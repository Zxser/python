import optparse
parser=optparse.OptionParser('usage%prog'+'-H -p')
parser.add_option('-H',dest='tgthost',type='string',help='specify target host ')
parser.add_option('-p ,dest=tgthost',type='string',help='specify target port[s] by comma')
(options,args)=parser.parse_args()
