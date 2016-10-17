#include <iostream>

int main() {
    int T, N;
	std::cin >> N;
    for (int i = 0; i < N; ++i) {
        std::cin >> T;
        int j;
        for (j = 0; j < 12; ++j) {
            int v = T - j * 10;
            if (v < 0)
            {
                j = 12;
                break;
            }
            if ((T - j * 10) % 12 == 0)
            {
                std::cout << j + (T - j * 10) / 12 << std::endl;
                break;
            }
        }
        if (j == 12) std::cout << -1 << std::endl;
    }
	return 0;
}
