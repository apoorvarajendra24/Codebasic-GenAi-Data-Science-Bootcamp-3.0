def calculate_triangle_area(base, height):

    print("Value of __name__ :", __name__)

    return (base * height) / 2


if __name__ == "__main__":

    print("Area :", calculate_triangle_area(10, 5))


"""
__main__ is not actually a function.

It is a special value Python gives to a file when that file is the starting point of execution.

Simple understanding:

If a Python file is run directly → Python says:
"You are the main file."

and sets:

__name__ = "__main__"
If the file is imported into another file → Python gives it its filename/module name instead.

Why this exists:

Sometimes a file contains:

reusable functions/classes
plus some testing/demo code

When imported elsewhere, we usually want:

only functions/classes
not the testing code to run automatically

So __main__ helps Python identify:

"Is this file being run directly,
or just being imported?"

That is the whole purpose of __main__.

"""




