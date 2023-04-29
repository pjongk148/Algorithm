-- 코드를 입력하세요
SELECT factory_id,factory_name, address FROM FOOD_FACTORY
    WHERE ADDRESS LIKE "강원도%"
        ORDER BY FACTORY_ID