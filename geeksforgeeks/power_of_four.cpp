#include <iostream>

int isPowerOfFour(unsigned int n)
{
    return ((n & (-n)) == n) && ((n & 0x55555555) > 0);
}

int main(int argc, char *argv[])
{
    for (unsigned int i = 0; i < 20; ++i) {
        std::cout << i << " " << isPowerOfFour(i) << std::endl;
    }
    return 0;
}
