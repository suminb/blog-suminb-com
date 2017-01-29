---
layout: post
title: JSP 커스텀 태그 사용하기
post_id: '71'
categories:
- Geeky Stuff
tags: []
status: publish
type: post
published: true
meta:
  dsq_thread_id: '287066618'
author:
  login: admin
  email: suminb@gmail.com
  display_name: Sumin
  first_name: Sumin
  last_name: Byeon
redirect_from:
  - /archives/71/
redirect_to:
  - http://philosophical.one/post/jsp-custom-tag
---
###### /WEB-INF/tlds/iterator.tld

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE taglib PUBLIC
		"-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.1//EN"
		"http://java.sun.com/j2ee/dtds/web-jsptaglibrary_1_1.dtd">
	<taglib>
		<tlibversion>1.0</tlibversion>
		<jspversion>1.1</jspversion>
		<shortname>Sun Microsystems Press Tag Library</shortname>
		<info>This tag library has a single counter tag</info>

		<tag>
			<name>iterate</name>
			<tagclass>tags.IteratorTag</tagclass>
			<teiclass>tags.IteratorTagInfo</teiclass>
			<bodycontent>tagdependent</bodycontent>
			<attribute>
				<name>id</name>
				<required>true</required>
				<rtexprvalue>true</rtexprvalue>
			</attribute>
			<attribute>
				<name>collection</name>
				<required>true</required>
				<rtexprvalue>true</rtexprvalue>
			</attribute>
		</tag>
	</taglib>

###### tags/IteratorTag.java

	package tags;

	import java.util.Collection;
	import java.util.Iterator;

	import javax.servlet.jsp.JspWriter;
	import javax.servlet.jsp.JspException;
	import javax.servlet.jsp.tagext.BodyTagSupport;

	public class IteratorTag extends BodyTagSupport
	{
		private Collection collection;
		private Iterator iterator;

		public IteratorTag()
		{
		}

		public void setCollection(Collection collection)
		{
			this.collection = collection;
		}

		public int doStartTag() throws JspException
		{
			if(collection.size() > 0 )
			{
				return EVAL_BODY_TAG;
			}
			else
				return SKIP_BODY;
		}

		public void doInitBody() throws JspException
		{
			iterator = collection.iterator();
			pageContext.setAttribute("item", iterator.next());
		}

		public int doAfterBody() throws JspException
		{
			if(iterator.hasNext())
			{
				pageContext.setAttribute("item", iterator.next());
				return EVAL_BODY_TAG;
			}
			else
			{
				try
				{
					getBodyContent().writeOut(getPreviousOut());
				}
				catch(java.io.IOException e)
				{
					throw new JspException(e.getMessage());
				}

				return SKIP_BODY;
			}
		}

	//	public int doEndTag() throws JspException
	//	{
	//	}

	}

###### index.jsp

	...
	<body>
	<%
	Vector v = new Vector();
	v.addElement("qwer");
	v.addElement("asdf");
	%>

	<iterator:iterate id="item" collection="<%=v%>">
		<%=item%><br/>
	</iterator:iterate>

	</body>
	...

