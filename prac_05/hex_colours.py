"""
CP1404 Practical
Colour codes in a dictionary
"""

COLOUR_TO_CODE = {"Absolute Zero": "#0048ba",
                  "Acid Green": "#b0bf1a",
                  "Alice Blue": "#f0f8ff",
                  "Baby Blue": 	"#89cff0",
                  "Baby Pink": "#f4c2c2",
                  "Banana Mania": "#fae7b5",
                  "Cadet Grey": "#91a3b0",
                  "CadetBlue": "#5f9ea0",
                  "Cadmium Green": "#006b3c",
                  "Camel": "#c19a6b"}

colour_name = input("Enter colour name: ").title()

while colour_name != "":
    try:
        print(f"{colour_name}'s code is {COLOUR_TO_CODE[colour_name]}")
    except KeyError:
        print("Invalid input")
    colour_name = input("Enter colour name: ").title()


