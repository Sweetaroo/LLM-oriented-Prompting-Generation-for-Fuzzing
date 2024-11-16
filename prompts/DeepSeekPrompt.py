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
### MACROS
Example of a macro:
```c
#define TO_STR(x) #x
#define PRIMITIVE_CAT(x, y) x ## y
#define LOG(fmt, ...) printf("[FILE: %s] [FUNCTION: %s] [LINE: %d] " fmt "\n", __FILE__, __FUNCTION__, __LINE__, ##__VA_ARGS__)
#define CAT(x, y) PRIMITIVE_CAT(x, y)
```
Example of conditional compilation:
```c
#ifdef CONDITION
    /* Code to execute if CONDITION is defined */
#else
    /* Code to execute if CONDITION is not defined */
#endif
```

### Your task: Write a C program that:
- Uses features from the C Standard Library headers (`<stdio.h>`, `<stdlib.h>`, `<string.h>`, `<math.h>`, `<time.h>`, `<ctype.h>`, `<limits.h>`, `<stdbool.h>`) in a complex way.
- Uses advanced macros and conditional compilation in C. The program should demonstrate the correct use of `TO_STR()`, `PRIMITIVE_CAT()`, `LOG()`, and `CAT()` macros, as well as `#ifdef`, `#else` and `#endif` directives.
- Uses features from newer versions of the C standard.

"""

MACRO_PROMPT2 = """
### Advanced C Programming Concepts with Rare Features

C programming language has a rich set of features that can help in writing diverse and complex code.
Among these, the C Standard Library is a collection of headers that provide various functionalities. 
Some key headers include:

- <stdio.h>: Handles input/output operations
- <stdlib.h>: Provides general utilities like memory management, random numbers, and string conversions
- <string.h>: Offers functions for string handling
- <math.h>: Contains common mathematical functions
- <time.h>: Supports time and date utilities

Additionally, C provides advanced preprocessor directives like macros, which can be used to define 
abbreviations for chunks of code, and conditional compilation, which can control which portions of your 
program are compiled under different circumstances.

C also has some rare features such as bit fields, volatile keyword, and pointer arithmetic. Bit fields 
are used in a structure declaration to specify that a variable should use only a specific number of bits,
thereby saving memory. The volatile keyword tells the compiler that a variable's value may change in ways
not explicitly specified by the program. Pointer arithmetic allows you to add or subtract integer values 
to or from pointers.

### Instruction:
Your task is to write a short C program that utilizes the features of the C Standard Library, macros, conditional compilation, along with incorporating bit fields, volatile keyword, and pointer arithmetic. Try to create a complex program that showcases the diversity and power of C programming.
"""


TYPEDEF_PROMPT = """
### Background
C programming language offers powerful features like the C Standard Library, the 'typedef' keyword, 
and more. In addition to these, C also allows for low-level programming using bit manipulation and 
inline assembly code. Bit manipulation can lead to more efficient code and inline assembly allows 
direct use of CPU instructions within your C code.

### Your task
Write a complex C program that demonstrates the usage of the C Standard Library, 'typedef', bit manipulation, and inline assembly. Use headers like `<stdio.h>`, `<stdlib.h>` and create aliases for basic types, pointers, function types, arrays, and structures using 'typedef'. Try to include bit manipulation in your program and a section of inline assembly code. Remember to include comments that explain your code and the purpose of each section.
"""

INASM_PROMPT = """
### C Standard Library, Pointers, Inline Assembly, and Unions
C programming offers a diverse range of features. The C Standard Library, headers like `<stdio.h>`, `<stdlib.h>`, `<string.h>`, `<math.h>`, `<time.h>`, `<ctype.h>`, `<limits.h>`, and `<stdbool.h>` provide a multitude of functionalities.

Pointers in C are variables storing addresses of other variables:
```c
int x = 10;
int* p = &x;
```
   
Inline assembly allows the embedding of assembly code in C:
```c
__asm__ volatile ("movl %0, %%eax" : : "r"(x));
```
   
Unions, a less common feature, allow you to store different data types in the same memory space:
```c
union Data {
    int i;
    float f;
    char str[20];
};
```
   
### Your Task
Write a comprehensive C program that utilizes the C Standard Library, pointers, inline assembly, and unions in a complex way. Show how pointers can be manipulated using inline assembly, demonstrate how new C features can be employed, and illustrate the use of unions.
"""

COMMA_PROMPT = """
The C programming language offers a rich set of features, including the C Standard Library 
which provides headers for functionalities such as input/output operations, string manipulation, 
math operations, memory management, etc. Some of these headers include stdio, stdlib, string, math, 
time, ctype, limits, and stdbool. Other features include the comma operator and the for loop. 
The comma operator (,) allows multiple expressions to be evaluated in a single compound expression, 
while the for loop allows code to be repeatedly executed. Here's an example of a code snippet that 
uses both the comma operator and the for loop:

```c
#include <stdio.h>

int main() {
    int a = 1, b = 2, c = 3;
    for(int i = 0; i<3; i++, a++, b++){
        c = a + b;
    }
    printf("Result is: %d\n", c); // Outputs: Result is: 7
    printf("a is: %d\n",a); //Outputs: a is: 4
    printf("b is: %d\n",b); //Outputs: b is: 5
    return 0;
}
```
"""
INIT_PROMPT = """
The C Standard Library provides a wide range of functions, macros, and types used in C programming. These functionalities are defined in various headers and include operations for input/output, string manipulation, math, memory management, boolean types, and complex numbers, among others.

