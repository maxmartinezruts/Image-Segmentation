# Image Segmentation with Gibbs Sampling
Use of a practical variant of Gibbs sampling to achieve binary image segmentation
Given an image of size NxM
- Y<sub>i</sub> represents the value of pixel i
- X<sub>i</sub> represents the laber of pixel i. This is 0 if classified as A and 1 if classified as B.
- mu<sub>x<sub>i</sub></sub> is the mean of the pixel values given x. This is a vector [mu<sub>0</sub>, mu<sub>1</sub>]


Then, we can the distribution P(x<sub>i</sub>) as
P(x<sub>i</sub>) = Q(x<sub>i</sub>) * R(x<sub>i</sub>,x<sub>J</sub>)
Where J is the set of all neighbours of i. Then

Where Q is a distribution that considers only the pixel value and copares it to the pixel values of the means of the labels
Q(x<sub>i</sub>) = exp((y<sub>i</sub>-mu<sub>x<sub>i</sub></sub>)<sup>2</sup>/2 * s<sup>2</sup>)
Such that Q is higher for pixel values that are closed to the mean of label x<sub>i</sub>.

And where P is a distribuiton that considers the labels of the neighbours
R(x<sub>i</sub>,x<sub>j</sub>) exp(-B * (X<sub>i</sub>-X<sub>j</sub>)<sup>2</sup>) for all neighbours j of i.
Such that R is 1 if all neighbours of i have the same label of i and <1 otherwise (for B>0).

With that, Gibbs algorithm is described as following:

- Initialize all the labels i randomly.

- For t=1 to infinity:

- ... x<sub>i</sub> <- sample x<sub>i</sub> from P(x<sub>i</sub>)

Such approach satisfies the Detailed Balance Equation, and therefore converges to a stationary distribution P(x<sub>i</sub>)
