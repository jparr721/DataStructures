#include "resizable_array.h"

void init(RArray* array, size_t size) {
  array->array = (BuffNode*) malloc(size * sizeof(BuffNode));
  array->used = 0;
  array->size = size;
}

void append(RArray* array, BuffNode element) {
 if (array->used == array->size) {
    array->size *= 2;
    array->array = (BuffNode*)realloc(array->array, array->size * sizeof(BuffNode));
  }
  array->array[array->used++] = element;
}

void remove_value(RArray* array, size_t index) {
  int len = sizeof(array->array)/sizeof(array->array) - 1;
  if (index > len) {
    perror("Array index out of bounds");
    return;
  }

  //  Overwrite old values and move the rest
  for (int i = index; i < len - 1; ++i) {
    array->array[i] = array->array[i + 1];
  }
}

void freeArray(RArray* array) {
  free(array->array);
  array->array = NULL;
  array->used = array->size = 0;
}
