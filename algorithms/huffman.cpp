#include <iostream>
#include <unordered_map>
#include <iterator>
#include <set>

bool comparator(std::pair<char, int> a, std::pair<char, int> b);

int main(void){
  const int max_input = 10000;
  char buf[max_input] = {0};

  std::cin.width(max_input + 1);
  std::cin >> buf;

  std::unordered_map<char, int> letters;
  for(char *item = std::begin(buf); item != std::end(buf) && *item != 0; item++){
    if(letters.count(item[0]) == 0){
      letters[*item] = 1;
    } else {
      letters[*item] += 1;
    }
  }

#ifdef DEBUG
  std::cout << "Mapping:\n";
  for(std::pair<char, int> x: letters){
    std::cout << x.first << ": " << x.second << "\n";
  }

  std::cout << "Buffer:\n";
  std::cout << buf << "\n";
#endif /*DEBUG*/

  return EXIT_SUCCESS;
}


bool comparator(std::pair<char, int> a, std::pair<char, int> b){
  return a.second > b.second;
}

