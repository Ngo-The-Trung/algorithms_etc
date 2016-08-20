#include <assert.h>
#include <iostream>

int Add(int x, int y);

int Mul(int x, int y) {
    int sum = 0, counter = 0;
    while (counter < y) {
        counter = Add(counter, 1);
        sum = Add(sum, x);
    }
    return sum;
}

int Add(int x, int y) {
    int sum = 0, tmp_x = x, tmp_y = y, mask = 1;
    int carryin = 0, carryout, sum1bit;
    while (tmp_x | tmp_y | carryin) {
        sum1bit = (x & mask) ^ (y & mask) ^ carryin;
        carryout = ((x & mask) & carryin) | ((y & mask) & carryin) | ((x & mask) & (y & mask));
        sum |= sum1bit;
        mask <<= 1;
        tmp_x >>= 1, tmp_y >>= 1;
        carryin = carryout << 1;
    }
    return sum;
}

void Test() {
    assert(Add(0, 0) == 0);
    assert(Add(0, 1) == 1);
    assert(Add(1, 0) == 1);
    assert(Add(1, 1) == 2);
    assert(Add(239480, 230498) == 469978);

    assert(Mul(0, 0) == 0);
    assert(Mul(0, 1) == 0);
    assert(Mul(1, 0) == 0);
    assert(Mul(1, 1) == 1);
    assert(Mul(23980, 2398) == 57504040);
}

int main()
{
    Test();

    return 0;
}
