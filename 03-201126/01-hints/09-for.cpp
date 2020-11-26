#include <iostream>

int main() {
    for (int x : {2, 3}) {  // UB? Not sure.
        std::cout << x << "\n";
    }
}
