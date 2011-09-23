#!/usr/bin/python

import math
import sys

class numnames:

    def unitnames( self, num ):
        unitname = [ 'zero',    'one',    'two',        'three',    'four',
                     'five',    'six',    'seven',      'eight',    'nine',
                     'ten',     'eleven', 'twelve',     'thirteen', 'forteen',
                     'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' ]

        if num < 0 or num >= len(unitname):
            print "num param out-of-range 0-%s" % len(unitname)-1
            return ''
        else:
            return unitname[num]

    def tynames( self, ty ):
        tyname = [ 'zero',   'ten',   'twenty',  'thirty', 'forty', 
                    'fifty', 'sixty', 'seventy', 'eighty', 'ninety' ]

        if ty < 0 or ty >= len(tyname):
            print 'ty param out-of-range 0-%s' % len(ty)-1
            return ''
        else:
            return tyname[ty]

    def thounames( self, thounum ):
        thouname  = [ '',                 'thousand',      'million',
                      'billion',          'trilion',       'quadrillion',
                      'quintillion',      'sextillion',    'septillion',
                      'octillion',        'nonillion',     'decillion',
                      'undecillion',      'duodecillion',  'tredecillion',
                      'quattordecillion', 'quindecillion', 'sexdecillion',
                      'septendecillion',  'octodecillion', 'novemdecillion',
                      'vigintillion' ]

        if thounum < 0 or thounum >= len(thouname):
            print 'thounum param out-of-range 0-%s' % len(thouname)-1
            return ''
        else:
            return thouname[thounum]

    def groupnames( self, grpnum ):
        retstr=''
        if grpnum < 0 and num > 999:
            print 'grpnum param out-of range 0-999'
            return ''
        else:
            hundreds  = int(grpnum/100)
            tensunits = grpnum%100 
            tens      = int(tensunits/10)
            units     = grpnum%10
            if hundreds > 0:
                retstr = self.unitnames(hundreds) + ' hundred'
            if tensunits > 0:
                if len(retstr) > 0:
                    retstr = retstr + ' and '
                if tensunits < 20:
                    retstr = retstr + self.unitnames(tensunits)
                else:
                    retstr = retstr + self.tynames(tens) 
                    if units > 0:
                        retstr = retstr + '-' + self.unitnames(units)
        return retstr

    def numnames( self, num ):
        retstr=''
        if num==0:
            return self.unitnames(num)
        digits = int(math.log10(num))
        thousand_groups = int(digits/3)
        for i in range( thousand_groups, -1, -1 ):
            groupnum = (num/(1000**i))%1000
            newstr = self.groupnames(groupnum) 
            if len(newstr) > 0:
                if i > 0:
                    if len(retstr) > 0:
                        retstr = retstr + ', '
                    retstr = retstr + newstr + ' ' + self.thounames(i)
                else:
                    if len(retstr) > 0:
                        if groupnum < 100:
                            retstr = retstr + ' and '
                        else:
                            retstr = retstr + ', '
                    retstr = retstr + newstr
        return retstr

def main(argv):
    if (len(argv) == 1):
        num = int(argv[0])
        n=numnames()
        print "%s == %s" % (num, n.numnames(num))
    else:
        print "expects a single num param that is to be displayed in words."

if __name__ == "__main__":
    main(sys.argv[1:])
