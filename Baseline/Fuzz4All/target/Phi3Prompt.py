BEST_PROMPT_STARCODER = """
### Background
 The C Standard Library is a collection of headers that define various functions, macros, and types used in C programming. These headers provide 
functionalities such as input/output operations, string manipulation, math operations, memory management, and more. Some key headers include:

- <stdio.h>: Handles input/output operations
- <stdlib.h>: Provides general utilities like memory management, random numbers, and string conversions
- <string.h>: Offers functions for string handling
- <math.h>: Contains common mathematical functions
- <time.h>: Supports time and date utilities
- <ctype.h>: Determines character data types
- <limits.h>: Defines range of integer types
- <stdbool.h>: Introduces boolean types and macros (since C99)

Additional headers in the library offer support for complex numbers, error reporting, localization, variable arguments, signal handling, multithreading, fixed-width 
integer types, and wide character utilities, among others. The library has evolved over time, with newer versions of the C standard introducing new headers and 
functionalities. 
### Your task: 
Please create a short program which uses new C features in a complex way. 
"""

BEST_PROMPT_DEEPSEEK = """
### Specification: 
The C Standard Library headers provide predefined functions, macros, and types that can be used for various common tasks. These headers include `<assert.h>` for macro comparisons to zero, `<complex.h>` for complex number arithmetic, and `<ctype.h>` for determining the type of character data. Headers `<errno.h>`, `<fenv.h>`, and `<float.h>` cater to error reporting, floating-point environment, and limits of floating-point types, respectively. Integer types, alternative operator spellings, and ranges of integer types come under `<inttypes.h>`, `<iso646.h>`, and `<limits.h>`. Localization utilities, common math functions, and nonlocal jumps are covered by `<locale.h>`, `<math.h>`, and `<setjmp.h>`. Headers `<signal.h>` to `<time.h>` provide signal handling, convenience macros, variable arguments, atomic operations, and time/date utilities. The headers from `<uchar.h>` to `<wctype.h>` help in dealing with UTF-16 and UTF-32 characters, multibyte and wide characters, and determining the type contained in wide character data. Other utilities include input/output, memory management, program utilities, string conversions, random numbers, and algorithms provided by headers like `<stdio.h>`, `<stdlib.h>`, and `<string.h>`. 
### Your task: 
Please create a short program which uses new C features in a complex way. 
"""

EVO_PROMPT = """
Design a brief, innovative and educational C program that intricately interacts with system level operations 
such as file operations, memory management, and process control while implementing complex algorithms and 
hierarchical data structures. The program should demonstrate a complex utilization of the language's capabilities, 
including advanced data structures and algorithms for optimal efficiency. This program should effectively use the 
language's features to illustrate advanced programming techniques, including inter-process communication protocols, 
and extend the boundaries of optimization, emphasizing speed and effectiveness in handling intricate tasks. 
"""

MACRO_PROMPT = """
In C programming language, standard predefined macros are identifiers that represent common expressions or values. They are usually defined by the compiler. They can be used to get useful information about the code, like file name, line numbers, function names etc. Here's a brief explanation of some common predefined macros.

1. `__LINE__`: This macro holds the line number in the source code file where this macro is being used.

2. `__FILE__`: This macro holds the name of the source file where this macro is being used.

3. `__DATE__`: This macro holds the date when the program was compiled.

4. `__TIME__`: This macro holds the time when the program was compiled.

5. `__func__`: This macro holds the name of the function where this macro is being used.

Here's a usage example of these macros:

```C
#include<stdio.h>

void testFunction() {
   printf("Current function: %s\\n",__func__);
   printf("Current line: %d\\n",__LINE__);
   printf("Current file: %s\\n",__FILE__);
}

int main() {
   printf("Compilation date: %s\\n",__DATE__);
   printf("Compilation time: %s\\n",__TIME__);
   testFunction();
   return 0;
}
```

In this program `__DATE__` and `__TIME__` macros print the date and time when the program was compiled. `__func__`, `__LINE__` and `__FILE__` macros are used inside `testFunction` to print the current function name, line number and file name.

### Your Task
Please create a short program that uses standard predefined macros in a complex way.

"""

