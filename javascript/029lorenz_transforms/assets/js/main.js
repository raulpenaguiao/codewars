const cross = function(vec1, vec2){
  let v0 = vec1[1]* vec2[2] - vec1[2]* vec2[1];
  let v1 = vec1[2]* vec2[0] - vec1[0]* vec2[2];
  let v2 = vec1[0]* vec2[1] - vec1[1]* vec2[0];
  return [v0, v1, v2];
}

const dot = function(vec1, vec2){
  return vec1[0]*vec2[0] + vec1[1]*vec2[1] + vec1[2]*vec2[2];
}

const scal = function(sc, vec){
  let ans = new Array(vec.length);
  for(let i = 0; i< vec.length; i++){
    ans[i] = vec[i] * sc;
  }
  return ans;
}

const add = function(vec1, vec2){
  let ans = new Array(vec1.length);
  for(let i = 0; i< vec1.length; i++){
    ans[i] = vec1[i] + vec2[i];
  }
  return ans;
}

const transformFields = (electric, magnetic, velocity) => {
  let norm_v = 0;
  for(let i=0; i < velocity.length; i++){
    norm_v += velocity[i]**2;
  }
  norm_v = Math.sqrt(norm_v);
  if(norm_v >= 1){
    return null
  }
  let phi = Math.atanh(norm_v);
  let uhat = new Array(3);
  uhat = scal(1/norm_v, velocity);
  let Eprime = new Array(3);
  let aux = new Array(3);
  Eprime = scal(Math.cosh(phi), electric);
  aux = cross(uhat, magnetic);
  aux = scal(Math.sinh(phi), aux);
  Eprime = add(Eprime, aux);
  aux = scal(- 2 * Math.sinh(phi / 2)* Math.sinh(phi / 2) * dot(uhat, electric), uhat);
  Eprime = add(Eprime, aux);
  console.log(Eprime);
  let Bprime = new Array(3);
  Bprime = scal(Math.cosh(phi), magnetic);
  aux = scal(-Math.sinh(phi), cross(uhat, electric));
  Bprime = add(Bprime, aux);
  aux = scal(- 2 * Math.sinh(phi / 2)* Math.sinh(phi / 2) * dot(uhat, magnetic), uhat);
  Bprime = add(aux, Bprime);
	return [Eprime, Bprime];
  // do Lorentz-Transform for electric and magnetic field vectors
}
