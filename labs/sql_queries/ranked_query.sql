--Napisz zapytanie SQL, które z nowo utworzonej tabeli pobierze najwyższe
--wartości zleceń (BUY / SELL) w przedziałach godzinowych per symbol .
--Posortuj wyniki od najstarszych przedziałów do najnowszych.
--Dodaj rowniez rzeczywisty czas transakcji z pola transaction_ts

with ranked_orders as (
    select
        transaction_ts,
        symbol,
        price,
        amount,
        dollar_amount,
        type,
        trans_id,
        year,
        month,
        day,
        hour,
        row_number() over (
            partition by 
                symbol, 
                type,
                date_format(from_unixtime(transaction_ts),'%Y-%m-%dT%H') --HourlyBucket
                
            order by dollar_amount desc
        ) as rn
    from crawler_stockdata
    where type in ('buy', 'sell')
)
select
    date_format(from_unixtime(transaction_ts),'%Y-%m-%dT%H') as HourlyBucket,
    transaction_ts,
    symbol,
    price,
    amount,
    dollar_amount,
    type,
    trans_id,
    year,
    month,
    day,
    hour
from ranked_orders
where rn = 1
order by
    date_format(from_unixtime(transaction_ts),'%Y-%m-%dT%H'), -- HourlyBucket
    symbol,
    type;

