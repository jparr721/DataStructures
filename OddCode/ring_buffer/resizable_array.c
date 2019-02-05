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

void freeArray(RArray *array) {
  free(array->array);
  array->array = NULL;
  array->used = array->size = 0;
}
