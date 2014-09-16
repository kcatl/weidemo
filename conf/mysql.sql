#create database weibo
create database weibo;
use weibo;

#create table userinfo

create table userinfo( id bigint primary key auto_increment,
	username varchar(50) null,
	province smallint null,
	city smallint null, 
	location varchar(200) null,
	description varchar(200) null, 

	profile_image_url varchar(200) null,

	gender varchar(5) null, followers_count bigint null,
	friends_count bigint null,
	statuses_count bigint null, favourites_count bigint null,
	created_at varchar(100) null, 
	geo_enabled varchar(5) null, verified varchar(5) null, 
	verified_reason varchar(200) null,
	url varchar(200) null,
	reqtime timestamp,userid bigint null
	);


#create table userdata

create table userdata(
	userid bigint null,
	year int null,
	month int null,
	hour int null,
	datanum bigint unique key auto_increment
);