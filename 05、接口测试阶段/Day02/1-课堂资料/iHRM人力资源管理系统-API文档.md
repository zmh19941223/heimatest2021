# IHRM人力资源管理系统接口文档

# 系统信息
- 系统路径：http://ihrm-test.itheima.net



# 1.框架

## 城市列表
### 基本信息

- Path：/api/sys/city

- Method： GET

- 接口描述：


### 请求参数

### 返回数据

- 操作成功响应状态码：200
- 错误码描述：
  - 10000：操作成功！
  - 99999：抱歉，系统繁忙，请稍后重试！

名称|类型|是否必须|默认值|备注
-|-|-
success|bool|是||操作成功标记
code|int|是|10000|错误码
message|String|是|操作成功！|消息
data|object[]|是||
├─id|string|是||城市id
├─name|string|是||城市名称



## 登录

### 基本信息

- Path： /api/sys/login

- Method： POST

- 接口描述：


### 请求参数
**Headers**

| 参数名称  | 参数值  |  是否必须 | 示例  | 备注  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Content-Type  |  application/json | 是  |   |   |
**Body**

| 名称     | 类型   | 是否必须 | 默认值 | 备注   | 其他信息 |
| -------- | ------ | -------- | ------ | ------ | -------- |
| mobile   | string | 必须     |        | 手机号 |          |
| password | string | 必须     |        | 密码   |          |

### 返回数据

- 操作成功响应状态码：200
- 错误码描述：
  - 10000：操作成功！
  - 20001：用户名或密码错误
  - 99999：抱歉，系统繁忙，请稍后重试！
  

名称|类型|是否必须|默认值|备注
-|-|-
success|bool|是||操作成功标记
code|int|是|10000|错误码
message|string|是|操作成功！|消息
data|string|是||令牌（token）

```json
{"success":true,"code":10000,"message":"操作成功！","data":"xxx"}
```
```json
{"success":false,"code":20001,"message":"用户名或密码错误","data":null}
```
```json
{"success":false,"code":99999,"message":"抱歉，系统繁忙，请稍后重试！","data":null}
```


## 用户资料

### 基本信息

- Path： /api/sys/profile

- Method： POST

- 接口描述：


### 请求参数
**Headers**

| 参数名称  | 参数值  |  是否必须 | 示例  | 备注  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Authorization  |  TOKEN | 是  |  Bearer 35581cc8-adce-4a32-9ca6-13e82ead121c |  用户令牌 |

### 返回数据

- 操作成功响应状态码：200
- 错误码描述：
  - 10000：操作成功！
  - 99999：抱歉，系统繁忙，请稍后重试！

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
            // 菜单
            "menus": [
                "settings",
                "departments",
                "test",
                "employees",
                "permissions"
            ],
            // 权限点
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



# 2.组织架构

## 组织架构列表
### 基本信息

- Path： /api/company/department

- Method： GET

- 接口描述：


### 请求参数
**Headers**

| 参数名称  | 参数值  |  是否必须 | 示例  | 备注  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Authorization  |  TOKEN | 是  |  Bearer 35581cc8-adce-4a32-9ca6-13e82ead121c |  用户令牌 |

### 返回数据

- 操作成功响应状态码：200
- 错误码描述：
  - 10000：操作成功！
  - 99999：抱歉，系统繁忙，请稍后重试！

