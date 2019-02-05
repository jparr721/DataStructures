#include "ring.h"
#include <assert.h>

void init_ring_buffer() {
  RArray ra;

  init(&ra, 10);
}

void push(struct ring_buffer* rb, BuffNode bn) {
  append(rb->ray, bn);
}

void offer(struct ring_buffer* rb, BuffNode bn) {
  if (!rb->full) {
    rb->tail = (rb->tail + 1) % rb->max;
    append(rb->ray, bn);
  }

  rb->head = (rb->head + 1) % rb->max;
  rb->full = (rb->head == rb->tail);
}

void buffer_reset(struct ring_buffer* rb) {
  assert(rb);

  rb->head = 0;
  rb->tail = 0;
  rb->full = false;
}

bool buffer_full(struct ring_buffer* rb) {
  assert(rb);

  return rb->full;
}

size_t buffer_size(struct ring_buffer* rb) {
  assert(rb);

  return rb->ray->size;
}

BuffNode pop(RArray* ra) {
  int len = sizeof(ra->array)/sizeof(ra->array[0]) - 1;

  return ra->array[len];
}
