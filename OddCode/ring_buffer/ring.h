#include <stdio.h>
#include "resizable_array.h"

struct ring_buffer {
  RArray ray;
};

void push(RArray*, BuffNode bn);
void init_ring_buffer();

BuffNode pop(RArray*);
