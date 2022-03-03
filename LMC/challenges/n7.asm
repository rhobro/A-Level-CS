        INP
        STA N
        INP
        ADD ONE
        STA ITERS

TOOSMALL LDA N
        SUB LB
        BRP TOOBIG
        BRA END
TOOBIG  LDA N
        SUB UB
        BRP END
        LDA N
        OUT

LOOP    LDA I
        ADD ONE
        STA I
        SUB ITERS
        BRZ END

        LDA N
        ADD ONE
        STA N
        OUT
        BRA LOOP


END     HLT
N       DAT
LB      DAT 1
UB      DAT 51
I       DAT
ITERS   DAT
ONE     DAT 1