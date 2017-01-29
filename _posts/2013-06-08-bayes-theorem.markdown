---
layout: post
title: Bayes' Theorem
post_id: '1861'
categories:
- Mathematics
tags:
- machine learning
status: publish
type: post
published: true
meta:
  _edit_last: '1'
  dsq_thread_id: '1380044454'
author:
  login: admin
  email: suminb@gmail.com
  display_name: Sumin
  first_name: Sumin
  last_name: Byeon
redirect_from:
  - /archives/1861/
redirect_to:
  - http://philosophical.one/post/bayes-theorem
---
In this article, I will explain Bayes' Theorem, which is the core of the Bayesian statistics, with a simple example.

First, the theorem is given as:

$$ P(A|B) = \frac{P(B | A)\, P(A)}{P(B)} \text{ where } P(B) = {\sum_i P(B|A_i) P(A_i)} \neq 0 $$

And here is the situation:

> Suppose two companies, A and B, manufacture 4.6L SOHC V-6 engines that go into a Mustang. Ford bought 5000 engines from those two companies, and
>
> * 9 out of 1000 engines from company A were defective.
> * 25 out of 4000 engines from company B were defective.

Now, the question is:

> What is the probability that a defective engine came from company B?

Define some variables we need:

* A = the engine came from company A
* B = the engine came from company B
* D = the engine is defective

Let's write down the original question in a bit more formal way. What is the probability of B given D? In other words, what is the probability that the engine came from company B given it is defective?

Here is the conditional probability of getting a defective engine from company A:

$$ P(D|A) = \frac{9}{1000} = 0.009 $$

Likewise, the conditional probability of getting a defective engine from company B is:

$$ P(D|B) = \frac{25}{4000} = 0.0625 $$

The prior probability of an engine coming from company A is:

$$ P(A) = \frac{1000}{5000} = 0.2 $$

Similarly for B:

$$ P(B) = \frac{4000}{5000} = 0.8 $$

Now we have what we need to calculate $P(B|D)$.

$$ P(B|D) = \frac{P(B)P(D|B)}{P(A)P(D|A) + P(B)P(D|B)} = \frac{(0.8)(0.0625)}{(0.2)(0.009) + (0.8)(0.0625)} \approx 0.965 $$

So, when Ford finds a defective engine, it's most likely coming from company B.

