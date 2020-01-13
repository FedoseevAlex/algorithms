#include <iostream>
#include <vector>
#include <sstream>
#include <string>

std::pair<long, long> extract_numbers(std::string, int);

int main(void){
  std::string buf;

  std::cin.width(99);
  std::cin >> buf;

  long rows = 0;
  rows = std::stol(buf);

  std::vector<std::pair<long, long>> non_blurred = {{0, 0}};
  std::string raw_nums = {0};
  for(long r = 0; r < rows; r++){
    std::getline(std::cin, raw_nums);
    non_blurred.push_back(extract_numbers(raw_nums, 2));
  }
  std::cout << "array = ";
  for(auto item: non_blurred){
    std::cout << "{" << item.first << " " << item.second << "}" ;
  }

  return EXIT_SUCCESS;
}


std::pair<long, long> extract_numbers(std::string str, int nums_count){
  std::pair<long, long> result = {0, 0};

  for(int i = 0; i < nums_count; i++){
    std::size_t start_pos = str.find_first_of("0123456789");

    if(start_pos == std::string::npos){
      return result;
    }

    std::size_t end_pos = str.find_first_not_of("0123456789", start_pos);
    std::string to_convert = str.substr(start_pos,
                                        std::string::npos == end_pos ? end_pos: end_pos - start_pos);
    std::cout << std::stol(to_convert) << " found" << std::endl;
    str = str.substr(end_pos);
  }

  return result;
}
