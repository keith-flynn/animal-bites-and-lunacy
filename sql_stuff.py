import sqlite3
import pandas as pd
import sqlalchemy

# dates 2009-10-28 - 2017-09-08
start_date = '2009-10-28'
end_date = '2017-09-08'

con = sqlite3.connect("lunacy.db")

bite_df = pd.read_sql("SELECT * FROM bites b WHERE b.bite_date BETWEEN '2009-10-29' and '2017-09-08' ORDER BY bite_date;", con, parse_dates='bite_date')

print(bite_df)

moon_df = pd.read_sql("SELECT * FROM moon m WHERE m.date BETWEEN '2009-10-29' and '2017-09-08' ORDER BY date;", con, parse_dates='date')

print(moon_df)

con.close()
