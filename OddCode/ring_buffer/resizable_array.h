#ifndef RING_BUFFER_RESIZABLE_ARRAY_H
#define RING_BUFFER_RESIZABLE_ARRAY_H

#include <stdlib.h>
#include <stdio.h>

typedef struct {
  char* title;
  char* body;
} BuffNode;

typedef struct {
  BuffNode* array;
  size_t used;
  size_t size;
} RArray;

void init(RArray* array, size_t size);
void append(RArray* array, BuffNode element);
void freeArray(RArray *array);

#endif
