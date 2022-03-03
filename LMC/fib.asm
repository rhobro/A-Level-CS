        INP
        STA ITERS

LOOP    LDA Z
        ADD PENULTIMATE
        ADD ULTIMATE
        STA CURRENT
        OUT

        LDA ULTIMATE
        STA PENULTIMATE
        LDA CURRENT
        STA ULTIMATE

        LDA I
        ADD INCR
        STA I
        SUB ITERS
        BRZ END
        BRA LOOP
        
END     HLT


ITERS   DAT
I       DAT 0
PENULTIMATE DAT 0
ULTIMATE DAT 1
CURRENT DAT
INCR    DAT 1
Z       DAT 0
