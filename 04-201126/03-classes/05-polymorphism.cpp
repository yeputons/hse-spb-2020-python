#include <iostream>
#include <vector>

// Полиморфная функция: написали один раз, работает с разными данными по-разному.
template<typename Container>
void print_all(const Container &c) {
    for (const auto &x : c) {
        std::cout << x << "\n";
    }
}

int main() {
    int arr[]{10, 20, 30};
    print_all(arr);
    print_all(std::vector{1, 2, 3});
    return 0;
}
