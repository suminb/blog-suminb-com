---
layout: post
title: SelectQuery
post_id: '378'
categories:
- Software Engineering
tags: []
status: publish
type: post
published: true
meta:
  dsq_thread_id: '287065171'
  _edit_last: '1'
author:
  login: admin
  email: suminb@gmail.com
  display_name: Sumin
  first_name: Sumin
  last_name: Byeon
redirect_from:
  - /archives/378/
---
홍민희군과의 대화 중 아이디어를 얻어 이것을 만들게 되었다.

	SelectQuery query = new SelectQuery();
	query.select("students", "*").where("major = 'CS'").orderBy("gpa DESC, name ASC").limit(15);

	System.out.println(query);

결과는

	SELECT * FROM students WHERE major = 'CS' ORDER BY gpa DESC, name ASC LIMIT 15

프로그램 코드가 SQL 문과 비슷하다는 점이 장점이 될 수도 있겠지만 자칫 코드가 보기 흉하게 길어질 수도 있으므로 다음과 같은 방법을 병행할 수 있도록 만들었다.

	SelectQuery query = new SelectQuery();
	query.select("students", "name, age, major");
	query.where("major = 'CS' AND minor = 'MATH'");
	query.orderBy("gpa DESC");
	query.limit(10, 15);

	System.out.println(query);

결과는

	SELECT name, age, major FROM students WHERE major = 'CS' AND minor = 'MATH' ORDER BY gpa DESC LIMIT 10, 15

SQL 을 수행하려면 `execute()` 메소드를 호출하면 된다.

	query.select("students", "*").where("major = 'CS'").execute();

또는

	query.select("students", "*");
	query.where("major = 'CS'");
	query.execute();

`execute()` 메소드는 `java.sql.ResultSet` 의 인스턴스를 반환한다.

사용할 수 있는 메소드는 다음과 같다.

	select(String table, String select)
	where(String where)
	orderBy(String orderBy)
	limit(int limit)
	limit(int start, int limit)
	groupBy(String groupBy)
	having(String having)
	execute()
	toString()

아쉽게도 아직은 JOIN 관련 메소드를 지원하지 않는다. 억지로 끼워넣어서 쓸 수는 있겠지만 별로 권장하고 싶은 방법은 아니다. '예외처리를 어떻게 할 것인가'에 대해서 조금 더 생각해보고 JOIN 관련 메소드를 만들 예정이다.

<!-- 자바, db, database, query -->

