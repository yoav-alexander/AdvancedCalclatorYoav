import pytest
from main import calculate_expression


# 5 syntax error, invalid input, empty input, white space
@pytest.mark.parametrize(
    'expression',
    (
            "1++",
            "3^*2",
            "()^*2",
            "1+.",
            "~~5",
            "4~@3",
            "one plus one"
            "",
            "  \t    \n  ",
    )
)
def test_calculate_expression_fail(expression: str):
    with pytest.raises(SyntaxError):
        calculate_expression(expression)


@pytest.mark.parametrize(
    ('expression', 'expected_result'),
    (
            ("1+2", 3),
            ("-1-2", -3),
            ("5*2.5", 12.5),
            ("7.50/2", 3.75),
            ("9^0.5", 3),
            ("1%-2", -1),
            ("1@2", 1.5),
            ("(-11)$0", 0),
            ("0.5&7.5", 0.5),
            ("~3.15", -3.15),
            ("5!#", 3),
            ("3!!", 720),
            (" 4+2*5 ", 14),
            ("4/6*3", 2),
            ("2---3", -1),
    )
)
def test_calculate_expression(expression: str, expected_result: float):
    assert calculate_expression(expression) == expected_result


@pytest.mark.parametrize(
    ('expression', 'expected_result'),
    (
        ("5!!#*23&3@(-2^2)---3", 3154),
        ("3!--2*0.5^4$(7.52/2)", 6.125),
        ("~(~2*2!^ (2%4-2)+(2))", 0),
        ("--(2 @ 4$23&3^0.15)/2!", 0.5895738228),
        ("(12*1.6^3##+45%-3)^0.2", 2.1792559419),
        ("3!!# +~23^(4-4)^12-0#", 10),
        ("3$3%6^3*3#-3/2$3#*~(-1)#", 80),
        ("1+2-3*4/5^6%7@8$9&~(~10)", 2.999232),
        ("~-2!*~(~5)#!#!-12^3&66/6", -276),
        ("666^0.5 + 12!#---(3+32)/3", 41.1403091345),
        (" -----2--2*3/2+2@3 + 23-3", 23.5),
        (" (1/3)+(1/6)-0.5 + 2 * 24", 48.0),
        ("(--1+(-1^2-4*1*-1)^0.5)/2", 1.6180339887),
        ("4*(1-1/3+1/5-1/7+1/9-1/11)", 2.976046176),
        ("9801/(2206*2^0.5)+126/2-63", 3.14159273),
        ("-3^2+-3^2---36^0.5*6/123#", 12.0),
        ("0.5*2+100-34@55-46^2-1234#", -2069.5),
        ("(12*(11+3^2$9))----(15*4%23)", 236388.0),
        ("4^4/4+2-4@36-1234566#--(3!+2)", 27),
        (" - 12 + 132 / 34 ^ 3 * 34 $ 2", -11.8858131488)
    )
)
def test_calculate_expression_complex(expression: str, expected_result: float):
    assert calculate_expression(expression) == expected_result

