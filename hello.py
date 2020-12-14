import numpy as np

msg = "hello world";
print(msg);

#init the numpy array
array = np.array([-1,2,5], dtype=np.float);

#print the array representation
print(repr(array));

print(array);

newarray = np.array([[0,1,2], [3,4,5]], dtype=np.int);
print(repr(newarray));

print(newarray);


##upcasting arrays
floatarray = np.array([1,2.34,3,5]);
print(floatarray);

stringarray = np.array([1,34,42, "eifoj", "ojeiof"]);
print(stringarray);


##copying arrays

a = np.array([0,1]);
b = np.array([9,8]);

c = a;
print('Array a: {}', format(repr(a)));

c[0] = 5;
print('Array a: {}', format(repr(a)));

d = b.copy();
d[0] = 6;
print('Array b : {}', format(repr(b)));
print('Array d : {}', format(repr(d)));

#casting in arrays
castArray = np.array([0,1,2]);
print(castArray.dtype);

castArray = castArray.astype(np.float32);
print(castArray.dtype);
