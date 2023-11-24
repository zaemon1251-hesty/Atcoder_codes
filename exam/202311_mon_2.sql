-- hotels, rooms
-- prepare
DROP TABLE IF EXISTS hotels;
DROP TABLE IF EXISTS rooms;

-- 宿泊施設情報を格納するテーブル
CREATE TABLE hotels (
  id integer PRIMARY KEY AUTOINCREMENT, -- 宿泊施設ID
  name varchar NOT NULL, -- 宿泊施設名
  breakfast varchar NOT NULL, -- 朝食の種類 （"none","continental","american","english","washoku","buffet"）
  large_public_bath boolean NOT NULL, -- 大浴場の有無 (1:有り 0:無し) ※これ以外の値は取らない
  prefecture varchar NOT NULL, -- 都道府県
  city varchar NOT NULL -- 市区町村
);

-- 客室情報を格納するテーブル
CREATE TABLE rooms (
  id integer PRIMARY KEY AUTOINCREMENT, -- 客室ID
  hotel_id integer NOT NULL, -- 宿泊施設ID
  name varchar NOT NULL, -- 客室名
  num integer NOT NULL, -- 客室数
  price integer NOT NULL, -- 一泊料金（円）
  space decimal NOT NULL, -- 床面積（平方メートル）
  bed varchar NOT NULL, -- ベッドの規格（single,semi-double,double,semi-queen,queen,semi-king,king,...）
  non_smoking boolean NOT NULL, -- 禁煙ルームか否か（1:禁煙 0:喫煙可）※これ以外の値は取らない
  ladies boolean NOT NULL, -- 女性専用か否か（1:女性専用 0:男女共用）※これ以外の値は取らない
  wifi boolean NOT NULL, -- 無料Wi-Fiの提供の有無（1:有り 0:無し）※これ以外の値は取らない
  FOREIGN KEY(hotel_id) REFERENCES hotels(id)
);

-- step1. 宿泊施設の追加。
INSERT INTO hotels (name, breakfast, large_public_bath, prefecture, city) VALUES
  ('ホテル ウエスト横浜', 'washoku', 1, '神奈川県', '横浜市');

-- step2. 禁煙ルームの客室の一泊料金を100円引きにする。
UPDATE rooms SET price = price - 100 WHERE non_smoking = 1;

-- step3. ベッドの規格が　single semi-double double　以外の客室を削除する
DELETE FROM rooms WHERE bed NOT IN ('single', 'semi-double', 'double');

-- step4. 宿泊施設が存在する都道府県・市区町村の一覧を作成する
SELECT DISTINCT prefecture, city FROM hotels;

-- step5. 宿泊施設名に「温泉」を含む宿泊施設の一覧を作成する
SELECT DISTINCT * FROM hotels WHERE name LIKE '%温泉%';

-- step6. 神奈川県 相模原市の宿泊施設の全客室を、1泊料金の安い順, 床面積の広い順にソートして、 id name price space を表示する
WITH hotels_in_sagamihara AS (
  SELECT id FROM hotels WHERE prefecture = '神奈川県' AND city = '相模原市'
)
SELECT id, name, price, space FROM rooms 
  WHERE hotel_id IN (SELECT id FROM hotels_in_sagamihara)
  ORDER BY price ASC, space DESC;


-- step7. 客室数の合計が「20以上30以下」である宿泊施設の宿泊施設IDを全件取得する
SELECT hotel_id AS id, SUM(num) AS number_of_rooms FROM rooms 
  GROUP BY hotel_id 
  HAVING SUM(num) BETWEEN 20 AND 30;

-- step 8 女性専用の客室しか登録されていない宿泊施設を取得する
WITH ladies_aware_hotel AS (
  SELECT hotel_id FROM rooms 
    GROUP BY hotel_id 
    HAVING SUM(ladies) = COUNT(*)
)
SELECT * FROM ladies_aware_hotel;

-- step9 客室屋の情報に対して同じ宿泊施設の最安値を添えて取得する id name price lowest_price
WITH hotel_min_price AS (
  SELECT hotel_id, MIN(price) AS lowest_price FROM rooms GROUP BY hotel_id
)
SELECT id, name, price, lowest_price FROM rooms 
  INNER JOIN hotel_min_price ON rooms.hotel_id = hotel_min_price.hotel_id;