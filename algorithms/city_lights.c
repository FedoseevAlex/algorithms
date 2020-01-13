#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

unsigned int max(unsigned int, unsigned int);
unsigned int advanced(unsigned int N, unsigned char k, unsigned int is[]);

int main(void) {
  char buf[100] = {0};
  char* err = NULL;

  unsigned int N = 0;
  err = fgets(buf, 100, stdin);
  if(err == NULL){
    return EXIT_FAILURE;
  }
  N = atoi(buf);

  unsigned char k = 0;
  err = fgets(buf, 100, stdin);
  if(err == NULL){
    return EXIT_FAILURE;
  }
  k = atoi(buf);

  unsigned int *is;
  is = calloc(k, sizeof(unsigned int));

  for (unsigned char i = 0; i < k; i++) {
    err = fgets(buf, 100, stdin);
    if(err == NULL){
      return EXIT_FAILURE;
    }
    is[i] = atoi(buf);
  }

  printf("%u\n", advanced(N, k, is));
  return EXIT_SUCCESS;
}

unsigned int advanced(unsigned int N, unsigned char k, unsigned int is[]) {
  unsigned int result = 0;

  bool *lights;
  lights = calloc(N, sizeof(bool));

  unsigned int counter = 0;
  for (unsigned int idx = 0; idx < k; idx++) {
    for (unsigned int n = is[idx]; n < N + 1; n += is[idx]) {
      lights[n - 1] ^= true;
      if(lights[n - 1]){
        counter++;
      } else {
        counter--;
      }
    };
    result = max(result, counter);
  };

  free(lights);
  return result;
}

unsigned int max(unsigned int a, unsigned int b) { return a > b ? a : b; }
