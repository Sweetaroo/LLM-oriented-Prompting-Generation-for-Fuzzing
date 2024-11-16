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
#### Basic Macros

```c
// Wrap x in quotes, e.g., `printf("%s", TO_STR(Hello!))` will be expanded to
// `printf("%s", "Hello!")`
#define TO_STR(x) #x

// Concatenate x and y, e.g.,
// `int age = 10;`
// `printf("%d", PRIMITIVE_CAT(a, ge));`
// will print the value of "age", i.e., 10.
#define PRIMITIVE_CAT(x, y) x ## y
```

#### Usage Examples

```c
#include <stdio.h>

int main() {
    int age = 10;
    printf("%s\n", TO_STR(Hello World!)); // Outputs: "Hello World!"
    printf("%d\n", PRIMITIVE_CAT(a, ge));    // Outputs: 10
    return 0;
}
```

#### Log Macro

A more complex macro can be used for logging purposes, incorporating file name, function name, line number, and a formatted message.

```c
#include <stdio.h>

#define LOG(fmt, ...) \
    printf("[FILE: %s] [FUNCTION: %s] [LINE: %d] " fmt "\n", \
    __FILE__, __FUNCTION__, __LINE__, ##__VA_ARGS__)

int main() {
    LOG("Got Here!"); // Example log message
    return 0;
}
```

### Pitfalls and Solutions

Macros can be tricky due to their textual substitution nature. Here's a common pitfall and how to address it:

#### Pitfall: Incorrect Macro Expansion

```c
#define X a
int age = 10;
printf("%d", PRIMITIVE_CAT(X, ge)); // Incorrectly expanded to `Xge`, not `age`!
```

#### Solution: Correct Macro Usage

To ensure that `X` is expanded correctly within the macro, you can define a helper macro that correctly uses `PRIMITIVE_CAT`.

```c
#define X a
#define CAT(x, y) PRIMITIVE_CAT(x, y)
int age = 10;
printf("%d", CAT(X, ge)); // Correctly expands to `age`
```
### Instruction: Write a short c program that uses macros in a complex way.
"""

MACRO_PROMPT2 = """
#### Fancier Macros
Consider the following:
```c
#define EXAMPLE(_) _(FOO) _(BAR) _(BAZ)
#define EXAMPLE_FN(eg) void func_##eg(int);
// what's the expansion this?
EXAMPLE(EXAMPLE_FN);
```

The preprocessor will expand "EXAMPLE(EXAMPLE_FN)" in this way:
```c
EXAMPLE(EXAMPLE_FN);
```
will be expanded to
```c
EXAMPLE_FN(FOO); EXAMPLE_FN(BAR); EXAMPLE_FN(BAZ);;
```
, which will then be expanded to:
```c
void func_FOO(int); void func_BAR(int); void func_BAZ(int);;
```
, i.e. expanded to the definition of three function declarations with the same prefix.

You may also use this trick to simplify **enum** declaration, consider the following:
```c
#define EXAMPLE_ENUM(eg) EG_##eg,
enum example {
  EG_NULL = 0,
  EXAMPLE(EXAMPLE_ENUM)
};
```
This is equivalent to:
```c
enum example {
  EG_NULL = 0,
  EG_FOO, EG_BAR, EG_BAZ,
};
```

#### Instruction:
Write a short c program that uses macros in a complex way.
"""

TYPEDEF_PROMPT = """
The keyword typedef is used in a declaration, in the grammatical position of a storage-class specifier, except that 
it does not affect storage or linkage:

typedef char char_t, *char_p, (*fp)(void);

Here we declares char_t to be an alias for char; char_p to be an alias for char *, fp to be an alias for char(*)(void).
Note that typedef name may be an incomplete type, which may be completed as usual:

typedef int A[]; // A is int[]
A a = {1, 2}, b = {3, 4, 5}; // type of a is int[2], type of b is int[3].

### Instruction: Write a short c program that uses typedef in a complex way.
"""


INASM_PROMPT = """
### Inline Assembly
In c language, inline assembly has the following format:
```c
asm volatile ("assembly" : input : output : clobbers);
```
Here `volatile` is optional, and `asm` can be replaced by `__asm__`.

Here's some examples:
1. `r_esp` read the value of register esp:
```c
static inline int r_eax () {
  int x;
  __asm__ volatile ("movl %%eax, %0" : "=r" (x));
  return x;
}
```
2. `w_esp` put the value of x into register esp:
```c
static inline void w_eax (int x) {
  __asm__ volatile ("movl %0, %%eax" : : "r" (x));
}
```
3. `sum` performs addition on two integers:
```c
static int sum(int a, int b) {
  // set eax to zero
  __asm__ volatile ("xor %eax, %eax");
  // set eax to be a
  __asm__ volatile ("add %0, %%eax" : : "r"(a));
  // set eax to be a + b.
  __asm__ volatile ("add %0, %%eax" : : "r"(b));  
  // return the value, in eax.
  return r_eax ();
}
```

You may want to try out using these functions yourself:
```c
int main (int argc, char **argv) {
  w_eax(0xf3a519cd);
  printf ("%x\n", r_eax());
  printf ("%d\n", sum(1, 4));
  asm volatile("int $0x30");
  return 0;
}
```

