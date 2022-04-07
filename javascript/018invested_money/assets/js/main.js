function calculateYears(principal, interest, tax, desired) {
  let current = principal, year = 0;
  while(current  < desired){
    current += current*interest*(1 - tax);
    year += 1;
  }
  return year
    // your code
}
