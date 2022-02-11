**What is a git?**

Git is an open source version control system that helps in managing large and small projects efficiently. One code base can have multiple versions which minimizes the risk especially when breaking changes are introduced to a project.

**What is a github?**

Github is an online repository for open source projects that makes it easier for engineers to collaborate on projects.

# [Generative Adverserial Networks](https://machinelearningmastery.com/what-are-generative-adversarial-networks-gans/)

![version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![license](https://img.shields.io/badge/license-MIT-blue.svg)

Generative Adversarial Networks, or GANs for short, are an approach to [generative modeling](https://developers.google.com/machine-learning/gan/generative#:~:text=A%20generative%20model%20includes%20the,to%20a%20sequence%20of%20words.) using deep learning methods, such as convolutional neural networks.

**What is a generative model?**

Generative models can generate new data instances. Generative modeling is an unsupervised learning task in machine learning that involves automatically discovering and learning the regularities or patterns in input data in such a way that the model can be used to generate or output new examples that plausibly could have been drawn from the original dataset.

![Meme](https://miro.medium.com/max/1152/1*Lhma2luPtlXXKGNcwFPmrg.jpeg)

For example, a single variable may have a known data distribution, such as a Gaussian distribution, or bell shape. A generative model may be able to sufficiently summarize this data distribution, and then be used to generate new variables that plausibly fit into the distribution of the input variable. A really good generative model may be able to generate new examples that are not just plausible, but indistinguishable from real examples from the problem domain.

**Examples of generative models**

## Naive Bayes

It is a simple but surprisingly powerful algorithm for predictive modeling. Naive Bayes works by summarizing the probability distribution of each input variable and the output class. When a prediction is made, the probability for each possible outcome is calculated for each variable, the independent probabilities are combined, and the most likely outcome is predicted. Used in reverse, the probability distributions for each variable can be sampled to generate new plausible (independent) feature values.

## Latent Dirichlet Allocation

It is one of the most popular [topic modeling](https://towardsdatascience.com/latent-dirichlet-allocation-lda-9d1cd064ffa2) methods. Each document is made up of various words, and each topic also has various words belonging to it. The aim of LDA is to find topics a document belongs to, based on the words in it. Confused much? Here is an example to walk you through it.

## Gaussian Mixture Model

A Gaussian mixture model is a probabilistic model that assumes all the data points are generated from a mixture of a finite number of Gaussian distributions with unknown parameters.

![Meme](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRig5tsZDbTvQsODbQ5-E1t89X2odIlrrYt4Q7wWHOLJI5iuHxEGUYRrm2gyKthY871BDc&usqp=CAU)

One can think of mixture models as generalizing k-means clustering to incorporate information about the covariance structure of the data as well as the centers of the latent Gaussians.

## Interesting application areas of GANS

- Generate Examples for Image Datasets

![Meme](https://machinelearningmastery.com/wp-content/uploads/2019/04/Examples-of-GANs-used-to-Generate-New-Plausible-Examples-for-Image-Datasets-1024x719.png)

- Generate Photographs of Human Faces

![Meme](https://machinelearningmastery.com/wp-content/uploads/2019/06/Examples-of-Photorealistic-GAN-Generated-Faces.png)

- Generate Realistic Photographs

![Meme](https://machinelearningmastery.com/wp-content/uploads/2019/06/Example-of-Realistic-Synthetic-Photographs-Generated-with-BigGAN.png)

- Generate Cartoon Characters

![Meme](https://machinelearningmastery.com/wp-content/uploads/2019/06/Example-of-GAN-Generated-Anime-Character-Faces.png)

- Image-to-Image Translation

![Meme](https://machinelearningmastery.com/wp-content/uploads/2019/06/Example-of-Sketches-to-Color-Photographs-with-pix2pix.png)

- Text-to-Image Translation

![Meme](https://machinelearningmastery.com/wp-content/uploads/2019/06/Example-of-Textual-Descriptions-and-GAN-Generated-Photographs-if-Birds-and-Flowers.png)