```json
{
    "success": true,
    "code": 10000,
    "message": "操作成功！",
    "data": {
        "companyId": "1",
        "companyName": "江苏传智播客教育科技股份有限公司",
        "companyManage": "张三",
        "depts": [
            {
                "id": "1063678149528784896",
                "pid": "1063676045212913664",
                "companyId": "1",
                "name": "测试部",
                "code": "DEPT-TEST",
                "managerId": null,
                "manager": "测试部门领导",
                "introduce": "所有测试人员统一划分到测试部",
                "createTime": "2018-11-17T06:20:07.000+0000"
            },
            {
                "id": "1066239766607040512",
                "pid": null,
                "companyId": "1",
                "name": "行政中心",
                "code": "DEPT-XZ",
                "managerId": null,
                "manager": "张三",
                "introduce": "包含人力资源和行政部门",
                "createTime": "2018-11-24T07:59:04.000+0000"
            },
            {
                "id": "1066240656856453120",
                "pid": "1063676045212913664",
                "companyId": "1",
                "name": "开发部",
                "code": "DEPT-DEV",
                "managerId": null,
                "manager": "研发",
                "introduce": "全部java开发人员",
                "createTime": "2018-11-24T08:02:37.000+0000"
            },
            {
                "id": "1185411048114860032",
                "pid": "1066240656856453120",
                "companyId": "1",
                "name": "4524",
                "code": "4534",
                "managerId": null,
                "manager": "453",
                "introduce": "45345",
                "createTime": null
            }
        ]
    }
}
```



## 获取部门信息

### 基本信息

- Path： /api/company/department/:id

- Method： GET

- 接口描述：


### 请求参数
**Headers**

| 参数名称  | 参数值  |  是否必须 | 示例  | 备注  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Authorization  |  TOKEN | 是  |  Bearer 35581cc8-adce-4a32-9ca6-13e82ead121c |  用户令牌 |

### 返回数据

- 操作成功响应状态码：200
- 错误码描述：
  - 10000：操作成功！
  - 99999：抱歉，系统繁忙，请稍后重试！

```json
{
    "success": true,
    "code": 10000,
    "message": "操作成功！",
    "data": {
        "id": "1066239766607040512",
        "pid": null,
        "companyId": "1",
        "name": "行政中心",
        "code": "DEPT-XZ",
        "managerId": null,
        "manager": "张三",
        "introduce": "包含人力资源和行政部门",
        "createTime": "2018-11-24T07:59:04.000+0000"
    }
}
```



## 部门添加

### 基本信息

- Path： /api/company/department

- Method： POST

- 接口描述：


### 请求参数
**Headers**

| 参数名称  | 参数值  |  是否必须 | 示例  | 备注  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Content-Type  |  application/json | 是  |   |   |
| Authorization  |  TOKEN | 是  |  Bearer 35581cc8-adce-4a32-9ca6-13e82ead121c |  用户令牌 |

**Body**

| 名称  | 类型  |  是否必须 | 默认值  | 备注  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| name  | string | 必须  |   |  名称 |
| code  | string | 必须  |   |  编号 |
| manager  | string | 非必须  |   |  部门负责人姓名 |
| introduce  | string | 非必须  |   |  部门介绍 |
| pid  | string | 非必须  |   |  父级部门ID，没有为空 |


### 返回数据

- 操作成功响应状态码：200
- 错误码描述：
  - 10000：操作成功！
  - 99999：抱歉，系统繁忙，请稍后重试！

```json
{"success":true,"code":10000,"message":"操作成功！","data":null}
```



## 部门修改

### 基本信息

- Path： /api/company/department/:id

- Method： PUT

- 接口描述：


### 请求参数
**Headers**

| 参数名称  | 参数值  |  是否必须 | 示例  | 备注  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Content-Type  |  application/json | 是  |   |   |
| Authorization  |  TOKEN | 是  |  Bearer 35581cc8-adce-4a32-9ca6-13e82ead121c |  用户令牌 |

**路径参数**
| 参数名称 | 示例  | 备注  |
| ------------ | ------------ | ------------ |
| id |   | 部门id |

**Body**

| 名称  | 类型  |  是否必须 | 示例  | 备注  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| name  | string | 必须  |   |  名称 |
| code  | string | 必须  |   |  编号 |
| manager  | string | 非必须  |   |  部门负责人姓名 |
| introduce  | string | 非必须  |   |  部门介绍 |

### 返回数据

- 操作成功响应状态码：200
- 错误码描述：
  - 10000：操作成功！
  - 99999：抱歉，系统繁忙，请稍后重试！

```json
{"success":true,"code":10000,"message":"操作成功！","data":null}
```



