module Main where

    ru_currents = [5000, 1000, 500, 200, 100, 50, 10, 5, 2, 1]
    usa_currents = reverse [1, 2, 5, 10, 15, 25, 50]
    
    exchange :: [Integer] -> Integer -> [(Integer, Integer)]
    exchange currents amount
        | amount == 0 = []
        | notes == 0 = exchange (tail currents) amount
        | otherwise = (current, notes): exchange (tail currents) remainder
            where 
                current = head currents
                (notes, remainder) = divMod amount current
    

    ru_exchange = exchange ru_currents

    count_change :: [Integer] -> Integer -> Integer
    count_change currents amount
        | length currents == 0 = 0
        | amount < 0 = 0
        | amount == 0 = 1
        | otherwise = (count_change (tail currents) amount) + (count_change currents (amount - (head currents))) 

    usa_count_change = count_change usa_currents

    main :: IO()
    main = do
        putStrLn "Enter money amount: "
        amount <- getLine
        putStrLn "Exchange: "
        print (ru_exchange (read amount :: Integer))
        putStrLn "Count exchanges: "
        print (usa_count_change (read amount :: Integer))
