LOOP    LDA CURRENT
        OUT
        ADD ONE
        STA CURRENT
        SUB TOTAL
        BRZ DONE
        BRA LOOP

DONE    HLT


CURRENT DAT 1
ONE     DAT 1
TOTAL   DAT 11
