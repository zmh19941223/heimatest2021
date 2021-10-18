# Day01每日作业

##### 一、基础题

1，请简述接口的概念？

答案：

```text

```

2，按照范围划分，接口可以分为哪两种类型？

```text

```

3，请简述接口测试的概念

答案：

```text

```

4，请简述接口测试的原理。

答案：

```text

```

5，为什么要进行接口测试？（特点）

答案：

```text

```

6，我们可以使用哪些方式来实现接口测试？

答案：

```text

```

7，简答题：什么是自动化接口测试？

答案：

```text

```

8，简答题：是什么是HTTP协议，他们由哪些部分组成，分别在原始数据包的什么位置？

答案：

```text

```

9，请写出HTTP协议的5个特点

答案：

```text

```

10，请问URL是什么？

答案：

```text

```

11，请根据以下三个URL，写出他们的端口号：

http://www.baidu.com
https://www.baidu.com

http://localhost:8000

```text

```

12，填空题：请根据URL写出每个部分的内容：<http://www.itcast.cn/subject/pythonzly/index.shtml?a=1&b=2>

答案：

```text

```

13，常见协议有哪些？

答：

```text

```

14，有一个只有请求路径和请求参数的字符串，请问这个字符串按照URL来进行解析时，有哪些请求参数，请求参数之间用什么符号隔开的？

/seeyon/meeting.do?method=create&listMethod=listMyMeeting

答案：

```text

```

15，以下关于HTTP请求的描述，错误的是？

A：HTTP请求包括了请求行，请求头，请求体

B：HTTP请求行包括协议/版本，URL，请求方法

C：HTTP请求头用于描述客户端信息

D：HTTP请求头中Content-Type用于描述客户端浏览器类型

E：HTTP请求中，只有Post请求才有请求体。

F：HTTP请求中，按照标准规范，请求的数据类型是由Content-Type来进行标志的。

答案

```text

```

16，在HTTP请求中，有哪些常用的请求方法？

答案：

```text

```

17，HTTP响应主要包括哪几个部分？

答案：

```text

```

18，HTTP相应中，关于状态码的描述，正确的是：

A：1xx表示是指示信息，说明请求已接收，在继续处理

B：2xx表示请求已经被成功接收和处理

C：3xx表示请求资源需要重定向到另外一个资源地址

D：4xx表示客户端有错误

E：5xx表示服务端有错误

答案：

```text

```

19，请简述Restful。

答案：

```text

```

20，请简述接口测试流程。

答案：

```text

```

21，有如下接口文档，请选出其中描述错误的选项

| 接口名称 | 用户资料查询接口                               |
| -------- | :--------------------------------------------- |
| 接口路径 | /api/sys/profile                               |
| 接口域名 | 182.92.81.159                                  |
| 请求头   | {"Authorization":"Bearer xxxx-xxxx-xxxx-xxxx"} |
| 请求方法 | POST                                           |
| 返回数据 | 见下图json代码模块                             |

```json
{
	"success": true,
	"code": 10000,
	"message": "操作成功！",
	"data": {
		"userId": "1063705989926227968",
		"mobile": "13800000002",
		"username": "aj123",
		"company": "传智播客",
		"companyId": "1",
		"roles": {
			"apis": [
				"API-USER-DELETE"
			],
			"menus": [
				"settings",
				"departments",
				"test",
				"employees",
				"permissions"
			],
			"points": [
				"point-user-delete",
				"POINT-USER-UPDATE",
				"POINT-USER-ADD"
			]
		},
		"authCacheKey": null
	}
}
```



A：根据文档描述，这个接口的请求方法是Post，请求路径是/api/sys/login，请求域名是182.92.81.159。

B：这个接口的名称是用户资料查询接口

C：这个接口的请求头中是{"Authorization":"Bearer xxxx-xxxx-xxxx"}

D：如果要测试这个接口是否准确，仅对响应数据进行断言还不够，还需要对比数据库中的数据。

答案：

```text

```



