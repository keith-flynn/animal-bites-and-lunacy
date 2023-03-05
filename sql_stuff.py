import sqlite3
import pandas as pd

con = sqlite3.connect("lunacy.db")

bite_df = pd.read_sql("""SELECT 
                            bite_date, 
                            SpeciesIDDesc, 
                            BreedIDDesc, 
                            GenderIDDesc, 
                            color, 
                            victim_zip, 
                            WhereBittenIDDesc, 
                            ResultsIDDesc 
                        FROM 
                            bites b 
                        WHERE 
                            b.bite_date 
                        BETWEEN 
                            '2009-10-29' and '2017-09-08' 
                        ORDER BY 
                            bite_date;""", con)

print(bite_df)

moon_df = pd.read_sql("""SELECT 
                            date, 
                            illum_pct, 
                            phase 
                        FROM 
                            moon m 
                        WHERE 
                            m.date 
                        BETWEEN 
                            '2009-10-29' and '2017-09-08' 
                        ORDER BY 
                            date;""", con)

print(moon_df)

df = pd.read_sql("""SELECT 
                        b.bite_date, 
                        b.SpeciesIDDesc, 
                        b.BreedIDDesc, 
                        b.GenderIDDesc, 
                        b.color, 
                        b.victim_zip, 
                        b.WhereBittenIDDesc, 
                        b.ResultsIDDesc, 
                        m.date, 
                        m.illum_pct, 
                        m.phase
                    FROM 
                        bites b 
                    LEFT JOIN moon m ON 
                        m.date = b.bite_date 
                    WHERE 
                        b.bite_date 
                    BETWEEN 
                        '2009-10-29' and '2017-09-08' 
                    ORDER BY 
                        bite_date;""", con)

print(df)

con.close()
