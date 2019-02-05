#ifndef RING_BUGGER_RING_H
#define RING_BUFFER_RING_H

#include "resizable_array.h"
#include <stdbool.h>
#include <stdio.h>

struct ring_buffer {
  RArray* ray;
  size_t head;
  size_t tail;
  size_t max;
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
