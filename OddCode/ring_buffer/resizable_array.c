#include "resizable_array.h"

// Init mallocs our data and sets up our data structures
void init(RArray* array, size_t size) {
  array->array = (BuffNode*) malloc(size * sizeof(BuffNode));
  array->used = 0;
  array->size = size;
}

// Adds to an array. If it is full, double the capacity
void append(RArray* array, BuffNode element) {
 if (array->used == array->size) {
    array->size *= 2;
    array->array = (BuffNode*)realloc(array->array, array->size * sizeof(BuffNode));
  }
  array->array[array->used++] = element;
}

// Removes a value from an array given an index, throws an error if out of bounds
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

// Frees memory associated with the Array to avoid leaks
void freeArray(RArray* array) {
  free(array->array);
  array->array = NULL;
  array->used = array->size = 0;
}
