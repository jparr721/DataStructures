#ifndef RING_BUGGER_RING_H
#define RING_BUFFER_RING_H

#include "resizable_array.h"
#include <stdbool.h>
#include <stdio.h>

// Defines the ring buffer struct
struct ring_buffer {
  // Our resizable array
  RArray* ray;
  // Our reference to the head of the list
  size_t head;
  // Our reference to the tail of the list
  size_t tail;
  // Our max size
  size_t max;
  // Whether or not it's full
  bool full;
};

void push(struct ring_buffer* rb, BuffNode bn);
void offer(struct ring_buffer* rb, BuffNode bn);
void remove_value(RArray* array, int index);
void buffer_reset(struct ring_buffer* rb);
void init_ring_buffer();

bool buffer_full(struct ring_buffer* rb);

size_t buffer_size(struct ring_buffer* rb);

BuffNode pop(RArray*);

#endif
