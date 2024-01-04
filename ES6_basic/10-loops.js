export default function appendToEachArrayValue(array, appendString) {
  const thearray = [];
  for (const idx of array) {
    const value = appendString + idx;
    thearray.push(value);
  }

  return thearray;
}
