#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

std::vector<long> extract_numbers(std::string, int);
int picture(std::vector<std::vector<long>> ranges);

int main(void){
  std::string buf;

  std::cin.width(99);
  std::getline(std::cin, buf);

  long rows = 0;
  rows = std::stol(buf);

  std::vector<std::vector<long>> non_blurred;
  std::string raw_nums;
  for(long r = 0; r < rows; r++){
    std::getline(std::cin, raw_nums);
    non_blurred.push_back(extract_numbers(raw_nums, 2));
  }

  std::cout << picture(non_blurred) << std::endl;

  return EXIT_SUCCESS;
}


std::vector<long> extract_numbers(std::string str, int nums_count){
  std::vector<long> result;
  std::size_t start_pos = 0, end_pos = 0;

  for(int i = 0; i < nums_count; i++){
    start_pos = str.find_first_of("0123456789");

    if(start_pos == std::string::npos){
      return result;
    }

    end_pos = str.find_first_not_of("0123456789", start_pos);
    std::string to_convert = str.substr(start_pos);
    result.push_back(std::stol(to_convert));
    if(end_pos != std::string::npos){
      str = str.substr(end_pos);
    }
  }
  return result;
}

int picture(std::vector<std::vector<long>> ranges){
  int **array = new int*[ranges.size()];
  for(unsigned long i = 0; i < ranges.size(); i++){
    array[i] = new int[ranges.size()]{0};
  }

  int result = 0;
  for(int i = 0; i < (int) ranges.size(); i++){
    for(long j = ranges[i][0]; j <= ranges[i][1]; j++){
      int upper = 0, diag = 0, left = 0;
      array[i][j] = 1;

      if(i - 1 >= 0 && j - 1 >= 0){
        diag = array[i - 1][j - 1];
        upper = array[i][j - 1];
        left = array[i - 1][j];
      } else if(i - 1 >= 0) {
        upper = array[i - 1][j];
      } else if(j - 1 >= 0) {
        left = array[i][j - 1];
      }
      array[i][j] += std::min({diag, upper, left});
      result = std::max({result, array[i][j]});
    }
  }

  for(unsigned long i = 0; i < ranges.size(); i++){
    delete[] array[i];
  }
  delete[] array;

  return result;
}
