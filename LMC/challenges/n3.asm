        INP
        STA SUM
        INP
        ADD SUM
        STA SUM

        INP
        STA THIRD
        LDA SUM
        SUB THIRD
        OUT

SUM     DAT
THIRD DAT