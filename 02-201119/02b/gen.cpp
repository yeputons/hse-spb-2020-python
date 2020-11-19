#include <random>
#include <iostream>

int main() {
    std::random_device gen;
    std::uniform_int_distribution<int> n_distrib(1, 300'000);
    std::cout << n_distrib(gen) << "\n";
}
