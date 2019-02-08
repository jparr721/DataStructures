#include "ring.h"
#include <assert.h>

void init_ring_buffer() {
  RArray ra;

  init(&ra, 10);
}

// Pushes to an array regardless of available space
void push(struct ring_buffer* rb, BuffNode bn) {
  append(rb->ray, bn);
}

// Pushes to an array if and only if space is available
void offer(struct ring_buffer* rb, BuffNode bn) {
  if (!rb->full) {
    rb->tail = (rb->tail + 1) % rb->max;
    append(rb->ray, bn);
  }

  rb->head = (rb->head + 1) % rb->max;
  rb->full = (rb->head == rb->tail);
}

// Resets the ring buffer
void buffer_reset(struct ring_buffer* rb) {
  assert(rb);

  // TODO: Call array delete method
  rb->head = 0;
  rb->tail = 0;
  rb->full = false;
}

// Chcecks if the ring buffer is full
bool buffer_full(struct ring_buffer* rb) {
  assert(rb);

  return rb->full;
}

// Returns the current array size
size_t buffer_size(struct ring_buffer* rb) {
  assert(rb);

  return rb->ray->size;
}

// Pops the first element off of the front of the queue
BuffNode pop(RArray* ra) {
  struct BuffNode bn = ra->array[rb->head];
  remove_value(rb->ray, rb->head);
  return bn;
}