MACRO_PROMPT2 = """

Dive into the world of X macros, an effective C programming strategy famed for its flexibility and utility in managing lists and data items. The notable DRY (Don't Repeat Yourself) principle is upheld as these macros minimize the need for repetitive code such as enum definitions and string arrays. Ensure consistency while programming with X macros as demonstrated in the following code:

```c
#include <stdio.h>

#define COLOR_LIST     \\
    X(RED,     255, 0,   0)      \\
    X(GREEN,   0,   255, 0)      \\
    X(BLUE,    0,   0,   255)    \\
    X(YELLOW,  255, 255, 0)      \\
    X(WHITE,   255, 255, 255)    \\
    X(BLACK,   0,   0,   0)

#define X(name, r, g, b) name,
typedef enum {
    COLOR_LIST
} Color;
#undef X

#define X(name, r, g, b) #name,
const char* color_names[] = {
    COLOR_LIST
};
#undef X

void print_color_info(Color color) {
    printf("Color: %s", color_names[color]);
}

int main() {
    Color color = RED;
    print_color_info(color);

    color = BLUE;
    print_color_info(color);

    return 0;
}
```
Your task: Create a concise program that showcases intricate uses of X macros. Are you prepared for the challenge? 
"""

TYPEDEF_PROMPT = """
### Usage of `typedef` in C Programming

`typedef` in C is a keyword that allows you to create an alias for an existing data type. This can make complex type declarations more readable and can help in code maintenance by allowing easy modification of type definitions in a single place.

#### Common Uses of `typedef`

1. **Simplifying Complex Type Declarations**: It's often used to create shorter, more intuitive names for complex types, such as pointers or structures.
2. **Portability**: It helps in making code more portable by abstracting away machine-specific details.

#### Example of `typedef`

Here's a simple example that demonstrates the use of `typedef` with structures:

```c
#include <stdio.h>

// Define a structure to represent a point in 2D space
typedef struct {
    int x;
    int y;
} Point;

// Define a typedef for an existing type
typedef unsigned long ulong;

int main() {
    // Create a Point instance
    Point p1;
    p1.x = 10;
    p1.y = 20;

    // Use the ulong typedef
    ulong distance = 100;

    printf("Point p1: (%d, %d)\\n", p1.x, p1.y);
    printf("Distance: %lu\\n", distance);

    return 0;
}
```

#### Explanation:

1. **Structure Typedef**: `typedef struct { int x; int y; } Point;` creates a new type `Point` that can be used to declare variables of the structure type without needing to use the keyword `struct` each time.

2. **Simple Typedef**: `typedef unsigned long ulong;` creates an alias `ulong` for the `unsigned long` type, simplifying code and making it more readable.

#### Key Points:

- **Readability**: `typedef` makes your code easier to read and understand, especially when dealing with complex types.
  
- **Code Maintenance**: Changing the underlying type in one place will automatically update all instances where the `typedef` is used, improving maintainability.

This example illustrates how `typedef` can be used to simplify the declaration of complex data types and enhance code readability.

#### Instruction
Please construct a very short program that uses c features in a complex way.

"""

INASM_PROMPT = """
Grab a chance to explore the world of Inline Assembly in C, a power-packed feature allowing direct embedding of assembly instructions. Familiarize yourself with inline assembly, as it provides you with tools for low-level hardware manipulation and code optimization. Consider the XOR Swap Algorithm, a technique that swaps integers by using a bitwise XOR operation, as an illustration of this feature's utility. This in-depth understanding promises greater command over your code, aiding in performance augmentation and portability. Here's a basic syntax for implementing it:

```c
#include <stdio.h>

int main() {
    int a = 10;
    int b = 20;

    __asm__ volatile (
        "xorl %%ebx, %%eax;"
        "xorl %%eax, %%ebx;"
        "xorl %%ebx, %%eax;"
        : "=a" (a), "=b" (b)
        : "a" (a), "b" (b)
    );

    printf("After swap: a = %d, b = %d\\n", a, b);

    return 0;
}
```
"""

COMMA_PROMPT = """
### Usage of the Comma Operator in C Programming

The comma operator in C is a binary operator that evaluates two expressions from left to right and returns the value of the second expression. It's used when you want to perform multiple operations in places where only one expression is expected, such as in a `for` loop or a function argument.

#### Example of Comma Operator

Here's a simple example that demonstrates the usage of the comma operator:

```c
#include <stdio.h>

int main() {
    int a = 10;
    int b = 20;
    int result;

    // Using the comma operator
    result = (a += 5, b += 10);

    printf("Value of a: %d\\n", a);      // a is now 15
    printf("Value of b: %d\\n", b);      // b is now 30
    printf("Result: %d\\n", result);     // result is 30 (the value of b)

    return 0;
}
```

#### Explanation:

1. **Comma Operator Usage**: In the expression `result = (a += 5, b += 10);`, the comma operator first evaluates `a += 5` (which adds 5 to `a`), and then evaluates `b += 10` (which adds 10 to `b`). The entire expression returns the value of `b += 10`, which is 30, and assigns it to `result`.

2. **Multiple Expressions**: The comma operator is often used when you need to execute multiple expressions and only care about the final result.

#### Key Points:

- **Evaluation Order**: The expressions are evaluated from left to right, but only the value of the last expression is returned.
  
- **Use Cases**: The comma operator is particularly useful in situations like initializing multiple variables in a `for` loop or in complex macros where multiple steps are required.

This example illustrates the use of the comma operator to perform and evaluate multiple expressions within a single statement in C.

#### Your Task
Please create a short c program that uses comma operator in a complex way.

"""


