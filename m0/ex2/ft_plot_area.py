# plot area

"""
defines function that calcutes plot area
"""


def ft_plot_area() -> None:
    """
    function calculates plot area with lenght and width from stdin
    """
    length = int(input("Enter length: "))
    wid = int(input("Enter width: "))
    area = length * wid
    print(f"Plot area: {area}")