## 删除部门

### 基本信息

- Path： /api/company/department/:id

- Method： DELETE

- 接口描述：


### 请求参数
**Headers**

| 参数名称  | 参数值  |  是否必须 | 示例  | 备注  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Authorization  |  TOKEN | 是  |  Bearer 35581cc8-adce-4a32-9ca6-13e82ead121c |  用户令牌 |

**路径参数**

| 参数名称 | 示例  | 备注  |
| ------------ | ------------ | ------------ |
| id |   | 部门id |

### 返回数据

- 操作成功响应状态码：200
- 错误码描述：
  - 10000：操作成功！
  - 99999：抱歉，系统繁忙，请稍后重试！

```json
{"success":true,"code":10000,"message":"操作成功！","data":null}
```



# 3.员工管理

## 员工管理列表
### 基本信息

- Path： /api/sys/user?page=1&size=10

- Method： GET

- 接口描述：


### 请求参数
**Headers**

| 参数名称  | 参数值  |  是否必须 | 示例  | 备注  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Content-Type  |  application/json | 是  |   |   |
| Authorization  |  TOKEN | 是  |  Bearer 35581cc8-adce-4a32-9ca6-13e82ead121c |  用户令牌 |

**Query**

| 参数名称  |  是否必须 | 示例  | 备注  |
| ------------ | ------------ | ------------ | ------------ |
| page | 是  |   |  当前第几页 |
| size | 是  |   |  每页展示记录数 |


### 返回数据

- 操作成功响应状态码：200
- 错误码描述：
  - 10000：操作成功！
  - 99999：抱歉，系统繁忙，请稍后重试！

```json
{
    "success": true,
    "code": 10000,
    "message": "操作成功！",
    "data": {
        "total": 12283,
        "rows": [
            {
                "id": "1177058847969570816",
                "mobile": "13308087976",
                "username": "jack",
                "password": "43f8027d40bda49adf57b288e9344a89",
                "enableState": 1,
                "createTime": null,
                "companyId": "1",
                "companyName": "传智播客",
                "departmentId": "1066240656856453120",
                "timeOfEntry": "2019-07-01T00:00:00.000+0000",
                "formOfEmployment": 1,
                "workNumber": "1322131",
                "formOfManagement": null,
                "workingCity": null,
                "correctionTime": "2019-11-30",
                "inServiceStatus": null,
                "departmentName": "开发部",
                "level": "user",
                "staffPhoto": null
            },
            {
                "id": "1177058858916704256",
                "mobile": "13488888889",
                "username": "jack11",
                "password": "d8cec60516d464699d217da7ba5b6545",
                "enableState": 1,
                "createTime": null,
                "companyId": "1",
                "companyName": "传智播客",
                "departmentId": "1066240656856453120",
                "timeOfEntry": "2019-07-01T00:00:00.000+0000",
                "formOfEmployment": 1,
                "workNumber": "1322130",
                "formOfManagement": null,
                "workingCity": null,
                "correctionTime": "2019-11-30",
                "inServiceStatus": null,
                "departmentName": "开发部",
                "level": "user",
                "staffPhoto": null
            }
        ]
    }
}
```



## 员工添加

### 基本信息

- Path： /api/sys/user

- Method： POST

- 接口描述：


### 请求参数
**Headers**

| 参数名称  | 参数值  |  是否必须 | 示例  | 备注  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Content-Type  |  application/json | 是  |   |   |
| Authorization  |  TOKEN | 是  |  Bearer f5050a1b-7919-444c-9ec4-3c1a7286536d |  用户令牌 |

**Body**

| 名称  | 类型  |  是否必须 | 示例  | 备注  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| username  | string | 必须  |   |  姓名 |
| mobile  | string | 必须  |   |  手机号 |
| workNumber  | string | 必须  |   |  工号 |
| timeOfEntry  | string | 非必须  |   |  入职时间 |
| formOfEmployment  | string | 非必须  |   |  聘用形式 |
| departmentId  | string | 非必须  |   |  部门id |
| departmentName  | string | 非必须  |   |  部门名称 |
| correctionTime  | string | 非必须  | 2019-11-30  |  转正时间 |