LABEL_PROMPT = """
Deep-dive into an advanced feature of GNU C programming: the 'label-as-values' or 'computed gotos'. This capability allows storing the address of a label using the `&&` operator and enables dynamic jumping to these labels using the `goto *` statement. It's a potent tool but needs to be wielded wisely as it can impact code readability and maintainability. Take a look at the following code to illustrate this feature:

```c
#include <stdio.h>

int main() {
    void *label;           // Declare a label variable
    label = &&label1;      // Assign the address of a label to the label variable
    goto *label;           // Use a goto statement with the label variable

label1:
    printf("Jumped to label1");

    label = &&label2;      // Change the label variable to point to another label
    goto *label;

label2:
    printf("Jumped to label2");

    return 0;
}
```
"""

NEST_FN_PROMPT = """
### Nested Functions in C Programming

In the C programming language, nested functions are functions defined inside other functions. However, it's important to note that nested functions are not part of the standard C language and are supported as an extension in some compilers, like GCC.

Nested functions can be useful when you need to encapsulate functionality that is only relevant within the context of the enclosing function. The nested function can access the variables of the enclosing function, providing a way to organize code more locally.

#### Example of Nested Functions

Here's a simple example demonstrating the usage of a nested function in GCC:

```c
#include <stdio.h>

int main() {
    // Outer function variable
    int x = 10;

    // Nested function
    void inner_function() {
        printf("Inner function: x = %d", x);
        // Modify the outer function's variable
        x += 5;
    }

    // Call the nested function
    inner_function();
    
    printf("After inner_function: x = %d", x);

    return 0;
}
```

#### Explanation:

1. **Defining a Nested Function**: Inside the `main` function, a nested function called `inner_function` is defined. This function can access and modify the variables of the `main` function, like `x`.

2. **Calling the Nested Function**: The `inner_function` is called within `main`, and it prints the value of `x` and modifies it.

3. **Variable Scope**: The nested function can access and modify the variables of the enclosing function, which is a key feature of nested functions.

#### Key Points:

- **Use Cases**: Nested functions are useful for organizing code, especially when the function is small and only relevant within the context of the enclosing function.

This example demonstrates how nested functions can be defined and used within another function in C, provided you are using a compiler that supports this feature, like GCC.

#### Instruction
Please create a short c program that uses nested functions in a complex way.

"""

STAT_EXPR_PROMPT = """
### Usage of Statement Expressions in C Programming

Statement expressions are a feature of the GNU C extension that allows you to include a block of code (a sequence of statements) inside an expression. This can be useful for creating complex macros or inline code blocks that return a value.

Statement expressions are enclosed in parentheses, with the statements themselves enclosed in braces. The value of the statement expression is the value of the last statement in the block.

#### Example of Statement Expressions

Here's a simple example demonstrating the usage of statement expressions:

```c
#include <stdio.h>

#define MAX(a, b) ({ \\
    int _a = (a);    \\
    int _b = (b);    \\
    _a > _b ? _a : _b; \\
})

int main() {
    int x = 10;
    int y = 20;

    // Use the statement expression in a macro
    int max_value = MAX(x, y);

    printf("Max of %d and %d is %d", x, y, max_value);

    return 0;
}
```

#### Explanation:

1. **Statement Expression in a Macro**: The `MAX` macro uses a statement expression to compare two values. The statement expression is defined within `({ ... })` and contains multiple statements.
   - First, it assigns the values of `a` and `b` to temporary variables `_a` and `_b`.
   - Then, it uses a conditional operator to return the larger of the two values.
   - The result of the statement expression is the result of the last statement, which is returned by the macro.

2. **Macro Usage**: The `MAX` macro is used in the `main` function to find the maximum of two integers, `x` and `y`.

#### Instruction
Please create a short program that uses statement expressions in a complex way.

"""

