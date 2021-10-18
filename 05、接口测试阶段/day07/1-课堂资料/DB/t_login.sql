/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : books

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2020-07-26 20:23:19
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_login
-- ----------------------------
DROP TABLE IF EXISTS `t_login`;
CREATE TABLE `t_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `case_desc` varchar(100) NOT NULL COMMENT '用例描述',
  `username` varchar(11) NOT NULL COMMENT '用户名',
  `password` varchar(16) NOT NULL COMMENT '密码',
  `verify_code` varchar(4) NOT NULL COMMENT '验证码',
  `status_code` int(3) NOT NULL DEFAULT '0' COMMENT '响应状态码',
  `content_type` varchar(11) NOT NULL COMMENT 'Content-Type',
  `status` int(1) NOT NULL DEFAULT '0' COMMENT '业务状态码',
  `msg` varchar(100) NOT NULL COMMENT '业务状态消息',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='TPshopLogin参数化';

-- ----------------------------
-- Records of t_login
-- ----------------------------
INSERT INTO `t_login` VALUES ('1', 'case01登录成功', '13488888888', '123456', '8888', '200', 'image', '1', '登陆成功');
INSERT INTO `t_login` VALUES ('2', 'case02账号不存在', '13488888899', '123456', '8888', '200', 'image', '-1', '账号不存在');
INSERT INTO `t_login` VALUES ('3', 'case03密码错误', '13488888888', 'error', '8888', '200', 'image', '-2', '密码错误');
