function DNAStrand(dna){
    //your code here
    return dna.replace(/A/g, "1").replace(/T/g, "A").replace(/1/g, "T").replace(/G/g, "1").replace(/C/g, "G").replace(/1/g, "C")
  }
