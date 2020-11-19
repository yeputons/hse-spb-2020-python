#include <cstdlib>
#include <ctime>
#include <iostream>

int main() {
    srand(time(nullptr));
    {
        long long x;
        asm("rdtsc" :: "=A"(x));
        srand(x);
    }
    std::cout << rand() % 300'000 + 1 << "\n";
    std::cout << RAND_MAX << "\n";
    (rand() << 16) ^ rand()
}
