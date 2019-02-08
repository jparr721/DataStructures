#ifndef RING_BUFFER_RESIZABLE_ARRAY_H
#define RING_BUFFER_RESIZABLE_ARRAY_H

#include <stdio.h>
#include <stdlib.h>

// Defines a buffer node which holds the data, in this case, our title and body of each passage of text
typedef struct {
  char* title;
  char* body;
} BuffNode;

// Our resizable array parameters
typedef struct {
  BuffNode* array;
  size_t used;
  size_t size;
} RArray;

void init(RArray* array, size_t size);
void append(RArray* array, BuffNode element);
void freeArray(RArray *array);

#endif
