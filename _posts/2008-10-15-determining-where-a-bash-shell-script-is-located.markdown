---
layout: post
title: Determining Where a Bash Shell Script Is Located
post_id: '701'
categories:
- Geeky Stuff
tags: []
status: publish
type: post
published: true
meta:
  _edit_last: '1'
  dsq_thread_id: '287065557'
author:
  login: admin
  email: suminb@gmail.com
  display_name: Sumin
  first_name: Sumin
  last_name: Byeon
redirect_from:
  - /post/701
---
I just figured this out today.

<pre><code>
#!/bin/bash
echo $(dirname $PWD/$0)
</code></pre>
