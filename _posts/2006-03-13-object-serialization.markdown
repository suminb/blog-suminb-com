---
layout: post
title: Object Serialization
post_id: '136'
categories:
- Geeky Stuff
tags:
- Java
status: publish
type: post
published: true
meta:
  _edit_last: '1'
  dsq_thread_id: '287065984'
author:
  login: admin
  email: suminb@gmail.com
  display_name: Sumin
  first_name: Sumin
  last_name: Byeon
redirect_from:
  - /archives/136/
redirect_to:
  - http://philosophical.one/post/object-serialization
---
Source Code
-----------

	import java.io.FileInputStream;
	import java.io.FileOutputStream;
	import java.io.ObjectInput;
	import java.io.ObjectInputStream;
	import java.io.ObjectOutput;
	import java.io.ObjectOutputStream;
	import java.util.Date;

	public class Test
	{
		public static void main(String[] args) {

			try {
				FileOutputStream fos = new FileOutputStream("object");
				ObjectOutput oo = new ObjectOutputStream(fos);

				oo.writeDouble(12.128);
				oo.writeObject("Today");
				oo.writeObject(new Date());
				oo.flush();
				oo.close();

				fos.flush();
				fos.close();

				FileInputStream fis = new FileInputStream("object");
				ObjectInput oi = new ObjectInputStream(fis);

				double d = oi.readDouble();
				String str = (String)oi.readObject();
				Date date = (Date)oi.readObject();

				fis.close();
				oi.close();

				System.out.println(d);
				System.out.println(str);
				System.out.println(date.toString());
			}
			catch (Exception e) {
				e.printStackTrace();
			}
		}
	}

References
----------

* [http://java.sun.com/j2se/1.3/docs/guide/serialization/spec/serial-arch.doc2.html](http://java.sun.com/j2se/1.3/docs/guide/serialization/spec/serial-arch.doc2.html)

<!-- (keyword:) 객체 직렬화 -->

