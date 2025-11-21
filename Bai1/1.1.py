BEGIN
    DECLARE a, h, S AS REAL

    OUTPUT "Nhap canh day a: "
    INPUT a

    OUTPUT "Nhap chieu cao h: "
    INPUT h

    SET S = 0.5 * a * h

    OUTPUT "Dien tich tam giac la: ", S
END