ZERO_ARR_PROMPT = """
A zero-length array is a C programming concept that's also frequently referred to as a flexible array member. It is often used in situations where a structure ends with a possibly empty array. It is formally included in the C99 standard. The zero-length array provides an easy and legal way to perform certain operations, which would be difficult with traditional C-style arrays.

Here's an example of how to use a zero length array in C programming:

```c
#include <stdio.h>
#include <stdlib.h>

// A structure which contains an integral member followed by zero-length array
struct array {
    int length;
    int arr[];  // this is a zero-length array

int main() {
    int n = 10;

    // Allocation of memory for structure and array
    struct array *a = malloc(sizeof(struct array) + sizeof(int) * n);
    a->length = n;

    // Accessing array members using pointer
    for (int i = 0; i < a->length; i++) {
        a->arr[i] = i;
    }

    // Printing array values
    for (int i = 0; i < a->length; i++) {
        printf("%d ", a->arr[i]);
    }

    free(a);
    return 0;
}
```

In this code, we define a zero-length array 'arr' inside the 'array' structure. In our main function, we allocate memory for our structure plus some extra memory for our array, and fill and print the array. This is a way to have a variable-length array inside a struct, often used when the length of the data is not known in advance. Note that older compilers may not support this feature (it works on any C99 or C11-compliant compiler).

#### Instruction
Please create a short c program that uses zero-length arrays in a complex way.

"""

ATTR_PROMPT = """
Function and variable attributes are a feature in C programming language that provides additional information about the behavior or contain specific properties of functions and variables, beyond what is conveyed by their type. This information helps the compiler in the optimization and code generation.

These attributes are compiler-specific and vary across compilers. The most common compiler used is GCC, which supports a wide range of function and variable attributes.

Here's an example showing the usage of `__attribute__` in C language for both function and variable:

```c
// 'used' attribute on variable
__attribute__((used)) static int usedVar = 10;

//'deprecated' attribute on function
__attribute__((deprecated)) void oldFunction()
{
    printf("This is a deprecated function.");
}

int main(){
    oldFunction();
    printf("Value of usedVar: %d", usedVar);
}
```

In the above code:

- The `used` attribute on the variable `usedVar` tells the compiler that `usedVar` variable is meant to be used. Even if it is not referenced in the main program, it should not be eliminated as dead code.

- The `deprecated` attribute is used with the function `oldFunction`. This tells the compiler to generate a warning whenever this function is used in the code. This helps programmers to avoid using outdated or potentially harmful functions.

Remember to have the appropriate includes in your code for all the functions you've used; in this case, you should add `#include <stdio.h>` at the top of your script.

#### Instruction
Please write a short c program that uses function and variable attributes in a complex way.

"""

INIT_PROMPT = """
### Usage of Designated Initializers in C Programming

Designated initializers in C allow you to initialize specific members of a structure or specific elements of an array by explicitly naming them. This feature, introduced in C99, improves code readability and reduces errors by making it clear which member or element is being initialized.

#### Example of Designated Initializers

Here’s a simple example demonstrating the use of designated initializers with a structure and an array:

```c
#include <stdio.h>

// Define a structure
typedef struct {
    int x;
    int y;
    int z;
} Point3D;

int main() {
    // Using designated initializers to initialize a structure
    Point3D p1 = {
        .x = 10,
        .z = 30,  // y will be initialized to 0 by default
    };

    // Using designated initializers to initialize an array
    int arr[5] = { [0] = 1, [2] = 3, [4] = 5 };

    printf("Point p1: x = %d, y = %d, z = %d\\n", p1.x, p1.y, p1.z);
    printf("Array: arr[0] = %d, arr[1] = %d, arr[2] = %d, arr[3] = %d, arr[4] = %d\\n",
           arr[0], arr[1], arr[2], arr[3], arr[4]);

    return 0;
}
```

#### Explanation:

1. **Designated Initializers for Structures**:
   - `Point3D p1 = { .x = 10, .z = 30 };` initializes the `x` and `z` members of the structure `p1`.
   - The `y` member is not explicitly initialized, so it defaults to 0.

2. **Designated Initializers for Arrays**:
   - `int arr[5] = { [0] = 1, [2] = 3, [4] = 5 };` initializes specific elements of the array.
   - Elements not explicitly initialized (like `arr[1]` and `arr[3]`) are automatically set to 0.

#### Key Points:

- **Clarity**: Designated initializers make it clear which members or elements are being initialized, reducing the likelihood of errors, especially in large or complex structures.
  
- **Flexibility**: You can initialize only the elements or members you care about, leaving others to their default values.

- **Order Independence**: The order of initialization does not need to follow the order of the members in the structure or elements in the array, providing flexibility.

This example illustrates how designated initializers can be used to clearly and concisely initialize specific members of structures or elements of arrays in C.

#### Your task
Please create a short c program that uses initialize designators in a complex way. 

"""

INITIAL_PROMPTS = [
    #BEST_PROMPT_STARCODER,
    #BEST_PROMPT_DEEPSEEK,
    # corner cases
    MACRO_PROMPT,
    MACRO_PROMPT2,
    TYPEDEF_PROMPT,
    INASM_PROMPT,
    COMMA_PROMPT,
    INIT_PROMPT,
    LABEL_PROMPT,
    NEST_FN_PROMPT,
    STAT_EXPR_PROMPT,
    ZERO_ARR_PROMPT,
    ATTR_PROMPT,
]
