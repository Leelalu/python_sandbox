#!/bin/python3
import sys
import random
import linecache

WORDFILE = ""
FILEPATH = ""
WORDRANDOM = ""
INPUTLETTER	=	""
GUESS_STRING = ""

LINECOUNT	=	0
CORRECTINPUTS	=	0
RANDLINENUM	=	0
TRYCOUNT	=	0
MAXTRY	=	0
WORDLEN	=	0
CHARNUM	=	0

DOESINPUTMATCH = False
HASWON = False


#	Attempt	toe	get	&	open	file
try:
    FILEPATH	=	sys.argv[1]
except	(TypeError,	IndexError):
    print("Needs the wordfile as cmd arg to get word")
    sys.exit()

try:
    WORDFILE	=	open(FILEPATH,	"r")
except	FileNotFoundError:
    print("File	not	found")
    sys.exit()

#setup	vars
LINECOUNT = len(WORDFILE.readlines())
RANDLINENUM	=	random.randint(1,	LINECOUNT)
WORDRANDOM = linecache.getline(FILEPATH, RANDLINENUM)
WORDLEN	=	len(WORDRANDOM)-1
MAXTRY = len(WORDRANDOM)*2
for	char	in	range(WORDLEN):
    GUESS_STRING = GUESS_STRING+"-"
WORDFILE.close()

#	game	loop
while	TRYCOUNT	<	MAXTRY	and	CORRECTINPUTS	<	WORDLEN:
#menu	scr
    print("===============Attempts left:	",	MAXTRY-TRYCOUNT)
    print(GUESS_STRING)
    print("===============Correct: ",	CORRECTINPUTS,	"/",	WORDLEN)
    INPUTLETTER	=	str(input("Enter your next guess:	"))

#scan	input
    CHARNUM	=	0
    while	CHARNUM	<	WORDLEN:
        if	INPUTLETTER	==	WORDRANDOM[CHARNUM]:
            GUESS_STRING =	GUESS_STRING[:CHARNUM]	+	INPUTLETTER	+	GUESS_STRING[CHARNUM	+	1:]
            DOESINPUTMATCH =	True
            CORRECTINPUTS	+= 1
        CHARNUM	+= 1

    if	DOESINPUTMATCH:
        print("Closer to sweet Freedom!")
    else:
        print("A step	closer to Death!")


    DOESINPUTMATCH = False
    TRYCOUNT +=	1

# Report on success
if	CORRECTINPUTS	== WORDLEN:
    print("ESCAPED HANGING!!!")
    print("Found Word:	", WORDRANDOM)
else:
    print("DEATH!!!")
    print("Word:", WORDRANDOM)
