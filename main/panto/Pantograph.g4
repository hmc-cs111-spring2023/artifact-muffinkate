/* grammar */
grammar Pantograph;

/* parser */
panto               : PROPAGATE NEWLINE (propagation)* DESIGN NEWLINE (line)+ EOF ;
line                : command NEWLINE ;
propagation         : option NEWLINE ;
option              : (offset | curve | rotate | scale | spacing) ;
offset              : OFFSET argument ;
curve               : CURVE (LOW | HIGH) ;
rotate              : ROTATE argument ;
scale               : SCALE argument ;
spacing             : SPACING argument ;
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

PROPAGATE           : P R O P A G A T E ':';
DRAW                : D R A W ;
TURN                : T U R N ;
LEFT                : L E F T ;
RIGHT               : R I G H T ;
LOW                 : L O W ;
HIGH                : H I G H ;
DESIGN              : D E S I G N ':';
SPACING             : S P A C I N G ;
OFFSET              : O F F S E T ;
CURVE               : C U R V E ;
ROTATE              : R O T A T E ;
SCALE               : S C A L E ;

NUMBER              : [0-9]+ ;

WHITESPACE          : (' ' | '\t')+ -> skip;
NEWLINE             : ('\r'? '\n' | '\r')+ ;
