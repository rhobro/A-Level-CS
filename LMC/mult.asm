        INP
        STA N
        INP
        BRP ASC
        BRA DESC


ASC     LDA I
        SUB ITERS
        BRZ FIN

        LDA CURRENT
        ADD N
        STA CURRENT
        OUT

        LDA I
        ADD INCR
        STA I
        BRA ASC


DESC    LDA I
        SUB ITERS
        SUB INCR
        BRZ DOWNPREP

        LDA CURRENT
        ADD N
        STA CURRENT

        LDA I
        ADD INCR
        STA I
        BRA DESC

DOWNPREP LDA INCR
        STA I
DOWN    LDA I
        SUB ITERS
        BRZ FIN

        LDA CURRENT
        SUB N
        STA CURRENT
        OUT

        LDA I
        ADD INCR
        STA I
        BRA DOWN


FIN     HLT


N       DAT
CURRENT DAT
I       DAT 1
ITERS   DAT 11
PROD    DAT 0
Z       DAT 0
INCR    DAT 1
