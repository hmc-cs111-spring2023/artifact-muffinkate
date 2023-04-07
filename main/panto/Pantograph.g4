/* grammar */
grammar Pantograph;

/* parser */
panto               : PROPOGATE (propogation)+ DESIGN (line)+ EOF ;
line                : command NEWLINE;
propogation         : VERTICAL ;
command             : (draw | turn) ;
draw                : DRAW argument ;
turn                : TURN (LEFT | RIGHT) argument ;
argument            : NUMBER ;
                                        

/* lexer */

fragment A          : ('A'|'a') ;
fragment B          : ('B'|'b') ;
fragment C          : ('C'|'c') ;
fragment D          : ('D'|'d') ;
fragment E          : ('E'|'e') ;
fragment F          : ('F'|'f') ;
fragment G          : ('G'|'g') ;
fragment I          : ('I'|'i') ;
fragment L          : ('L'|'l') ;
fragment N          : ('N'|'n') ;
fragment P          : ('P'|'p') ;
fragment R          : ('R'|'r') ;
fragment V          : ('V'|'v') ;
fragment W          : ('W'|'w') ;
fragment S          : ('S'|'s') ;
fragment Y          : ('Y'|'y') ;
fragment H          : ('H'|'h') ;
fragment O          : ('O'|'o') ;
fragment U          : ('U'|'u') ;
fragment T          : ('T'|'t') ;

PROPOGATE           : P R O P O G A T E ;
DRAW                : D R A W ;
TURN                : T U R N ;
LEFT                : L E F T ;
RIGHT               : R I G H T ;
DESIGN              : D E S I G N ;
VERTICAL            : V E R T I C A L ;

NUMBER              : [0-9]+ ;

WHITESPACE          : (' ' | '\t') ;
NEWLINE             : ('\r'? '\n' | '\r')+ ;
