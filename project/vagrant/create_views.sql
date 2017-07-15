create view aggregated_error_logs AS (select time::date as date, count(*) as count
from log
where status != '200 OK'
group by time::date);

create view aggregated_all_logs AS (select time::date as date, count(*) as count
from log
group by time::date);