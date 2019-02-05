#include "ring.h"

void init_ring_buffer() {
  RArray ra;

  init(&ra, 10);
}

void push(RArray* ra, BuffNode bn) {
  append(ra, bn);
}

BuffNode pop(RArray* ra) {
  int len = sizeof(&ra)/sizeof(&ra[0]) - 1;
}
