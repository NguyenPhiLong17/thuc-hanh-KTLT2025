BEGIN
    DECLARE n, i AS INTEGER

    OUTPUT "Nhap so nguyen duong n:"
    INPUT n

    IF n = 1 THEN
        OUTPUT n, " khong la so nguyen to"
        END
    END IF

    IF n < 4 THEN
        OUTPUT n, " la so nguyen to"
        END
    END IF

    SET i = 2

    WHILE (i < n) AND (n % i <> 0)
        SET i = i + 1
    END WHILE

    IF i = n THEN
        OUTPUT n, " la so nguyen to"
    ELSE
        OUTPUT n, " khong la so nguyen to"
    END IF
END
