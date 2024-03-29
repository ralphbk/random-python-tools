#!/usr/bin/python

# Copyright (C) 2011 by Ralph Bearpark.
# Contact: <http://www.bearpark.ch/who/ralph/>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
                      'billion',          'trillion',      'quadrillion',
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

    def checkandtranslate( self, num ):
        if num == None:
            return "Please enter a number that you want to be displayed in words."
        if not str(num).isdigit():
            return "Sorry, you should give me digits only." 
        if len(str(num)) > 63:
            return "Sorry, that's too big for me."
        return self.numnames(int(num))

def main(argv):
    n=numnames()
    print "%s == %s" % (argv[0], n.checkandtranslate(argv[0]))

if __name__ == "__main__":
    main(sys.argv[1:])
