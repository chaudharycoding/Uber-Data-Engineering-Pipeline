CREATE OR REPLACE TABLE `uber-project-438005.uber_data_zaeem.tbl_analytics` AS (
SELECT 
    f.trip_id,
    f.VendorID,
    f.datetime_id,
    f.passenger_count_id,
    f.trip_distance_id,
    f.rate_code_id,
    f.pickup_location_id,
    f.dropoff_location_id,
    f.payment_type_id,
    f.fare_amount,
    f.extra,
    f.mta_tax,
    f.tip_amount,
    f.tolls_amount,
    f.improvement_surcharge,
    f.total_amount,
    
    -- Additional analytics
    COUNT(*) OVER() AS total_trip_count,  -- Total number of trips
    AVG(f.fare_amount) OVER() AS avg_fare_amount,  -- Average fare amount
    SUM(f.tip_amount) OVER() AS total_tips,  -- Total tips given
    SUM(f.trip_distance_id) OVER() AS total_distance_traveled  -- Total distance traveled
FROM 
    `uber-project-438005.uber_data_zaeem.fact_table` f
);