Introduced in C99, initializer designators enable selective initialization of structures and arrays, while Variable Length Arrays (VLAs) permit array length to be determined at runtime. Here are examples of these features:

Initializer designators:
```c
#include <stdio.h>

struct point {
    int x, y, z;
};
int main() {
    struct point p = { .y = 10, .z = 20, .x = 5 };
    printf("p.x = %d, p.y = %d, p.z = %d\n", p.x, p.y, p.z); // Outputs: p.x = 5, p.y = 10, p.z = 20
    return 0;
}
```
Variable Length Arrays:
```c
#include <stdio.h>

int main() {
    int n = 5;
    int arr[n]; // Variable Length Array 
    for(int i=0; i<n; i++) {
        arr[i] = i;
        printf("%d ", arr[i]); // Outputs: 0 1 2 3 4
    }
    return 0;
}
```
Your mission is to write a short C program that not only employs the features of the C Standard Library and C99, but also incorporates inline functions and the _Generic keyword in a complex way.
"""


LABEL_PROMPT = """
### Background
Advanced C features such as inline functions, named initializers, compound literals, and designated initializers are equally important and offer a more sophisticated level of programming.

### Example
Named initializers simplify the initialization of structures:
```c
struct point {
  int x, y;
};

struct point p = {
  .y = 5,
  .x = 3
};
```
### Instruction
Please create a short, complex C program that uses new and rare C features, including but not limited to the C Standard Library, label variables as "goto" targets, conditional statements, inline functions, named initializers, compound literals, and designated initializers.
"""

NEST_FN_PROMPT = """
### Background
The C language offers a vast range of features that enable it to be versatile and powerful. These include the C Standard Library with headers such as `<stdio.h>`, `<stdlib.h>`, `<string.h>`, `<math.h>`, `<time.h>`, `<ctype.h>`, `<limits.h>`, and `<stdbool.h>`. The library also includes support for complex numbers, error reporting, localization, variable arguments, signal handling, multithreading, fixed-width integer types, and wide character utilities.

C also supports features like nested functions, made possible through certain compiler extensions, and recursion where a function calls itself. Another interesting feature of C is pointer arithmetic which allows operations on pointer variables. Variadic functions are another unique feature, allowing a function to accept an indefinite number of arguments. The use of the volatile keyword is another less commonly used feature, instructing the compiler that a variable may be changed in ways not explicitly specified by the program.

### Instruction
Your task is to create a short C program that combines these diverse features in a complex manner. Your program should make use of the C Standard Library, nested functions, recursion, pointer arithmetic, variadic functions, and the volatile keyword. Try to showcase the unique capabilities of these features and how they can interact with each other.
"""


STAT_EXPR_PROMPT = """
### Background
C programming is rich with features that span from its Standard Library to rare and new attributes like designated initializers and compound literals. Designated initializers, introduced in C99, allow initializing elements of arrays or structures in any order. Compound literals, also introduced in C99, let you define and initialize a compound object in a single expression.

The Standard Library is a collection of headers providing a broad spectrum of functionalities, including input/output operations (`<stdio.h>`), utilities such as memory management, random numbers, string conversions (`<stdlib.h>`), and more. Features like statement expressions and function pointers add complexity and flexibility to the language, allowing for the execution of multiple statements within a block and the passing of functions as parameters or the storing of them in data structures.
### Instruction
Your task is to write a program that effectively uses these aspects of C—particularly the Standard Library, statement expressions, function pointers, designated initializers, and compound literals—and incorporates some of the new features introduced in recent C standards. The objective is to generate code snippets with high diversity, showcasing the expansive capabilities of the C language.
"""

ZERO_ARR_PROMPT = """
C is a high-level programming language that supports a wide array of features. The C Standard Library offers various functions, macros, and types that are essential in C programming. These include input/output operations, string manipulation, math operations, memory management, and more. For instance, the header <stdio.h> is used for input/output operations, <stdlib.h> provides general utilities, <string.h> offers string handling functions, and <math.h> contains common mathematical functions. 

One of the features introduced in C99 is the zero-length array, which provides a way to dynamically allocate array sizes within structures. This feature facilitates the creation of flexible data structures. For instance, you can define a structure with an integer count and a zero-length array of type double, and then allocate the structure using malloc.

```c
struct flex_array {
    int count;
    double data[0]; // Zero-length array
};

int n = 5;
struct flex_array *arr = malloc(sizeof(struct flex_array) + n * sizeof(double));
arr->count = n;
for (int i = 0; i < n; ++i) {
    arr->data[i] = i * 1.5;
}
```

Another feature in C is the use of pointers to structures. Pointers are used to store memory addresses, but they can also point to structures. Try to use these features in a complex and creative manner to demonstrate your understanding of C programming.
"""

INITIAL_PROMPTS = [
    BEST_PROMPT_STARCODER,
    BEST_PROMPT_DEEPSEEK,
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
]
