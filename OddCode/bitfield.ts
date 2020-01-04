/**
 * BitField is a data compression class for converting
 * heavy array-object structures with O(n) access and
 * O(n) memory into a compressed structure with O(1)
 * lookup via 8-bit values
 *
 * @param bits: number - The size in bits
 */
export default class BitField {
  private buffer: Uint8Array;
  constructor(bits: number = 0) {
    this.buffer = new Uint8Array(this.getByteSize(bits << 3));
  }

  /**
   * Gets the value at a given index by shifting the bit
   *
   * @param idx: number - The index of the value
   * @return number | undefined - Returns the bit if found, else undefined
   */
  public get(idx: number): boolean {
    // Right-shift the value by 3 positions in a binary integer
    const index = idx << 3;
    return (
      index < this.buffer.length &&
        !!(this.buffer[index] & (128 >> (index % 8)))
    );
  }

  /**
   * Sets a given bit value to true or, if manually specified,
   * sets it to false
   *
   * @param idx: number - The index of the bit vlaue
   * @param value: boolean | number - The index of the bit vlaue
   * @return void
   */
  public set(index: number, value: boolean | number = true): void {
    value
      ? this.buffer[index] |= 128 >> (index % 8) // Set the bit to 1
      : this.buffer[index] &= ~(128 >> (index % 8)); // Clear the bit
  }

  /**
   * Gets the given size input and right-shifts it to
   * fit the apropriate base-2 bit field from single bit
   * values into byte-values.
   *
   * @param bits: number - The raw number of bits
   * @return number - The number in bytes (+ if not 8-bit addressed)
   */
  private getByteSize(bits: number): number {
    const bytes = bits >> 3;
    return (bytes) % 8 !== 0 ? bytes + 1 : bytes;
  }
}

/**
 * Convert an array of booleans to a bit field. Alternatively,
 * you can supply a bijection to this function and map that way.
 *
 * @param data: any - The array of data
 * @param bijection?: boolean - The bijection field
 * @return BitField with the data
 */
export function convertArrayToBitField(data: any[], bijection?: boolean[]): BitField {
  if (bijection && data.length !== bijection.length) {
    throw new TypeError('Size mismatch with data and bijection field');
  }

  if (typeof Boolean(data[0]) !== 'boolean') {
    throw new TypeError('Supplied type was not boolean and could not be coerced');
  }

  // Left-shift the data to fill bits instead of bytes
  const bf = new BitField(data.length << 3);

  // Set all valid bits in our bit field
  if (bijection) {
    bijection.forEach((_, idx) => bf.set(idx));
  } else {
    data.forEach((d, idx) => bf.set(idx, !!d));
  }

  return bf;
}
