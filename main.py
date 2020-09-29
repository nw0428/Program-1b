import sys

# <- notice these. What do you think they do?
# int means integer which is math for "whole number"
# feel free to edit this code as you would like

# I originally wrote this in Java so there may
# be some weird errors that need to be fixed

def fun0():
    name = ""
    message = "It's nice to meet you ";
    print("What is your name? ")
    name = input();
    print(message, end="")
    print(name)
    return name


def fun1():
    f = int(input("Please give me a temperature in farenheit: "))
    c = ((f - 32) * 5) / 9
    print("That is " + str(c) + " in celcius")


def fib():
    print("How many numbers should I produce? ")
    q = int(input())

    i = 0
    a = 0
    b = 1

    while (i < q):
        temp = a
        a = b
        b = a + temp
        #print(str(a), end = " ")
        i = i + 1
        print(i)

    print()

# public static int fun3(int number) {
#   if (number < 0) {
#     System.out.println("Number must be greater than zero");
#     System.exit(1);
#   }
#   if (number < 2) {
#     return 1;
#   }
#   return number * fun3(number - 1);
# }


# Hello world to make sure the program is running
print("Hello World!")

choice = int(input("Please chose program 0, 1, 2, or 3: "))

print("You chose " + str(choice))

if (0 == choice):
    fun0();

if (1 == choice):
    fun1();

if (2 == choice): # If 2 is the choice you made
    fib();

# if (3 == choice) {
#   System.out.println("Please provide a number: ");
#   int number;
#   number = (new Scanner(System.in)).nextInt();
#   System.out.println(fun3(number));
# }
name = ""
if (len(sys.argv) > 1):
    name = sys.argv[1]

print("Thanks " + name)


#For homework please do at least one of the following
# Fully annotate the program
# Add Python rules to our shared class document
# Add a code exploration/investigation/experimentation strategy you used in class to the document
# Get fun3 working and explain what it does