### 返回数据

- 操作成功响应状态码：200
- 错误码描述：
  - 10000：操作成功！
  - 99999：抱歉，系统繁忙，请稍后重试！

```json
{"success":true,"code":10000,"message":"操作成功！", "data":{"id":"113749504"}}
```



## 员工修改

### 基本信息

- Path： /api/sys/user/:target

- Method： PUT

- 接口描述：

### 请求参数

**Headers**

| 参数名称      | 参数值           | 是否必须 | 示例                                        | 备注     |
| ------------- | ---------------- | -------- | ------------------------------------------- | -------- |
| Content-Type  | application/json | 是       |                                             |          |
| Authorization | TOKEN        | 是       | Bearer f5050a1b-7919-444c-9ec4-3c1a7286536d | 用户令牌 |

**Body**

| 名称  | 类型  |  是否必须 | 示例  | 备注  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| username  | string | 非必须  |   |  姓名 |
| password  | string | 非必须  |   |  密码 |
| departmentId  | string | 非必须  |   |  部门ID |
| departmentName  | string | 非必须  |   |  部门名称 |


### 返回数据

- 操作成功响应状态码：200
- 错误码描述：
  - 10000：操作成功！
  - 10003：权限不足
  - 99999：抱歉，系统繁忙，请稍后重试！

```json
{"success":true,"code":10000,"message":"操作成功！", "data":{"id":"113749504"}}
```



## 员工查询

### 基本信息

- Path： /api/sys/user/:target

- Method： GET

- 接口描述：

### 请求参数

**Headers**

| 参数名称      | 参数值           | 是否必须 | 示例                                        | 备注     |
| ------------- | ---------------- | -------- | ------------------------------------------- | -------- |
| Content-Type  | application/json | 是       |                                             |          |
| Authorization | TOKEN        | 是       | Bearer f5050a1b-7919-444c-9ec4-3c1a7286536d | 用户令牌 |



### 返回数据

- 操作成功响应状态码：200
- 错误码描述：
  - 10000：操作成功！
  - 99999：抱歉，系统繁忙，请稍后重试！

```json
{
    "success": true,
    "code": 10000,
    "message": "操作成功！",
    "data": {
        "id": "1148850279369990144",
        "mobile": "13012340007",
        "username": "tom7",
        "password": "9da8512ab685c1c60842b696c2bf6f3f",
        "enableState": 1,
        "createTime": null,
        "companyId": "1",
        "companyName": "传智播客",
        "departmentId": "1066240656856453120",
        "timeOfEntry": "2019-07-01T00:00:00.000+0000",
        "formOfEmployment": 1,
        "workNumber": "1322131",
        "formOfManagement": null,
        "workingCity": null,
        "correctionTime": "2019-07-30T16:00:00.000+0000",
        "inServiceStatus": null,
        "departmentName": "开发部",
        "roleIds": [],
        "staffPhoto": null
    }
}
```



## 员工删除

### 基本信息

- Path： /api/sys/user/:target

- Method： DELETE

- 接口描述：

### 请求参数

**Headers**

| 参数名称      | 参数值           | 是否必须 | 示例                                        | 备注     |
| ------------- | ---------------- | -------- | ------------------------------------------- | -------- |
| Content-Type  | application/json | 是       |                                             |          |
| Authorization | TOKEN            | 是       | Bearer f5050a1b-7919-444c-9ec4-3c1a7286536d | 用户令牌 |



### 返回数据

- 操作成功响应状态码：200
- 错误码描述：
  - 10000：操作成功！
  - 10003：权限不足
  - 99999：抱歉，系统繁忙，请稍后重试！

```json
{"success":true,"code":10000,"message":"操作成功！","data":null}
```



​       Vv m   bbn  cbvb         nbvvvvvvvfntggggnbfvggggbnv   **vv**
