---
layout: post
title: Mathjax Matrix Rendering Issues with WordPress Markdown Plugin
post_id: '1920'
categories:
- Troubleshooting
tags:
- Markdown
- Mathjax
- matrix
- WordPress
status: publish
type: post
published: true
meta:
  _edit_last: '1'
  dsq_thread_id: '2084695535'
author:
  login: admin
  email: suminb@gmail.com
  display_name: Sumin
  first_name: Sumin
  last_name: Byeon
redirect_from:
  - /post/1920
---
Problem
-------

When the WordPress Markdown plugin and the Mathjax plugin are activated simultaneously, the Markdown plugin replaces `\\` to `\` and it causes a number of issues when the Mathjax plugin renders LaTeX. For example, a matrix may look like the following

<a href="http://blog.suminb.com/wp-content/uploads/2013/12/mathjax1.png"><img src="http://blog.suminb.com/wp-content/uploads/2013/12/mathjax1.png" alt="mathjax1" width="207" height="42" class="aligncenter size-full wp-image-1922" /></a>

where the intended rendering is as follows

<a href="http://blog.suminb.com/wp-content/uploads/2013/12/mathjax2.png"><img src="http://blog.suminb.com/wp-content/uploads/2013/12/mathjax2.png" alt="mathjax2" width="145" height="77" class="aligncenter size-full wp-image-1923" /></a>

Solution
--------

When writing a LaTeX expression, one may use `\\\\` to compensate the string replacement done by the Markdown plugin. For example, one may write an expression to represent a matrix as follows

    U = \begin{bmatrix}
        x_1 & 1 \\\\
        x_2 & 1
    \end{bmatrix}

Note that `\\\\` is used to denote a new row of the matrix instead of `\\`.

Alternatively, one may alter the PHP implementation of Markdown to disable the string replacement within LaTeX blocks `$$ ... $$`. I decided not to do this because there may be unforeseen side-effects due to this change.

