---
layout: post
title: LCS(Longest Common Subsequence) 찾기
post_id: '614'
categories:
- Computer Science
tags: []
status: publish
type: post
published: true
meta:
  _edit_last: '1'
  dsq_thread_id: '287066168'
author:
  login: admin
  email: suminb@gmail.com
  display_name: Sumin
  first_name: Sumin
  last_name: Byeon
redirect_from:
  - /archives/614/
---
오... 완전 신기>_ <

	LCS(X, Y)
		for(i=1; i<=m; i++) L[i, 0] = 0
		for(j=0; j<=n; j++) L[0, j] = 0
		for(i=1; i<=m; i++)
			for(j=1; j<=n; j++)
				if(x[i] == y[j])
					L[i, j] = 1 + L[i-1, j-1]
				else if(L[i-1, j] >= L[i, j-1])
					L[i, j] = L[i-1, j]
				else
					L[i, j] = L[i, j-1]

