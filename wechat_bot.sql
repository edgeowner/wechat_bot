/*
 Navicat Premium Data Transfer

 Source Server         : wechat_bot
 Source Server Type    : MySQL
 Source Server Version : 50724
 Source Host           : localhost:3306
 Source Schema         : wechat_bot

 Target Server Type    : MySQL
 Target Server Version : 50724
 File Encoding         : 65001

 Date: 29/12/2018 16:28:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for group_member
-- ----------------------------
DROP TABLE IF EXISTS `group_member`;
CREATE TABLE `group_member` (
  `id` bigint(18) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '群成员名称',
  `group_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '群组名称',
  `sender_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '发送者唯一标识',
  `sex` tinyint(1) DEFAULT NULL COMMENT '性别  1:M 2:F',
  `head_url` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '头像链接',
  `signature` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '个人签名',
  `province` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '省份',
  `city` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '城市',
  `py_quan_pin` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '群昵称全拼',
  `py_initial` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '群昵称大写',
  `is_delete` tinyint(1) DEFAULT NULL COMMENT '是否删除 0:未删除，1：删除',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `id` bigint(18) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `sender_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '该条消息发送者唯一标识',
  `sender_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '发送者微信群名称',
  `sender_img` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '发送者头像链接',
  `group_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '群名称',
  `type` int(4) NOT NULL COMMENT '消息类型: 0:文本，1:图片',
  `text` text COLLATE utf8mb4_unicode_ci COMMENT '发送消息内容',
  `url` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '发送消息若为文件，存入文件的url',
  `msg_id` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '微信消息的唯一标识',
  `rebot_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '爬取的机器人账号',
  `send_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '发送消息的时间',
  `is_delete` tinyint(1) DEFAULT NULL COMMENT '是否删除：0:未删除 ，1:删除',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Table structure for msg_distinct_text
-- ----------------------------
DROP TABLE IF EXISTS `msg_distinct_text`;
CREATE TABLE `msg_distinct_text` (
  `id` bigint(18) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `message_id` bigint(18) NOT NULL COMMENT '镜像聊天ID',
  `sender_id` bigint(18) NOT NULL COMMENT '镜像聊天ID',
  `sender_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '微信账号',
  `text` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '群发消息',
  `group` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '微信群名称',
  `is_delete` tinyint(1) DEFAULT NULL COMMENT '是否删除 0 未删除 1 删除',
  `can_use` int(2) DEFAULT NULL COMMENT '标注是否有用  0:未处理  1:能使用  2:不能用  ',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '添加时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Table structure for sender
-- ----------------------------
DROP TABLE IF EXISTS `sender`;
CREATE TABLE `sender` (
  `id` bigint(18) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '发送者名称',
  `sender_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '发送者唯一标识',
  `head_url` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '发送者头像url',
  `sex` tinyint(1) NOT NULL COMMENT '发送者性别',
  `province` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '发送者省份',
  `city` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '发送者城市',
  `signature` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '发送者签名',
  `phones` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '发送者电话（多个 以'',''隔开）',
  `is_delete` tinyint(255) DEFAULT NULL COMMENT '是否删除：0:未删除 ，1:删除',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '入库时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


SET FOREIGN_KEY_CHECKS = 1;