### Your Task
Write a short c program that uses inline assembly in a complex way.
"""

COMMA_PROMPT = """
### Comma Operator
In C, the comma operator (,) is a binary operator that allows multiple expressions to be evaluated in a single compound expression, returning the value of the last expression. This operator can be particularly useful for performing a sequence of operations where the result of the previous operations is not needed. Here’s a code snippet example:
```c
#include <stdio.h>

int main() {
    int a = 1, b = 2, c = 3;
    int result = (a++, b++, c);
    printf("Result is: %d\n", result); // Outputs: Result is: 3
    printf("a is: %d\n",a); //Outputs: a is: 2
    printf("b is: %d\n",b); //Outputs: b is: 3
    return 0;
}
```

### Instruction:
Please create a short c program that uses the comma operator in a complex way.
"""

INIT_PROMPT = """
### Initializer Designators
For C language in C99, initializer designators were introduced, allowing for the initialization of specific members of structures and arrays. This feature provides a more flexible and readable way to initialize complex data types. Here’s code snippet example:
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

### Instruction:
Please create a short c program that uses initializer designators in a complex way.
"""

LABEL_PROMPT = """
### Label variables
In C language， it is possible to use labels as targets for goto statements, which allows the program to jump to a specific point in the code. However, a lesser-known feature is the ability to store these labels in variables, enabling dynamic control over the jump destination. Here’s a detailed description of how this is achieved in the provided code snippet example:
“In the following C code example, a pointer to a label is stored in a variable, which is then used as a dynamic target for a goto statement. The code begins by declaring a void* variable named label and initializing it with the address of a label named end using the && operator. This operator returns the address of the label. Next, the program prints a message indicating it is before the goto statement. The goto statement itself is then executed with goto *label;, which instructs the program to jump to the location pointed to by the label variable. Consequently, the line of code that would print ‘This will not be printed.’ is skipped, and the program execution continues at the end: label, printing ‘After goto.’ to the console.”
```c
#include <stdio.h>

int main (){
  // store the label in a variable
  void *label = &&end;
  printf("Before label\n");
  goto *label;  // jump to the label, end 
  printf("Will not be printed");
end:
  printf("After label\n");
  return 0;
}
```

### Instruction:
Please create a short c program that uses label variables as "goto" targets in a complex way.
"""

NEST_FN_PROMPT = """
### Nested functions
In C, although nested functions are not officially supported by the C99 standard, certain compilers, such as GCC, provide an extension that allows for this feature. A nested function is defined within the scope of another function, enabling it to access variables from its enclosing function. Here’s a code snippet example of how nested function is implemented:

```c
#include <stdio.h>

void inner() {
  printf("Oh, inner!\n");
}
void outer() {
    printf("Hello from outer fn\n");
    void inner() {
        printf("Hello from inner fn\n");
    }
    inner ();
}

int main () {
    inner();  // Oh, inner!
    outer();  // Hello from outer fn! \
                 Hello from inner fn!
}
```

### Instruction
Create a short c program which uses nested functions in a complex way.
"""

STAT_EXPR_PROMPT = """
### Statement Expression
In c programming language, you can use `({...})` to create a statement expression, which allows for multiple statements to be executed within it, returning the value of the last expression, here's a short example:
```c
#include <stdio.h>

int main (){
  int day = 3; // third day of a week
  const char *s = ({
    const char *ret;
    switch (day) {
      case 1: ret="Monday"; break;
      case 2: ret="Tuesday"; break;
      case 3: ret="Wednesday"; break;
      case 4: ret="Thursday"; break;
      case 5: ret="Friday"; break;
      case 6: ret="Saturday"; break;
      case 7: ret="Sunday"; break;
    }
    ret;  // will be assigned to s
  });
  printf ("Today is %s\n", s); // Today is Wednesday
  return 0;
}
```

### Instruction
Create a short c program that uses statement expression in a complex way.
"""
ZERO_ARR_PROMPT = """
### Zero-length Array
For C language in C99, the concept of zero-length arrays was introduced, allowing for the dynamic allocation of array sizes within structures. This feature enables the creation of flexible data structures that can be allocated with a variable number of elements at runtime. Here's a detailed code snippet example :
"In the following C code example, a structure named flex_array is defined, which contains an integer count to store the number of elements and a zero-length array data of type double. The zero-length array does not consume any memory within the structure itself but serves as a placeholder for the actual data array that will be allocated dynamically. 
In the main function, an integer n is initialized to specify the number of elements desired for the array. The flex_array structure is then allocated using malloc, with the size of the structure plus the total size needed for n double elements. The count member of the structure is set to n, indicating the number of elements in the array. A loop is used to populate the data array with values, multiplying each index by 1.5 to assign a value to each element. Another loop is used to print the values of the data array elements to the console.
Finally, the allocated memory for the flex_array structure, including the dynamically allocated data array, is freed using free. This example demonstrates how zero-length arrays can be used to create flexible and efficient data structures in C."
```c
#include <stdio.h>
#include <stdlib.h>

struct flex_array {
    int count;
    double data[0]; // Zero-length array
};

int main() {
    int n = 5;
    struct flex_array *arr = malloc(sizeof(struct flex_array) + n * sizeof(double));
    arr->count = n;
    for (int i = 0; i < n; ++i) {
        arr->data[i] = i * 1.5;
    }
    for (int i = 0; i < n; ++i) {
        printf("arr->data[%d] = %f\n", i, arr->data[i]);
    }
    free(arr);
    return 0;
}
```

Note that the following will not compile("assignment to array type"):
```c
struct flex_array *arr = malloc(sizeof(struct flex_array));
arr->data = (double *)malloc(sizeof(double) * 4);
```

### Instruction:
Please create a short c program that uses zero-length array in a complex way.
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
