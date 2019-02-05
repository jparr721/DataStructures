// Lib functions for euler
#include <cmath>
#include <type_traits>

class Lib {
  template<typename T>
  bool multiple_of(T value, T check) {
    static_assert(std::is_arithmetic<T>::value, "We need a number for this function, pal");
    return std::fmod(value, check);
  }
};
