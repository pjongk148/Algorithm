-- 코드를 입력하세요
SELECT f.flavor from first_half as f
    inner join icecream_info as i on f.flavor = i.flavor
    where INGREDIENT_TYPE = "fruit_based"
    and total_order > 3000
    group by f.flavor
    
    
    
    