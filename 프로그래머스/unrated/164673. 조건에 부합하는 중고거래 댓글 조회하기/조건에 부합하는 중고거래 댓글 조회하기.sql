-- 코드를 입력하세요
SELECT  b.title as TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, date_format(r.created_date,"%Y-%m-%d") as CREATED_DATE
    from used_goods_board as b
    join used_goods_reply as r ON B.BOARD_ID = R.BOARD_ID
    where b.created_date between '2022-10-01' and '2022-10-31'
    order by r.created_date, b.title