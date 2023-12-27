# Polygon Calculations With Python
This is one of the practices I completed for the "Scientific Computing with Python" certificate from freecodecamp.org. <br>
"test_module" and "main" were already given, "shape_calculator" is the file I developed code in. <br><br>
There are two classes of polygons that this project focuses on: <br>
- **Rectangle** objects initialize with two parameters in case of differing lengths between shape height and width. <br>
- **Square** objects initialize with only one parameter for the length of a side (as squares have the same length on all sides) and inherits the methods from the **Rectangle** class as a subclass. <br><br> "shape_calculator" holds methods that can be called from main to set/mutate or get/return the width/height values of a particular shape. It also contains further methods for: <br>
- measuring diagonal length (even for squares as the width and height are derived from the given side length for calculations)
- seeing how many of X shapes will fit in Y shape (done by diving the areas of the two shapes)
