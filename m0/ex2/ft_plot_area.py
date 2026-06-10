# plot area

"""
defines function that calcutes plot area
"""


def ft_plot_area():
    """
    function calculates plot area with lenght and width from stdin 
    """
    len = int(input("Enter length: "))
    wid = int(input("Enter width: "))
    area = len * wid
    print(f"Plot area: {area}")
