#include <iostream>

void reduce(int num, int den)
{
    int a = num, b = den, rem;

    while (a > 0 && b > 0) {
        rem = a % b;
        a = b;
        b = rem;
    }
    std::cout << num/(a + b) << "/" << den/(a + b) << std::endl;
}

void addFraction(int num1, int den1, int num2,int den2)
{
    reduce(num1 * den2 + num2 * den1, den1 * den2);
}

int main(int argc, char *argv[])
{
    addFraction(237, 500, 163, 500);
    return 0;
}
