#include <iostream>
#include <assert.h>

long SwapBits(long num, int i, int j) {
    if (((num >> i) & 1L) == ((num >> j) & 1L)) {
        return num;
    } else {
        return num ^ ((1 << i) | (1 << j));
    }
    return 0;
}

void TestSwapBits() {
    assert(SwapBits(0b100101011, 0, 1) == 0b100101011);
    assert(SwapBits(0b100101011, 0, 2) == 0b100101110);
    assert(SwapBits(0b100101011, 2, 3) == 0b100100111);
    assert(SwapBits(0b100101011, 5, 7) == 0b110001011);
}

int main()
{
    TestSwapBits();
    return 0;
}
