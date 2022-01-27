# Screenshots
## Requirement 3: SQL CRUD
1. 使用 INSERT 指令新增一筆資料到 member 資料表中,這筆資料的 username 和
password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
###### 指令
```
mysql> INSERT INTO `member`
    -> (id,name,username,password,follower_count)
    -> VALUES
    -> (1,"test1","test","test",0);

mysql> INSERT INTO `member`
    -> (name,username,password,follower_count)
    -> VALUES
    -> ("ponpon","pon123","pon123",100000),
    -> ("chichi","chi123","chi123",300),
    -> ("wu","wu123","wu123",8500),
    -> ("yuyu","yu123","yu123",200);
```
2. 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
###### 指令
```
mysql> SELECT * FROM `member`;
```
###### 執行畫面
![image](https://github.com/chiachil/wehelp-assignments/blob/master/week-5/screenshots/screenshots-1.png)
3. 使用 SELECT 指令取得所有在 member 資料表中的會員資料,並按照 time 欄位,由
近到遠排序。
###### 指令
```
mysql> SELECT * FROM `member`
    -> ORDER BY `time` DESC;
```
###### 執行畫面
![image](https://github.com/chiachil/wehelp-assignments/blob/master/week-5/screenshots/screenshots-2.png)
4. 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料,並按照 time 欄位,
由近到遠排序。( 並非編號 2、3、4 的資料,而是排序後的第 2 ~ 4 筆資料 )
###### 指令
```
mysql> SELECT * FROM `member`
    -> ORDER BY `time` DESC
    -> LIMIT 1,3;
```
###### 執行畫面
![image](https://github.com/chiachil/wehelp-assignments/blob/master/week-5/screenshots/screenshots-3.png)
5. 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
###### 指令
```
mysql> SELECT * FROM `member`
    -> WHERE `username` = "test";
```
###### 執行畫面
![image](https://github.com/chiachil/wehelp-assignments/blob/master/week-5/screenshots/screenshots-4.png)
6. 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
###### 指令
```
mysql> SELECT * FROM `member`
    -> WHERE `username` = "test" AND `password` = "test";
```
###### 執行畫面
![image](https://github.com/chiachil/wehelp-assignments/blob/master/week-5/screenshots/screenshots-5.png)
7. 使用 UPDATE 指令更新欄位 username 是 test 的會員資料,將資料中的 name 欄位
改成 test2。
###### 指令
```
mysql> UPDATE `member`
    -> SET `name` = "test2"
    -> WHERE `username` = "test";

mysql> SELECT * FROM `member`;
```
###### 執行畫面
![image](https://github.com/chiachil/wehelp-assignments/blob/master/week-5/screenshots/screenshots-6.png)

## Requirement 4: SQL Aggregate Functions
1. 取得 member 資料表中,總共有幾筆資料 ( 幾位會員 )。
###### 指令
```
mysql> SELECT COUNT(*) FROM `member`;
```
###### 執行畫面
![image](https://github.com/chiachil/wehelp-assignments/blob/master/week-5/screenshots/screenshots-7.png)</br>
2. 取得 member 資料表中,所有會員 follower_count 欄位的總和。
###### 指令
```
mysql> SELECT SUM(`follower_count`) FROM `member`;
```
###### 執行畫面
![image](https://github.com/chiachil/wehelp-assignments/blob/master/week-5/screenshots/screenshots-8.png)</br>
3. 取得 member 資料表中,所有會員 follower_count 欄位的平均數。
###### 指令
```
mysql> SELECT AVG(`follower_count`) FROM `member`;
```
###### 執行畫面
![image](https://github.com/chiachil/wehelp-assignments/blob/master/week-5/screenshots/screenshots-9.png)

## Requirement 5: SQL JOIN (Optional)
1. 在資料庫中,建立新資料表,取名字為 message。資料表中必須包含以下欄位設定:
###### 指令
```
mysql> CREATE TABLE `message`(
    -> `id` BIGINT PRIMARY KEY AUTO_INCREMENT,
    -> `member_id` BIGINT NOT NULL,
    -> `content` VARCHAR(225) NOT NULL,
    -> `time` DATETIME NOT NULL DEFAULT NOW());

mysql> ALTER TABLE `message`
    -> ADD FOREIGN KEY(`member_id`)
    -> REFERENCES `member`(`id`)
    -> ON DELETE CASCADE ON UPDATE CASCADE;

mysql> DESCRIBE `message`;
```
###### 執行畫面
![image](https://github.com/chiachil/wehelp-assignments/blob/master/week-5/screenshots/screenshots-10.png)
---
1.1 要求外：新增資料表資料
###### 指令
```
mysql> INSERT INTO `message`
    -> (member_id,content)
    -> VALUES
    -> (1,"hi"),
    -> (1,"how are you?"),
    -> (2,"olala"),
    -> (4,"this is a message..."),
    -> (5,"this is another message..");

mysql> SELECT * FROM `message`;
```
###### 執行畫面
![image](https://github.com/chiachil/wehelp-assignments/blob/master/week-5/screenshots/screenshots-11.png)
---
2. 使用 SELECT 搭配 JOIN 語法,取得所有留言,結果須包含留言者會員的姓名。
###### 指令
```
mysql> SELECT `message`.*,`member`.`name` FROM `message`
    -> LEFT JOIN `member`
    -> ON `message`.`member_id` = `member`.`id`;
```
###### 執行畫面
![image](https://github.com/chiachil/wehelp-assignments/blob/master/week-5/screenshots/screenshots-12.png)
3. 使用 SELECT 搭配 JOIN 語法,取得 member 資料表中欄位 username 是 test 的所有
留言,資料中須包含留言者會員的姓名。
###### 指令
```
mysql> SELECT `member`.`name`,`message`.* FROM `member`
    -> JOIN `message`
    -> ON `member`.`id` = `message`.`member_id`
    -> WHERE `member`.`username` = "test";
```
###### 執行畫面
![image](https://github.com/chiachil/wehelp-assignments/blob/master/week-5/screenshots/screenshots-13.png)