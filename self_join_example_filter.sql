# This self-join reduces the set of all parcelids to only the latest transaction for each parcelid

# Selects only the latest transaction date for all properties
# Selects all columns from predictions and properties

use zillow;

select e.*, *
from 
(select max(transactiondate), parcelid
    from predictions_2017 
    group by parcelid) as e
join predictions_2017  # Gets the rest of the columns to join onto that subset
on predictions_2017.transactiondate = e.transactiondate and predictions_2017.parcelid = e.parcelid
