/* grammar */
grammar Pantograph;

/* parser */
panto               : PROPOGATE NEWLINE (propogation)+ NEWLINE DESIGN NEWLINE (line)+ EOF ;
line                : command NEWLINE;
propogation         : SPACING ;
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

PROPOGATE           : P R O P O G A T E ':';
DRAW                : D R A W ;
TURN                : T U R N ;
LEFT                : L E F T ;
RIGHT               : R I G H T ;
DESIGN              : D E S I G N ':';
SPACING             : S P A C I N G ;

NUMBER              : [0-9]+ ;

WHITESPACE          : (' ' | '\t')+ -> skip;
NEWLINE             : ('\r'? '\n' | '\r')+ ;
